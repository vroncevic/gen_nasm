#!/bin/bash
#
# @brief   gen_nasm
# @version v1.0.3
# @date    Wed Jun 19 06:28:16 AM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_nasm_coverage.xml gen_nasm_coverage.json .coverage
rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
python3 -m coverage run -m --source=../gen_nasm unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_nasm_coverage.xml 
python3 -m coverage json -o gen_nasm_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n gen_nasm
rm htmlcov/.gitignore
echo "Done"