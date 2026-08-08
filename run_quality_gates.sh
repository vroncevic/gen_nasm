#!/bin/bash
#
# @brief   gen_nasm
# @version v1.0.3
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_nasm
python3 gates/gates/isp_checker.py gen_nasm
python3 gates/gates/limits_checker.py gen_nasm
python3 gates/gates/srp_checker.py gen_nasm

echo "Done"
