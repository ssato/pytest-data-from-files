#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
"""Fixtures and hooks to load test data automatically."""
from .datatypes import (
    ModuleInfo, DataInfo
)
from .fixtures import (
    test_data_info, test_data
)
from .hooks import pytest_addoption

__all__ = [
    'ModuleInfo', 'DataInfo',
    'test_data_info', 'test_data',
    'pytest_addoption',
]
