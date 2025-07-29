from flask_restx import Resource

from ARZi.api.v1.statistics import statistics_namespace
from ARZi.models import Teams
from ARZi.utils.decorators import admins_only


@statistics_namespace.route("/teams")
class TeamStatistics(Resource):
    @admins_only
    def get(self):
        registered = Teams.query.count()
        data = {"registered": registered}
        return {"success": True, "data": data}
