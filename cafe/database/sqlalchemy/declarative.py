from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData


# Useful naming conventions
metadata = MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})


# All base classes inheriting from this will use the same metadata
CafeSQLAlchemyBase = declarative_base(metadata=metadata)


# ensure str() returns id if an id is present, useful for when id is uuid
CafeSQLAlchemyBase.__str__ = lambda self: \
    '{}::{}'.format(self.__class__.__name__, str(self.id)) \
    if hasattr(self, 'id') \
    else super(CafeSQLAlchemyBase, self).__str__()
