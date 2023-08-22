import requests
import pytest
import httpretty

from unittest.mock import patch

from aixplain.client import (AixplainClient,
                             create_retry_session,
                             DEFAULT_RETRY_TOTAL,
                             DEFAULT_RETRY_BACKOFF_FACTOR,
                             DEFAULT_RETRY_STATUS_FORCELIST)


BASE_URL = 'https://api.example.com'


def setup_function():
    httpretty.enable()


def teardown_function():
    httpretty.disable()


def test_create_retry_session_defaults():
    session = create_retry_session()
    assert session
    assert session.adapters
    for _, adapter in session.adapters.items():
        retry = adapter.max_retries
        assert retry.total == DEFAULT_RETRY_TOTAL
        assert retry.backoff_factor == DEFAULT_RETRY_BACKOFF_FACTOR
        assert retry.status_forcelist == DEFAULT_RETRY_STATUS_FORCELIST


@pytest.mark.parametrize(
    "total, backoff_factor, status_forcelist",
    [
        (5, 0.3, [502]),
        (3, 0.1, [503, 504]),
        (10, 0.5, [500]),
    ]
)
def test_create_retry_session_customs(total,
                                      backoff_factor,
                                      status_forcelist):
    session = create_retry_session(
        total=total,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist
    )
    
    assert session
    assert session.adapters
    for _, adapter in session.adapters.items():
        retry = adapter.max_retries
        assert retry.total == total
        assert retry.backoff_factor == backoff_factor
        assert retry.status_forcelist == status_forcelist


def test_client_constructor_defaults():
    aixplain_api_key = 'some_key'

    mock_session = requests.Session()
    with patch('aixplain.client.create_retry_session',
               return_value=mock_session) as mock_create_retry:
        client = AixplainClient(BASE_URL, aixplain_api_key=aixplain_api_key)

        assert client.base_url == BASE_URL
        assert client.aixplain_api_key == aixplain_api_key
        assert client.team_api_key is None

        # session
        assert client.session == mock_session

        # session headers
        assert 'x-aixplain-key' in client.session.headers
        assert client.session.headers['x-aixplain-key'] == aixplain_api_key
        assert 'x-api-key' not in client.session.headers

        mock_create_retry.assert_called_once_with(
            total=None,
            backoff_factor=None,
            status_forcelist=None
        )


def test_client_constructor_customs():
    aixplain_api_key = 'some_key'
    team_api_key = 'some_other_key'

    # Should fail when both keys set
    with pytest.raises(ValueError):
        client = AixplainClient(BASE_URL,
                                team_api_key=team_api_key,
                                aixplain_api_key=aixplain_api_key)

    # Should fail when none of the keys set
    with pytest.raises(ValueError):
        client = AixplainClient(BASE_URL)

    # Should be initialized with custom kwargs
    mock_session = requests.Session()
    with patch('aixplain.client.create_retry_session',
               return_value=mock_session) as mock_create_retry:

        custom_total = 5
        custom_backoff_factor = 0.3
        custom_status_forcelist = [502]
        client = AixplainClient(BASE_URL,
                                team_api_key=team_api_key,
                                retry_total=custom_total,
                                retry_backoff_factor=custom_backoff_factor,
                                retry_status_forcelist=custom_status_forcelist)

        assert client.base_url == BASE_URL
        assert client.aixplain_api_key is None
        assert client.team_api_key == team_api_key

        # session
        assert client.session == mock_session

        # session headers
        assert 'x-api-key' in client.session.headers
        assert client.session.headers['x-api-key'] == team_api_key
        assert 'x-aixplain-key' not in client.session.headers

        mock_create_retry.assert_called_once_with(
            total=custom_total,
            backoff_factor=custom_backoff_factor,
            status_forcelist=custom_status_forcelist
        )


@httpretty.activate
def test_request():
    success_url = f'{BASE_URL}/success'
    fail_url = f'{BASE_URL}/fail'
    httpretty.register_uri(httpretty.GET, success_url, body='OK', status=200)
    httpretty.register_uri(httpretty.GET, fail_url, body='NOK', status=500)

    client = AixplainClient(BASE_URL, aixplain_api_key='some_key')
    response = client.get('success')
    assert response.status_code == 200
    assert response.text == 'OK'

    with pytest.raises(requests.RequestException):
        response = client.get('fail')
