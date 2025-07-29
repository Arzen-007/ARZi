#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ARZi.utils import set_config
from tests.helpers import create_arzi, destroy_arzi


def test_legal_settings():
    app = create_arzi()
    with app.app_context():
        set_config("tos_text", "Terms of Service")
        set_config("privacy_text", "Privacy Policy")

        with app.test_client() as client:
            r = client.get("/register")
            assert r.status_code == 200
            assert "privacy policy" in r.get_data(as_text=True)
            assert "terms of service" in r.get_data(as_text=True)

            r = client.get("/tos")
            assert r.status_code == 200
            assert "Terms of Service" in r.get_data(as_text=True)

            r = client.get("/privacy")
            assert r.status_code == 200
            assert "Privacy Policy" in r.get_data(as_text=True)
    destroy_arzi(app)
