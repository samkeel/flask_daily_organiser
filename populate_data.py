from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Planner

engine = create_engine('sqlite:///controller.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

event1 = Planner(title="one")
session.add(event1)
session.commit()
