#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.helpers import create_arzi, destroy_arzi, gen_user


def test_arzi_setup_redirect():
    """Test that a fresh ARZi instance redirects to /setup"""
    app = create_arzi(setup=False)
    with app.app_context():
        with app.test_client() as client:
            r = client.get("/users")
            assert r.status_code == 302
            assert r.location == "http://localhost/setup"

            # Files in /themes load properly
            r = client.get("/themes/core/static/css/main.dev.css")
            r = client.get("/themes/core/static/css/main.min.css")
            assert r.status_code == 200
    destroy_arzi(app)


def test_arzi_setup_verification():
    app = create_arzi(setup=False)
    with app.app_context():
        with app.test_client() as client:
            r = client.get("/setup")
            assert r.status_code == 200

            with client.session_transaction() as sess:
                data = {
                    "ctf_name": "ARZi",
                    "ctf_description": "CTF description",
                    "name": "test",
                    "email": "test@examplectf.com",
                    "password": "",
                    "user_mode": "users",
                    "nonce": sess.get("nonce"),
                }
            r = client.post("/setup", data=data)
            assert "longer password" in r.get_data(as_text=True)

            gen_user(app.db, name="test", email="test@examplectf.com")

            data["password"] = "password"
            r = client.post("/setup", data=data)
            resp = r.get_data(as_text=True)
            assert "email has already been used" in resp
            assert "name is already taken" in resp

            data["name"] = "admin"
            data["email"] = "admin@examplectf.com"
            r = client.post("/setup", data=data)
            assert r.status_code == 302
            assert r.location == "http://localhost/"
    destroy_arzi(app)
