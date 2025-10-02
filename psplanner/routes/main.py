from quart import Blueprint, render_template, request, redirect, url_for

from psplanner.models import Project, Milestone, Task, AcceptanceCriterion, Assumption, ProjectRole
from psplanner.factory import db


bp = Blueprint("main", "main")

@bp.route("/")
async def index():
    return await render_template("main/index.html")

@bp.route("/project/<id>")
async def get_project(id):
    project = Project.query.filter(Project.id == id).first()
    return await render_template("main/project.html", project=project)

@bp.route("/project/<project_id>/milestone", methods=["POST"])
async def add_milestone(project_id):
    form = await request.form
    
    milestone = Milestone(
        title=form.get("title"),
        description=form.get("description"),
        start_week=int(form.get("start_week")),
        duration=int(form.get("duration")),
        dependent_milestone_id=form.get("dependent_milestone_id") or None,
        project_id=project_id
    )
    
    db.session.add(milestone)
    db.session.commit()
    
    return redirect(url_for("main.get_project", id=project_id))

@bp.route("/task", methods=["POST"])
async def add_task():
    form = await request.form

    milestone = Milestone.query.filter(Milestone.id == form.get("milestone_id")).first()

    task = Task(
        title=form.get("title"),
        description=form.get("description"),
        hours_estimated=int(form.get("hours_estimated")),
        role_id=form.get("role_id"),
        milestone_id=form.get("milestone_id")
    )

    db.session.add(task)
    db.session.commit()

    return redirect(url_for("main.get_project", id=milestone.project_id))

@bp.route("/criterion", methods=["POST"])
async def add_criterion():
    form = await request.form
    
    milestone = Milestone.query.filter(Milestone.id == form.get("milestone_id")).first()
    
    criterion = AcceptanceCriterion(
        description=form.get("description"),
        milestone_id=form.get("milestone_id")
    )
    
    db.session.add(criterion)
    db.session.commit()
    
    return redirect(url_for("main.get_project", id=milestone.project_id))

@bp.route("/assumption", methods=["POST"])
async def add_assumption():
    form = await request.form
    
    milestone = Milestone.query.filter(Milestone.id == form.get("milestone_id")).first()
    
    assumption = Assumption(
        description=form.get("description"),
        milestone_id=form.get("milestone_id")
    )
    
    db.session.add(assumption)
    db.session.commit()
    
    return redirect(url_for("main.get_project", id=milestone.project_id))