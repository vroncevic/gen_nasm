# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_nasm components for simplification of gen_nasm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_nasm.core.service.iservice import IService
from gen_nasm.core.service.isubprocessor import ISubProcessor
from gen_nasm.infrastructure.cli.icli import ICLI
from gen_nasm.setup.bundle import GenNasmBundle
from gen_nasm.setup.validator import GenNasmBundleValidator
from gen_nasm.setup.keys import GenNasmBundleKeys
from gen_nasm.setup.dependencies import GenNasmBundleDependencies
from gen_nasm.setup.dep_validator import GenNasmBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_nasm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_nasm/blob/dev/LICENSE'
__version__ = '1.0.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenNasmBundleRegistry:
    '''
        Encapsulates core gen_nasm components for simplification of gen_nasm bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_nasm bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenNasmBundleDependencies) -> GenNasmBundle:
        '''
            Creates the gen_nasm bundle.

            :param dependencies: The gen_nasm bundle dependencies.
            :return: The gen_nasm bundle.
            :exceptions:
                | ATSValueError: The gen_nasm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_nasm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_nasm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_nasm bundle must be an instance of GenNasmBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenNasmBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenNasmBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenNasmBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenNasmBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenNasmBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenNasmBundle = GenNasmBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenNasmBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
