from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   jsonify,
                   url_for,
                   flash,
                   make_response)

from sqlalchemy import create_engine, asc, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, UploadFile, User, Category, Project

# NEW IMPORTS FOR AUTHENTICATION
from flask import session as login_session
import random
import string
from datetime import datetime
import os

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField
from wtforms.validators import InputRequired
from functools import wraps

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

engine = create_engine('sqlite:///yearn.db')
Base.metadata.bind = engine

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())[
    'web']['client_id']


# # **************************************************************************
# # SHOW DASHBOARD: User Dashboard - companies, projects, tasks
# # **************************************************************************
#
#
@app.route('/')
@app.route('/dashboard')
def showDashboard():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    companies = session.query(tblOrg).filter_by(
        orgType='CUSTOMER').all()
    recentProjects = session.query(tblProject).outerjoin(
        Category).outerjoin(User).order_by(Project.DateAdd.desc()).limit(6)
#     if 'username' not in login_session:
#         # prevent unauthorized users from adding new categories
#         return render_template('publiccategories.html', categories=categories,
#                                recentProjects=recentProjects)
#     else:
#         return render_template('categories.html', categories=categories,
#                                recentProjects=recentProjects)


# **************************************************************************
# SHOW USERS: Display All Registered Users
# **************************************************************************
@app.route('/users')
def showUsers():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

# **************************************************************************
# ADD USER: Add New User
# **************************************************************************


@app.route('/newuser')
def newUser():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# EDIT USER: Edit Existing User
# **************************************************************************


@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST']')
def editUser(user_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
# **************************************************************************
# DELETE USER: Delete an Existing User
# **************************************************************************


@app.route('/users/<int:user_id>/delete', methods=['GET', 'POST']')
def deleteUser(user_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# SHOW COMPANIES: Display All Companies
# **************************************************************************
@app.route('/companies')
def showOrgs():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# SHOW ONE COMPANY: Display ONE Company
# **************************************************************************
@app.route('/companies/<int:org_id>')
def showOneOrg(org_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    company = session.query(tblOrg).filter_by(orgID=org_id).one()
    projects = session.query(
        tblProjects).filter_by(orgID=org_id).all()


# **************************************************************************
# ADD COMPANY: Add New Company
# **************************************************************************


@app.route('/newcompany')
def newOrg():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# EDIT COMPANY: Edit Existing Company
# **************************************************************************


@app.route('/companies/<int:org_id>/edit', methods=['GET', 'POST']')
def editOrg(org_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
# **************************************************************************
# DELETE COMPANY: Delete an Existing Company
# **************************************************************************


@app.route('/companies/<int:org_id>/delete', methods=['GET', 'POST']')
def deleteOrg(org_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# SHOW ONE PROJECT: Display ONE Project
# **************************************************************************
@app.route('/companies/<int:org_id>/projects/<int:project_id>')
def showOneProject(org_id, project_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    company = session.query(tblOrg).filter_by(orgID=org_id).one()
    project = session.query(tblProject).filter_by(
        projectID=project_id).one()


# **************************************************************************
# ADD PROJECT: Add New Project
# **************************************************************************
@app.route('/newproject')
def newProject(org_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# EDIT Project: Edit Existing Project
# **************************************************************************
@app.route('/companies/<int:org_id>/projects/<int:project_id>/edit',
           methods=['GET', 'POST']')
def editProject():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
# **************************************************************************
# DELETE PROJECT: Delete an Existing Project
# **************************************************************************


@app.route('/companies/<int:org_id>/projects/<int:project_id>/edit',
           methods=['GET', 'POST']')
def deleteUser():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# SHOW ONE TASK: Display ONE Task
# **************************************************************************
@app.route('/companies/<int:org_id>/projects/<int:project_id>/<int:task_id>')
def showOneTask(org_id, project_id, task_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    company = session.query(tblOrg).filter_by(orgID=org_id).one()
    project = session.query(tblProjects).filter_by(orgID=org_id).one()
    task = session.query(tblTasks).filter_by(taskID=task_id).one()


# **************************************************************************
# ADD TASK: Add New Task
# **************************************************************************
@app.route('/newtask')
def newTask(org_id, project_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

# **************************************************************************
# EDIT TASK: Edit Existing Task
# **************************************************************************


@app.route('/companies/<int:org_id>/<int:project_id>/<int:task_id>/edit',
           methods=['GET', 'POST']')
def editTask(org_id, project_id, task_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
# **************************************************************************
# DELETE TASK: Delete an Existing Task
# **************************************************************************


@app.route('/companies/<int:org_id>/<int:project_id>/<int:task_id>/delete',
           methods=['GET', 'POST']')
def deleteTask(org_id, project_id, task_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# SHOW ONE TIME ENTRY: Display ONE Time Entry
# **************************************************************************


@app.route('/companies/<int:org_id>/projects/<int:project_id>/<int:task_id>/<int:time_id>')
def showOneTimeEntry(org_id, project_id, task_id, time_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # company = session.query(tblOrg).filter_by(orgID=org_id).one()
    # project = session.query(tblProjects).filter_by(orgID=org_id).one()
    # task = session.query(tblTasks).filter_by(taskID=task_id).one()


# **************************************************************************
# ADD TIME ENTRY: Add New Time Entry
# **************************************************************************
@app.route('/newtimeentry')
def newTimeEntry(org_id, project_id, task_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

# **************************************************************************
# EDIT TIME ENTRY: Edit Existing Time Entry
# **************************************************************************


@app.route('/companies/<int:org_id>/<int:project_id>/<int:task_id>/<int:time_id>/edit',
           methods=['GET', 'POST']')
def editTimeEntry(org_id, project_id, task_id, time_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
# **************************************************************************
# DELETE TIME ENTRY: Delete an Existing Time Entry
# **************************************************************************


@app.route('/companies/<int:org_id>/<int:project_id>/<int:task_id>/<int:time_id>/delete',
           methods=['GET', 'POST']')
def deleteTimeEntry(org_id, project_id, task_id, time_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()


# **************************************************************************
# JSON API Endpoints:
# **************************************************************************

# JSON Endpoint to view All Company data
# **************************************************************************


@app.route('/companies/JSON')
def companiesJSON():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    companies = session.query(tblOrg).all()
    return jsonify(Companies=[c.serialize for c in companies])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
