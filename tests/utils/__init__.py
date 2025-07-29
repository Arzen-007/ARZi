#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ARZi.utils import get_config, set_config
from tests.helpers import create_arzi, destroy_arzi


def test_ctf_version_is_set():
    """Does ctf_version get set correctly"""
    app = create_arzi()
    with app.app_context():
        assert get_config("ctf_version") == app.VERSION
    destroy_arzi(app)


def test_get_config_and_set_config():
    """Does get_config and set_config work properly"""
    app = create_arzi()
    with app.app_context():
        assert get_config("setup") == True
        config = set_config("TEST_CONFIG_ENTRY", "test_config_entry")
        assert config.value == "test_config_entry"
        assert get_config("TEST_CONFIG_ENTRY") == "test_config_entry"
    destroy_arzi(app)
