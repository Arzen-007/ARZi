from ARZi.models import Brackets, ma


class BracketSchema(ma.ModelSchema):
    class Meta:
        model = Brackets
        include_fk = True
        dump_only = ("id",)
