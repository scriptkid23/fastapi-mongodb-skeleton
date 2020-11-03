from .RWModel import RWModel
class RWSchema(RWModel):
    class Config(RWModel.Config):
        orm_mode = True
        