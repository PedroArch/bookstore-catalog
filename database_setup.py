from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# SQLAlchemy object init
Base = declarative_base()

# Category table
class Category(Base):
    __tablename__ = "category"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }

# Book table
class Book(Base):
    __tablename__ = "book"

    title = Column(String(120), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(2000))
    category = relationship(Category)
    category_id = Column(Integer, ForeignKey('category.id'))

    @property
    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category.name,
        }


# End of File
if __name__ == "__main__":
    # Creating the DB
    engine = create_engine("sqlite:///bookstorecatalog.db")
    Base.metadata.create_all(engine)