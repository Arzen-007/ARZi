#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ARZi.models import Comments
from tests.helpers import (
    create_arzi,
    destroy_arzi,
    gen_challenge,
    gen_comment,
    login_as_user,
    register_user,
)


def test_api_post_comments():
    app = create_arzi()
    with app.app_context():
        gen_challenge(app.db)
        with login_as_user(app, "admin") as admin:
            r = admin.post(
                "/api/v1/comments",
                json={
                    "content": "this is a challenge comment",
                    "type": "challenge",
                    "challenge_id": 1,
                },
            )
            # Check that POST response has comment data
            assert r.status_code == 200
            resp = r.get_json()
            assert resp["data"]["content"] == "this is a challenge comment"
            assert "this is a challenge comment" in resp["data"]["html"]
            assert resp["data"]["type"] == "challenge"

            # Check that the comment shows up in the list of comments for the given challenge
            r = admin.get("/api/v1/comments?challenge_id=1", json="")
            assert r.status_code == 200
            resp = r.get_json()
            assert resp["data"][0]["content"] == "this is a challenge comment"
            assert "this is a challenge comment" in resp["data"][0]["html"]
            assert resp["data"][0]["type"] == "challenge"
    destroy_arzi(app)


def test_api_post_comments_with_invalid_author_id():
    app = create_arzi()
    with app.app_context():
        gen_challenge(app.db)
        register_user(app)
        with login_as_user(app, "admin") as admin:
            r = admin.post(
                "/api/v1/comments",
                json={
                    "content": "this is a challenge comment",
                    "type": "challenge",
                    "challenge_id": 1,
                    "author_id": 2,
                },
            )
            # Check that POST response has comment data
            assert r.status_code == 200
            resp = r.get_json()
            assert resp["data"]["author_id"] == 1
    destroy_arzi(app)


def test_api_get_comments():
    app = create_arzi()
    with app.app_context():
        gen_challenge(app.db)
        with login_as_user(app, "admin") as admin:
            gen_comment(
                app.db,
                content="this is a challenge comment",
                author_id=1,
                challenge_id=1,
            )
            r = admin.get("/api/v1/comments", json="")

            # Check that the comment shows up in the list of all comments
            assert r.status_code == 200
            resp = r.get_json()
            assert resp["data"][0]["content"] == "this is a challenge comment"
            assert "this is a challenge comment" in resp["data"][0]["html"]
            assert resp["data"][0]["type"] == "challenge"
    destroy_arzi(app)


def test_api_delete_comments():
    app = create_arzi()
    with app.app_context():
        gen_challenge(app.db)
        with login_as_user(app, "admin") as admin:
            gen_comment(
                app.db,
                content="this is a challenge comment",
                author_id=1,
                challenge_id=1,
            )
            assert Comments.query.count() == 1

            # Check that the comment can be deleted
            r = admin.delete("/api/v1/comments/1", json="")
            assert r.status_code == 200
            resp = r.get_json()
            assert Comments.query.count() == 0
            assert resp["success"] is True
    destroy_arzi(app)
