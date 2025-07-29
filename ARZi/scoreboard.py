from flask import Blueprint, render_template

from ARZi.utils import config
from ARZi.utils.config.visibility import scores_visible
from ARZi.utils.decorators.visibility import (
    check_account_visibility,
    check_score_visibility,
)
from ARZi.utils.helpers import get_infos
from ARZi.utils.scores import get_standings
from ARZi.utils.user import is_admin

scoreboard = Blueprint("scoreboard", __name__)


@scoreboard.route("/scoreboard")
@check_account_visibility
@check_score_visibility
def listing():
    infos = get_infos()

    if config.is_scoreboard_frozen():
        infos.append("Scoreboard has been frozen")

    if is_admin() is True and scores_visible() is False:
        infos.append("Scores are not currently visible to users")

    standings = get_standings()
    return render_template("scoreboard.html", standings=standings, infos=infos)
