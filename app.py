from flask import (Flask,
                   render_template,
                   jsonify)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base

app = Flask(__name__)

engine = create_engine('sqlite:///controller.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
def showMain():
    return render_template('main.html')

@app.route("/todo")
def showTodo():
    return render_template('todo.html')

@app.route("/planner")
def showPlanner():
    return render_template('planner.html')

@app.route("/kb")
def showKnowledgebase():
    return render_template('kb.html')

if __name__ == '__main__':
  app.run(port=5000, debug=True)