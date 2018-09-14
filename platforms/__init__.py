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


class MCU(object):
    NAME=""
    ROM_OFF=0x0
    PERIPH_OFF=0x40000000
    RAM_OFF=0x20000000
    IRQ=[
        "SP_VALUE",
        "RESET_IRQ",
        "NMI_IRQ",
        "HARDFAULT_IRQ",
        "MEMORYMANAGE_IRQ",
        "BUSFAULT_IRQ",
        "USAGEFAULT_IRQ",
        "RESERVED",
        "RESERVED",
        "RESERVED",
        "RESERVED",
        "SVCALL_IRQ",
        "DEBUG_MONITOR_IRQ",
        "RESERVED",
        "PEND_SV_IRQ",
        "SYSTICK_IRQ",
        ]
