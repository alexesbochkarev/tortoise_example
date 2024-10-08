from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    
    def upper_name(self) -> str:
        return self.name.upper()
    
    class PydanticMeta:
        computed = ["upper_name"]
