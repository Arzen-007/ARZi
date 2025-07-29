#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ARZi.models import Users
from ARZi.utils.crypto import verify_password
from tests.helpers import create_arzi, destroy_arzi, login_as_user, register_user


def test_email_cannot_be_changed_without_password():
    """Test that a user can't update their email address without current password"""
    app = create_arzi()
    with app.app_context():
        register_user(app)
        client = login_as_user(app)

        data = {"name": "user", "email": "user2@examplectf.com"}

        r = client.patch("/api/v1/users/me", json=data)
        assert r.status_code == 400
        user = Users.query.filter_by(id=2).first()
        assert user.email == "user@examplectf.com"

        data = {"name": "user", "email": "user2@examplectf.com", "confirm": "asdf"}

        r = client.patch("/api/v1/users/me", json=data)
        assert r.status_code == 400
        user = Users.query.filter_by(id=2).first()
        assert user.email == "user@examplectf.com"

        data = {"name": "user", "email": "user2@examplectf.com", "confirm": "password"}

        r = client.patch("/api/v1/users/me", json=data)
        assert r.status_code == 200
        user = Users.query.filter_by(id=2).first()
        assert user.email == "user2@examplectf.com"
        assert verify_password(plaintext="password", ciphertext=user.password)
    destroy_arzi(app)
