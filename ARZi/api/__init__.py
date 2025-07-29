from flask import Blueprint, current_app
from flask_restx import Api

from ARZi.api.v1.awards import awards_namespace
from ARZi.api.v1.brackets import brackets_namespace
from ARZi.api.v1.challenges import challenges_namespace
from ARZi.api.v1.comments import comments_namespace
from ARZi.api.v1.config import configs_namespace
from ARZi.api.v1.exports import exports_namespace
from ARZi.api.v1.files import files_namespace
from ARZi.api.v1.flags import flags_namespace
from ARZi.api.v1.hints import hints_namespace
from ARZi.api.v1.notifications import notifications_namespace
from ARZi.api.v1.pages import pages_namespace
from ARZi.api.v1.schemas import (
    APIDetailedSuccessResponse,
    APISimpleErrorResponse,
    APISimpleSuccessResponse,
)
from ARZi.api.v1.scoreboard import scoreboard_namespace
from ARZi.api.v1.shares import shares_namespace
from ARZi.api.v1.solutions import solutions_namespace
from ARZi.api.v1.statistics import statistics_namespace
from ARZi.api.v1.submissions import submissions_namespace
from ARZi.api.v1.tags import tags_namespace
from ARZi.api.v1.teams import teams_namespace
from ARZi.api.v1.tokens import tokens_namespace
from ARZi.api.v1.topics import topics_namespace
from ARZi.api.v1.unlocks import unlocks_namespace
from ARZi.api.v1.users import users_namespace

api = Blueprint("api", __name__, url_prefix="/api/v1")
ARZi_API_v1 = Api(
    api,
    version="v1",
    doc=current_app.config.get("SWAGGER_UI_ENDPOINT"),
    authorizations={
        "AccessToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Generate access token in the settings page of your user account.",
        },
    },
    security=["AccessToken"],
)

ARZi_API_v1.schema_model("APISimpleErrorResponse", APISimpleErrorResponse.schema())
ARZi_API_v1.schema_model(
    "APIDetailedSuccessResponse", APIDetailedSuccessResponse.schema()
)
ARZi_API_v1.schema_model("APISimpleSuccessResponse", APISimpleSuccessResponse.schema())

ARZi_API_v1.add_namespace(challenges_namespace, "/challenges")
ARZi_API_v1.add_namespace(tags_namespace, "/tags")
ARZi_API_v1.add_namespace(topics_namespace, "/topics")
ARZi_API_v1.add_namespace(awards_namespace, "/awards")
ARZi_API_v1.add_namespace(hints_namespace, "/hints")
ARZi_API_v1.add_namespace(flags_namespace, "/flags")
ARZi_API_v1.add_namespace(submissions_namespace, "/submissions")
ARZi_API_v1.add_namespace(scoreboard_namespace, "/scoreboard")
ARZi_API_v1.add_namespace(teams_namespace, "/teams")
ARZi_API_v1.add_namespace(users_namespace, "/users")
ARZi_API_v1.add_namespace(statistics_namespace, "/statistics")
ARZi_API_v1.add_namespace(files_namespace, "/files")
ARZi_API_v1.add_namespace(notifications_namespace, "/notifications")
ARZi_API_v1.add_namespace(configs_namespace, "/configs")
ARZi_API_v1.add_namespace(pages_namespace, "/pages")
ARZi_API_v1.add_namespace(unlocks_namespace, "/unlocks")
ARZi_API_v1.add_namespace(tokens_namespace, "/tokens")
ARZi_API_v1.add_namespace(comments_namespace, "/comments")
ARZi_API_v1.add_namespace(shares_namespace, "/shares")
ARZi_API_v1.add_namespace(brackets_namespace, "/brackets")
ARZi_API_v1.add_namespace(exports_namespace, "/exports")
ARZi_API_v1.add_namespace(solutions_namespace, "/solutions")
