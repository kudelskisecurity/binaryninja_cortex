#!/bin/bash
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

#This script generates header files from libopencm3 to be parsed by the plugin

if [[ "$#" -ne 1 ]]; then
    echo "Usage : $0 <libopencm3_dir>"
    exit 0
fi
OCM3_DIR=$1
OCM3_INCLUDE_DIR=$OCM3_DIR/include/

MCUS=( "STM32F0" "STM32F1" "STM32F2" "STM32F3" "STM32F4" "STM32F7" "STM32L0" "STM32L1" "STM32L4" "EFM32TG" "EFM32G" "EFM32LG" "EFM32GG" "EFM32HG" "EFM32WG" "EZR32WG" "LPC13XX" "LPC17XX" "LPC43XX_M4" "LPC43XX_M0" "SAM3A" "SAM3N" "SAM3S" "SAM3U" "SAM3X" "SAM4L" "SAMD" "LM3S" "LM4F" "MSP432E4" "VF6XX" )


for i in "${MCUS[@]}"
do
    echo "from binaryninja_cortex.platforms import MCU" > $i.py
    echo "" >> $i.py
    echo "class Chip(MCU):" >> $i.py
    echo "    NAME=\"$i\"" >> $i.py
    python2 $OCM3_DIR/scripts/genlink.py $OCM3_DIR/ld/devices.data $i DEFS | sed -nr 's/-D_/\n    /gp' | sed -nr 's/(R[OA]M_OFF)=(0x[0-9A-F]+)/\1=\2/p' >> $i.py
    echo "" >> $i.py
    echo "    IRQ=MCU.IRQ+ [" >> $i.py
    echo "#include \"libopencm3/cm3/vector.h\"" | gcc -D$i -I$OCM3_INCLUDE_DIR -fno-builtin -E -dD -x c -P - | grep -E "NVIC\w*_IRQ" | sed -nr 's/^.*(NVIC_\w+_IRQ) (\w+)/        "\1",/p' >> $i.py
    echo "        ]">> $i.py


done
