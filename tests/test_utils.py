#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring
"""Test cases for tests.utils."""
from . import utils as TT


def test_get_basename():
    assert TT.get_basename(__file__) == 'utils'

# vim:sw=4:ts=4:et:
