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

import numpy as np

from mo.front.extractor import FrontExtractorOp
from mo.front.mxnet.extractors.utils import get_mxnet_layer_attrs
from mo.ops.slice import MXSlice


class SliceFrontExtractor(FrontExtractorOp):
    op = 'slice'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        node_attrs = {
            'crop_begin': np.array(attrs.tuple("begin", int, ())),
            'crop_end': np.array(attrs.tuple("end", int, ())),
            'step': np.array(attrs.tuple("step", int, ())),
        }

        MXSlice.update_node_stat(node, node_attrs)
        return cls.enabled
