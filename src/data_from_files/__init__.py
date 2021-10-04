#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
"""Fixtures and hooks to load test data."""
from .fixtures import (  # noqa: F401
    module_info, test_data
)
from .hooks import pytest_addoption  # noqa: F401
