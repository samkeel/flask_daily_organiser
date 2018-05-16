from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Planner(Base):
    __tablename__ = 'planner'

    planner_id = Column(Integer, primary_key=True)
    # Default=func.now() to set default time
    created = Column(DateTime, default=func.now())
    title = Column(String(), nullable=False)

    @property
    def serialize(self):
        """Return JSON of object"""
        return {
            'planner_id': self.planner_id,
            'created': self.created,
            'title': self.title
        }


engine = create_engine('sqlite:///controller.db')

Base.metadata.create_all(engine)