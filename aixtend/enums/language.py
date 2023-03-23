__author__ = "aiXplain"

"""
Copyright 2023 The aiXplain SDK authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author: aiXplain team
Date: March 22th 2023
Description:
    Language Enum
"""

import logging
import os
import traceback

from aixtend.utils import config
from aixtend.utils.file_utils import _request_with_retry
from enum import Enum


def load_languages():
    try:
        api_key = config.TEAM_API_KEY
        backend_url = config.BACKEND_URL

        url = os.path.join(backend_url, "sdk/languages")
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        r = _request_with_retry("get", url, headers=headers)
        resp = r.json()
        languages = {}
        for w in resp:
            language = w["value"]
            language_label = "_".join(w["label"].split())
            languages[language_label] = {"language": language, "dialect": ""}
            for dialect in w["dialects"]:
                dialect_label = "_".join(dialect["label"].split()).upper()
                dialect_value = dialect["value"]

                languages[language_label + "_" + dialect_label] = {"language": language, "dialect": dialect_value}
        return Enum("Language", languages, type=dict)
    except:
        msg = f"Language Loading Error:\n{traceback.format_exc()}"
        logging.warning(msg)
        raise Exception(msg)


Language = load_languages()
