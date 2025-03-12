from datetime import datetime, timezone
from random import Random
from uuid import uuid4

from psplanner.factory import db


def get_date():
    return datetime.now(timezone.utc)

def gen_uuid():
    return str(uuid4())


class User(db.Model):
    """
    Users create new projects.
    """
    __tablename__ = "users"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    last_login_date = db.Column(db.DateTime, default=get_date)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.email

class Project(db.Model):
    """
    """
    __tablename__ = "projects"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=False)
    funding_program = db.Column(db.String(100), unique=False, nullable=True)
    funding_amount = db.Column(db.Integer, default=0)
    user_id = db.Column(db.String(200), db.ForeignKey(User.id), nullable=False)
    user = db.relationship("User", backref="projects", foreign_keys=user_id)

    def __repr__(self):
        return self.name

class ProjectRole(db.Model):
    """
    """
    __tablename__ = "project_roles"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    hourly_rate = db.Column(db.Integer, unique=False, nullable=False)
    currency = db.Column(db.String(20), default="USD", unique=False, nullable=False)
    project_id = db.Column(db.String(200), db.ForeignKey(Project.id))
    project = db.relationship("Project", backref="roles", foreign_keys=project_id)

    def __repr__(self):
        return self.id

class Milestone(db.Model):
    """
    """
    __tablename__ = "project_milestones"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    title = db.Column(db.String(200), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    start_week = db.Column(db.Integer, unique=False, nullable=False)
    duration = db.Column(db.Integer, unique=False, nullable=False)
    dependent_milestone_id = db.Column(db.String(200), unique=False, nullable=True)
    project_id = db.Column(db.String(200), db.ForeignKey(Project.id))
    project = db.relationship("Project", backref="milestones", foreign_keys=project_id)

    def __repr__(self):
        return self.id

class Task(db.Model):
    """
    """
    __tablename__ = "project_milestone_tasks"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    title = db.Column(db.String(200), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    hours_estimated = db.Column(db.Integer, unique=False, nullable=False)
    role_id = db.Column(db.String(200), db.ForeignKey(ProjectRole.id))
    role = db.relationship("ProjectRole", backref="tasks", foreign_keys=role_id)
    milestone_id = db.Column(db.String(200), db.ForeignKey(Milestone.id))
    milestone = db.relationship("Milestone", backref="tasks", foreign_keys=milestone_id)

    def __repr__(self):
        return self.id

class AcceptanceCriterion(db.Model):
    """
    """
    __tablename__ = "project_milestone_acceptance_criteria"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    description = db.Column(db.Text, unique=False, nullable=False)
    milestone_id = db.Column(db.String(200), db.ForeignKey(Milestone.id))
    milestone = db.relationship("Milestone", backref="criteria", foreign_keys=milestone_id)

    def __repr__(self):
        return self.id

class Assumption(db.Model):
    """
    """
    __tablename__ = "project_assumptions"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    description = db.Column(db.Text, unique=False, nullable=False)
    milestone_id = db.Column(db.String(200), db.ForeignKey(Milestone.id))
    milestone = db.relationship("Milestone", backref="assumptions", foreign_keys=milestone_id)

    def __repr__(self):
        return self.id
