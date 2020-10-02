from sqlalchemy import inspect

from database import db

# Base data model for all objects
class BaseModel(db.Model):
  __abstract__ = True

  def __init__(self, *args):
    super().__init__(*args)

  def __repr__(self):
    return '%s(%s)' % (self.__class__.__name__, {
      column: value
      for column, value in self.as_dict().items()
    })

  def as_dict(self):
    return {
      c.key: getattr(self, c.key)
      for c in inspect(self).mapper.column_attrs
    }