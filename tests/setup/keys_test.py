# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenNasmBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_nasm.setup.keys import GenNasmBundleKeys


class TestGenNasmBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenNasmBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenNasmBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenNasmBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenNasmBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenNasmBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenNasmBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenNasmBundleKeys.OPTION_INFO_FILE, opts)
