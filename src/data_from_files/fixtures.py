#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
"""Fixtures to load test data."""
import typing

import pytest

from . import constants, loader, modinfo

if typing.TYPE_CHECKING:
    import _pytest


@pytest.fixture(scope='session')
def data_pattern(pytestconfig: '_pytest.config.Config'):
    """Fixture provides glob path pattern for test data files.

    .. todo:: This does not look worked.
    """
    return pytestconfig.getoption(constants.OPT_DATA_PATTERN)


@pytest.fixture(scope='module')
def module_info(request: pytest.FixtureRequest):
    """Fixture provides some path info of the target module."""
    return modinfo.get_test_data_info_for_target(request)


# .. note:: To disable pylint's warning about the reuse of fixture.
# pylint: disable=redefined-outer-name
@pytest.fixture
def test_data(module_info, pytestconfig):
    """Fixture provides test data loaded from files automatically."""
    data_pattern = pytestconfig.getoption(constants.OPT_DATA_PATTERN)

    if module_info.subdirs:
        return list(
            list(loader.each_data_under_dir(
                module_info.datadir / subdir, data_pattern
            ))
            for subdir in module_info.subdirs
        )

    return list(loader.each_data_under_dir(module_info.datadir, data_pattern))

# vim:sw=4:ts=4:et:
