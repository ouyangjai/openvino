"""
 Copyright (C) 2018-2021 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import logging as log

from extensions.ops.dequantize_linear import DequantizeLinear
from mo.front.extractor import FrontExtractorOp
from mo.front.onnx.extractors.utils import onnx_attr, get_onnx_opset_version


class DequantizeLinearFrontExtractor(FrontExtractorOp):
    op = 'DequantizeLinear'
    enabled = True

    @classmethod
    def extract(cls, node):
        if get_onnx_opset_version(node) >= 13:
            log.warning('Ignoring "axis" attribute for DequantizeLinear-{} node, inference might be incorrect.'.format(
                get_onnx_opset_version(node)))
        DequantizeLinear.update_node_stat(node)
        return cls.enabled
