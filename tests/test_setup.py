#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ARZi.utils import get_config
from ARZi.utils.security.csrf import generate_nonce
from ARZi.utils.security.signing import serialize
from tests.helpers import create_arzi, destroy_arzi, login_as_user, register_user


def test_setup_integrations():
    app = create_arzi()
    with app.app_context():
        register_user(app)
        user = login_as_user(app)
        r = user.get("/setup/integrations")
        assert r.status_code == 403

        admin = login_as_user(app, "admin")
        r = admin.get("/setup/integrations")
        assert r.status_code == 403

        admin = login_as_user(app, "admin")

        url = "/setup/integrations?state={state}&mlc_client_id=client_id&mlc_client_secret=client_secret&name=mlc".format(
            state=serialize(generate_nonce())
        )
        r = admin.get(url)
        assert r.status_code == 200
        assert get_config("oauth_client_id") == "client_id"
        assert get_config("oauth_client_secret") == "client_secret"
    destroy_arzi(app)
