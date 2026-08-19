# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_nasm is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_nasm is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    GenNasm bundle dependencies for the gen_nasm bundle.
'''

from __future__ import annotations

from typing import TypedDict

from ats_utilities.base.setup.bundle import BaseBundle

from gen_nasm.core.service.iservice import IService
from gen_nasm.core.service.isubprocessor import ISubProcessor
from gen_nasm.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_nasm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_nasm/blob/dev/LICENSE'
__version__ = '1.0.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenNasmBundleDependencies(TypedDict):
    '''
        GenNasm bundle dependencies for the gen_nasm bundle.

        It defines:

            :attributes:
                | base - The base bundle with the base components for the gen_nasm bundle.
                | service - The service orchestrating the gen_nasm's execution for the gen_nasm bundle.
                | subprocessor - The adapter executing the gen_nasm's sub-processes for the gen_nasm bundle.
                | cli - The command-line interface adapter for the gen_nasm bundle.
    '''

    base: BaseBundle
    service: IService
    subprocessor: ISubProcessor
    cli: ICLI
