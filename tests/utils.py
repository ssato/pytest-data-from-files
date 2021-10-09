#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring
"""Common constant variables for test cases."""
import pathlib


def get_basename(path: str) -> str:
    """Extract basename from given path ``path``."""
    return pathlib.Path(path).name.replace('.py', '').replace('test_', '')

# vim:sw=4:ts=4:et:
