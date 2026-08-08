# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_nasm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_nasm.setup.bundle import GenNasmBundle
from gen_nasm.setup.options import GenNasmBundleOptions
from gen_nasm.setup.registry import GenNasmBundleRegistry
from gen_nasm.setup.dependencies import GenNasmBundleDependencies
from gen_nasm.setup.opt_validator import GenNasmBundleOptionsValidator
from gen_nasm.setup.keys import GenNasmBundleKeys
from gen_nasm.core.service.engine import Service
from gen_nasm.infrastructure.subprocessor import SubProcessor
from gen_nasm.infrastructure.cli.engine import CLI
from gen_nasm.infrastructure.cli.setup.bundle import CLIBundle
from gen_nasm.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_nasm.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_nasm.infrastructure.command.command import CommandBundle
from gen_nasm.infrastructure.command.gen_nasm_command_definition import GenNasmCommandDefinition
from gen_nasm.infrastructure.command.gen_nasm_command_executor import GenNasmCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_nasm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_nasm/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenNasmBundleFactory:
    '''
        Factory for creating the gen_nasm bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_nasm info file.
            :methods:
                | create_bundle - Creates the gen_nasm bundle with optional pre-configured options.
    '''

    _info_file: str = 'gen_nasm/infrastructure/config/gen_nasm.cfg'

    @classmethod
    def create_bundle(cls, options: GenNasmBundleOptions | None = None) -> GenNasmBundle:
        '''
            Creates the gen_nasm bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_nasm bundle.
            :return: The gen_nasm bundle.
            :exceptions:
                | ATSValueError: The gen_nasm bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_nasm bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_nasm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_nasm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_nasm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_nasm bundle must be an instance of GenNasmBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenNasmBundleOptionsValidator.validate(options)

        info_file = options.get(GenNasmBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_nasm_definition: GenNasmCommandDefinition = GenNasmCommandDefinition()

        gen_nasm_bundle: CommandBundle = CommandBundle(
            definition=gen_nasm_definition,
            executor=GenNasmCommandExecutor(gen_nasm_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_nasm_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenNasmBundleRegistry.create_bundle(
            dependencies=GenNasmBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
