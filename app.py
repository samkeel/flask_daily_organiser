#! /usr/bin/env python3.5

from flask import (Flask,
                   render_template,
                   jsonify,
                   request,
                   redirect)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Base, Planner
import httplib2

app = Flask(__name__)

engine = create_engine('sqlite:///controller.db')
Base.metadata.bind = engine

# Use scoped_session to make requests thread safe
session = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def showMain():
    return render_template('main.html')

@app.route("/todo")
def showTodo():
    return render_template('todo.html')

@app.route("/planner")
def showPlanner():
    arranger = session.query(Planner).all()
    return render_template('planner.html', arranger=arranger)

#JSON parser
@app.route('/planner/JSON')
def plannerJSON():
    plans = session.query(Planner).all()
    return jsonify(Plans=[i.serialize for i in plans])

@app.route("/kb")
def showKnowledgebase():
    return render_template('kb.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)