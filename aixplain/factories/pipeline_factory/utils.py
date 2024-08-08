__author__ = "aixplain"
import logging

from aixplain.enums import DataType
import aixplain.utils.config as config
from aixplain.modules.pipeline import Pipeline
from aixplain.modules.pipeline.designer import (
    Input,
    Output,
    AssetNode,
    Router,
    Route,
    Link,
)
from typing import Dict


def build_from_response(response: Dict, load_architecture: bool = False) -> Pipeline:
    """Converts response Json to 'Pipeline' object

    Args:
        response (Dict): Json from API
        load_architecture (bool, optional): If True, the architecture will be loaded. Defaults to False.

    Returns:
        Pipeline: Coverted 'Pipeline' object
    """
    if "api_key" not in response:
        response["api_key"] = config.TEAM_API_KEY

    # instantiating pipeline generic info
    pipeline = Pipeline(response["id"], response["name"], response["api_key"])
    if load_architecture is True:
        try:
            # instantiating nodes
            for node_json in response["nodes"]:
                if node_json["type"].lower() == "input":
                    node = Input(
                        data=node_json["data"] if "data" in node_json else None,
                        data_types=[DataType(dt) for dt in node_json["dataType"]],
                    )
                elif node_json["type"].lower() == "asset":
                    node = AssetNode(asset_id=node_json["assetId"])
                elif node_json["type"].lower() == "segmentor":
                    raise NotImplementedError()
                elif node_json["type"].lower() == "reconstructor":
                    raise NotImplementedError()
                elif node_json["type"].lower() == "decision":
                    raise NotImplementedError()
                elif node_json["type"].lower() == "router":
                    node = Router(routes=[Route(**route) for route in node_json["routes"]])
                elif node_json["type"].lower() == "script":
                    raise NotImplementedError()
                elif node_json["type"].lower() == "output":
                    node = Output()
                node.number = node_json["number"]
                node.label = node_json["label"]
                pipeline.add_node(node)

            # instantiating links
            for link_json in response["links"]:
                for param_mapping in link_json["paramMapping"]:
                    link = Link(
                        from_node=pipeline.get_node(link_json["from"]),
                        to_node=pipeline.get_node(link_json["to"]),
                        from_param=param_mapping["from"],
                        to_param=param_mapping["to"],
                    )
                    pipeline.add_link(link)
        except Exception as e:
            logging.warning("Error loading pipeline architecture:, error: %s", e)
            pipeline.nodes = []
            pipeline.links = []
    return pipeline
