# Copyright 2018 Nagravision SA
# 
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from binaryninja.architecture import Architecture
from binaryninja.binaryview import BinaryView
from binaryninja.log import log_error
from binaryninja.types import Symbol, Type
from binaryninja.enums import (BranchType, InstructionTextTokenType, LowLevelILOperation, LowLevelILFlagCondition, FlagRole, SegmentFlag, SymbolType)
from binaryninja.interaction import get_open_filename_input, get_choice_input

import struct
import importlib

class CortexView(BinaryView):
    name = "CortexFirmware"
    long_name = "ARM Cortex Firmware file"

    def __init__(self, data):
        BinaryView.__init__(self, parent_view = data, file_metadata = data.file)
        self.platform= Architecture['thumb2'].standalone_platform
        self.MCUS=[
            "STM32F0",
            "STM32F1",
            "STM32F2",
            "STM32F3",
            "STM32F4",
            "STM32F7",
            "STM32L0",
            "STM32L1",
            "STM32L4",
            "EFM32TG",
            "EFM32G",
            "EFM32LG",
            "EFM32GG",
            "EFM32HG",
            "EFM32WG",
            "EZR32WG",
            "LPC13XX",
            "LPC17XX",
            "LPC43XX_M4",
            "LPC43XX_M0",
            "SAM3A",
            "SAM3N",
            "SAM3S",
            "SAM3U",
            "SAM3X",
            "SAM4L",
            "SAMD",
            "LM3S",
            "LM4F",
            "MSP432E4",
            "VF6XX",
            ]

    def init(self):

        user_choice = get_choice_input("Select MCU family", "MCU selection", self.MCUS)
        if user_choice is not None:
            chosen_mcu = self.MCUS[user_choice]
            mcu_lib = importlib.import_module("binaryninja_cortex.platforms."+chosen_mcu)
            mcu = mcu_lib.Chip
        else:
            mcu_lib = importlib.import_module("binaryninja_cortex.platforms")
            mcu = mcu_lib.MCU


        #Add RAM segment
        self.add_auto_segment(mcu.RAM_OFF, 0xffff, 0, 0, SegmentFlag.SegmentReadable | SegmentFlag.SegmentWritable | SegmentFlag.SegmentExecutable)

        # Add peripherals segment
        self.add_auto_segment(mcu.PERIPH_OFF, 0x10000000, 0, 0, SegmentFlag.SegmentReadable | SegmentFlag.SegmentWritable)

        #Add flash segment, assume flash < 2MB
        self.add_auto_segment(mcu.ROM_OFF, 0x200000, 0, 0x200000, SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable)

        #Add IVT symbols

        #SP_VALUE is a data pointer
        self.define_auto_symbol_and_var_or_function(
                Symbol(SymbolType.DataSymbol, 
                    mcu.ROM_OFF,
                    mcu.IRQ[0]),
                Type.pointer(self.arch, Type.void(), const=True),
                self.platform)
        addr = struct.unpack("<I", self.parent_view.read(0, 4))[0]
        self.define_auto_symbol(Symbol(SymbolType.DataSymbol,
            addr, "p_{}".format(mcu.IRQ[0])))

        #All other vectory are function pointers
        for i in range(1, len(mcu.IRQ)):
            self.define_auto_symbol_and_var_or_function(
                    Symbol(SymbolType.DataSymbol, 
                        mcu.ROM_OFF+(4*i), 
                        mcu.IRQ[i]),
                    Type.pointer(self.arch, Type.void(), const=True),
                    self.platform)
            addr = struct.unpack("<I", self.parent_view.read(4*i, 4))[0]&~1
            self.define_auto_symbol(Symbol(SymbolType.FunctionSymbol,
                addr, "f_{}".format(mcu.IRQ[i])))
            self.add_function(addr, self.platform)

        #Add entry point to RESET_IRQ
        self.add_entry_point(self.symbols['f_RESET_IRQ'].address, self.platform)

        return True

    @classmethod
    def is_valid_for_data(self, data):
        #Read two DWORDS
        ivt = data.read(0, 8)
        if ord(ivt[3])>0x20:
            #SP value should be in SRAM (max 0x20......)
            return False
        if ord(ivt[7])>0x08:
            #Reset vector should be in flash (max 0x08......)
            return False
        return True

    def perform_get_entry_point(self):
        return self.symbols['f_RESET_IRQ'].address
        

CortexView.register()
