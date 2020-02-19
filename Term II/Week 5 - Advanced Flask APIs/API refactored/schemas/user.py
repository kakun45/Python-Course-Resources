from ma import marsh
from models.user import UserModel


class UserSchema(marsh.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
