# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenNasmBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_nasm.setup.bundle import GenNasmBundle
from gen_nasm.setup.factory import GenNasmBundleFactory


class TestGenNasmBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenNasmBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenNasmBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_nasm/infrastructure/config/gen_nasm.cfg'}
        bundle = GenNasmBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenNasmBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenNasmBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenNasmBundleFactory.get_version(), '1.0.4')
