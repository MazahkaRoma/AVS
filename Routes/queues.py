from flask.blueprints import Blueprint
from flask import render_template
from models.lecturer import Lecturer
import datetime
from flask import request
from models.subject import Subject
from models.interval import Interval
from models.group import Group
from models.schedule import Schedule
from managers.DatabaseManager import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

queues = Blueprint('q', __name__,
                template_folder='templates',
                static_folder='static')

@queues.route("/queues")
def queue():
    return render_template("queues.html", lectors=Lecturer.query.all(), subjects=Subject.query.all(), groups=Group.query.all())
