#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.testing import FlaskClient

from tests.helpers import create_arzi, destroy_arzi, login_as_user


def test_api_csrf_failure():
    """Test that API requests require the CSRF-Token header"""
    app = create_arzi()
    app.test_client_class = FlaskClient
    with app.app_context():
        with login_as_user(app, "admin") as client:
            r = client.post(
                "/api/v1/challenges",
                json={
                    "name": "chal",
                    "category": "cate",
                    "description": "desc",
                    "value": "100",
                    "state": "hidden",
                    "type": "standard",
                },
            )
            assert r.status_code == 403

            with client.session_transaction() as sess:
                nonce = sess.get("nonce")

            r = client.post(
                "/api/v1/challenges",
                headers={"CSRF-Token": nonce},
                json={
                    "name": "chal",
                    "category": "cate",
                    "description": "desc",
                    "value": "100",
                    "state": "hidden",
                    "type": "standard",
                },
            )
            assert r.status_code == 200
    destroy_arzi(app)
