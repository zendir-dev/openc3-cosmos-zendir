# Copyright 2025 OpenC3, Inc.
# All Rights Reserved.
#
# This program is free software; you can modify and/or redistribute it
# under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation; version 3 with
# attribution addendums as found in the LICENSE.txt
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# This file may also be used under the terms of a commercial license
# if purchased from OpenC3, Inc.

import math
import statistics
from openc3.processors.processor import Processor


class HashProcessor(Processor):
    # @param item_name [String] The name of the item to gather statistics on
    # @param value_type #See Processor::initialize
    def __init__(self, item_name, value_type="CONVERTED"):
        super().__init__(value_type)
        self.item_name = str(item_name).upper()
        self.reset()

    # Run statistics on the item
    #
    # See Processor#call
    def call(self, packet, buffer):
        result = packet.read(self.item_name, self.value_type, buffer)
        for key, value in result.items():
            self.results[key] = value

    # Reset any state
    def reset(self):
        self.results = {}

    # Convert to configuration file string
    def to_config(self):
        return f"  PROCESSOR {self.name} {self.__class__.__name__} {self.item_name} {self.value_type}\n"

    def as_json(self):
        return {
            "name": self.name,
            "class": self.__class__.__name__,
            "params": [self.item_name, self.value_type],
        }
