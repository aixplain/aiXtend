import uuid

from enum import Enum
from dataclasses import dataclass, field, asdict, InitVar
from typing import Any, List, Tuple

# these are commented out because of circular imports, please fix it
# "any" is used to avoid circular imports, should be replaced with the correct
# type once the circular imports are fixed

# from aixplain.modules import Model
# from aixplain.modules import Dataset
# from aixplain.modules import Pipeline

from aixplain.factories import ModelFactory
from aixplain.factories import PipelineFactory
from aixplain.factories.file_factory import FileFactory
from aixplain.enums.function import FunctionInputOutput


class DataType(str, Enum):
    TEXT = 'text'
    IMAGE = 'image'
    AUDIO = 'audio'
    VIDEO = 'video'
    LABEL = 'label'


class NodeType(str, Enum):
    ASSET = 'ASSET'
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    SCRIPT = 'SCRIPT'
    SEGMENTOR = 'SEGMENTOR'
    RECONSTRUCTOR = 'RECONSTRUCTOR'
    ROUTER = 'ROUTER'
    DECISION = 'DECISION'


class AssetType(str, Enum):
    MODEL = 'MODEL'


class FunctionType(str, Enum):
    AI = 'AI'
    SEGMENTOR = 'SEGMENTOR'
    RECONSTRUCTOR = 'RECONSTRUCTOR'


@dataclass
class ParamMapping:
    from_param: str
    to_param: str


@dataclass
class Link:
    from_node: int
    to_node: int
    paramMapping: List[ParamMapping] = field(default_factory=list)


@dataclass
class Param:
    code: str
    dataType: DataType
    value: str
    node: InitVar['Node'] = None

    def __post_init__(self, node: 'Node' = None):
        self.node = node

    def link(self, to_param: 'Param') -> 'Param':
        assert self.node, 'Param not added to a node'
        to_param.back_link(self)

    def back_link(self, from_param: 'Param') -> 'Param':
        assert self.node, 'Param not added to a node'
        from_param.node.link(self.node, from_param.code, self.code)


@dataclass
class Route:
    value: DataType
    path: List[int] = field(default_factory=list)
    operation: str = 'equal'
    type: str = 'checkType'


class ParamProxy:
    def __init__(self, params: List[Param]):
        self.params = params

    def get_param(self, code: str) -> Param:
        for param in self.params:
            if param.code == code:
                return param
        raise ValueError(f'Param {code} not found')

    def set_param(self, code: str, value: any) -> None:
        param = self.get_param(code)
        param.value = value

    def __call__(self, code: str) -> Param:
        return self.get_param(code)

    def __getitem__(self, code: str) -> Param:
        return self.get_param(code)

    def __getattr__(self, name: str) -> Any:
        return self.get_param(name)


@dataclass
class Node:
    pipeline: InitVar['Pipeline'] = None
    number: int = field(default=None, init=False)
    label: str = field(default=None, init=False)
    type: NodeType = field(default=None, init=False)
    inputValues: List[Param] = field(default_factory=list, init=False)
    outputValues: List[Param] = field(default_factory=list, init=False)

    def __post_init__(self, pipeline=None):
        if pipeline:
            pipeline.add_node(self)
        self.pipeline = pipeline
        self.inputs = ParamProxy(self.inputValues)
        self.outputs = ParamProxy(self.outputValues)

    def use_output(self, param_code: str) -> 'Node':
        assert self.pipeline, 'Node not added to a pipeline'
        output = self.pipeline.node(Output)
        self.outputs[param_code].link(output.inputs.output)
        return output

    def asdict(self) -> dict:
        return asdict(self)

    def add_input_param(
        self,
        code: str,
        dataType: DataType,
        value: any = None
    ) -> 'Node':
        self.inputValues.append(
            Param(code=code, dataType=dataType, value=value, node=self)
        )
        return self

    def add_output_param(
        self,
        code: str,
        dataType: DataType,
        value: any = None
    ) -> 'Node':
        self.outputValues.append(
            Param(code=code, dataType=dataType, value=value, node=self)
        )
        return self

    def link(self, to_node: 'Node', from_param: str = None,
             to_param: str = None) -> 'Node':

        pipeline = self.pipeline or to_node.pipeline
        assert pipeline, 'Node not added to a pipeline'

        self.pipeline = pipeline
        to_node.pipeline = pipeline

        param_mapping = []
        if from_param and to_param:
            param_mapping = [
                ParamMapping(from_param=from_param, to_param=to_param)
            ]
        link = Link(from_node=self.number, to_node=to_node.number,
                    paramMapping=param_mapping)
        return self.pipeline.add_link(link)


@dataclass
class Asset(Node):
    assetId: str = None
    function: str = None
    supplier: str = None
    version: str = None
    assetType: AssetType = AssetType.MODEL
    functionType: FunctionType = FunctionType.AI
    instance: InitVar[any] = None

    type: NodeType = NodeType.ASSET

    def __post_init__(self, pipeline: any = None, instance: any = None):
        super().__post_init__(pipeline=pipeline)
        if not self.assetId and not self.instance:
            raise ValueError('assetId or instance is required')

        if not self.instance:
            instance = ModelFactory.get(self.assetId)

        function = FunctionInputOutput[instance.function.value]['spec']
        self.function = instance.function.value
        self.supplier = instance.supplier.value['code']
        self.version = instance.version
        self.instance = instance
        self.assetId = instance.id

        for item in function['params']:
            self.add_input_param(code=item['code'],
                                 dataType=item['dataType'])

        for item in function['output']:
            self.add_output_param(code=item['code'],
                                  dataType=item['dataType'])


@dataclass
class Input(Node):
    dataType: List[DataType] = field(default_factory=list)
    data: str = None
    type: NodeType = NodeType.INPUT

    def __post_init__(self, pipeline: any = None):
        super().__post_init__(pipeline=pipeline)
        if not self.dataType:
            self.dataType = [DataType.TEXT]

        self.add_output_param('input', self.dataType[0])

        if self.data:
            self.data = FileFactory.to_link(self.data)

    def route(self, conditions: List[Tuple[DataType, Param]]) -> 'Node':
        assert self.pipeline, 'Node not added to a pipeline'

        router = self.pipeline.router([
            (condition[0], condition[1].node) for condition in conditions
        ])
        self.link(router)
        for condition in conditions:
            router.outputs.input.link(condition[1])

        return router


@dataclass
class Output(Node):
    dataType: List[DataType] = field(default_factory=list)
    type: NodeType = NodeType.OUTPUT

    def __post_init__(self, pipeline: any = None):
        super().__post_init__(pipeline=pipeline)
        if not self.dataType:
            self.dataType = [DataType.TEXT]

        self.add_input_param('output', self.dataType[0])


@dataclass
class Script(Node):
    fileUrl: str = None
    script_path: InitVar[str] = None
    type: NodeType = NodeType.SCRIPT

    def __post_init__(self, pipeline: any = None, script_path: str = None):
        super().__post_init__(pipeline=pipeline)
        if script_path:
            self.fileUrl = FileFactory.create(local_path=script_path)
        if not self.fileUrl:
            raise ValueError('fileUrl is required')


@dataclass
class Router(Node):
    routes: List[Route] = field(default_factory=list)
    type: NodeType = NodeType.ROUTER

    def __post_init__(self, pipeline):
        super().__post_init__(pipeline)
        self.add_output_param('input', None)


@dataclass
class Pipeline:
    nodes: List[Node] = field(default_factory=list)
    links: List[Link] = field(default_factory=list)
    number_of_nodes: InitVar[int] = 0
    instance: InitVar[any] = None

    def add_node(self, node: Node):
        node.pipeline = self
        if not node.number:
            node.number = self.number_of_nodes
            self.number_of_nodes += 1

        if not node.label:
            node.label = f'{node.type.value}-{node.number}'

        self.nodes.append(node)
        return node

    def add_nodes(self, *nodes: Node) -> List[Node]:
        return [self.add_node(node) for node in nodes]

    def add_link(self, link: Link) -> Node:
        self.links.append(link)
        return link

    def node(self, node_cls, *args, **kwargs) -> Node:
        return self.add_node(node_cls(*args, **kwargs))

    def input(self, data: str = None, **kwargs) -> Node:
        return self.node(Input, data=data, **kwargs)

    def asset(self, assetId: str, *args, **kwargs) -> Node:
        return self.node(Asset, assetId=assetId, **kwargs)

    def output(self, *args, **kwargs) -> Node:
        return self.node(Output, *args, **kwargs)

    def router(self, routes: List[Tuple[DataType, Node]] = None,
               **kwargs) -> Node:
        return self.node(Router, routes=[
            Route(value=route[0], path=[route[1].number]) for route in routes
        ])

    def to_dict(self) -> dict:
        obj = asdict(self)
        for link in obj['links']:
            link['from'] = link.pop('from_node')
            link['to'] = link.pop('to_node')
            params = link.get('paramMapping', []) or []
            for param in params:
                param['from'] = param.pop('from_param')
                param['to'] = param.pop('to_param')
        return obj

    def save(self) -> 'Pipeline':
        name = f'pipeline-{uuid.uuid4()}'
        self.instance = PipelineFactory.create(name, self.to_dict())
        return self

    def run(self, *args, **kwargs) -> any:
        if not self.instance:
            raise ValueError('Pipeline not saved')

        return self.instance.run(*args, **kwargs)
