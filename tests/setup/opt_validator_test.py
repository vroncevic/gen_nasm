# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenNasmBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_nasm.setup.opt_validator import GenNasmBundleOptionsValidator


class TestGenNasmBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenNasmBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenNasmBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenNasmBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenNasmBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenNasmBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenNasmBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenNasmBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenNasmBundleOptionsValidator.is_valid({'info_file': 123}))
