from quart import Blueprint, render_template

from psplanner.models import Project


bp = Blueprint("main", "main")

@bp.route("/")
async def index():
    return await render_template("main/index.html")

@bp.route("/project/<id>")
async def get_project(id):
    project = Project.query.filter(Project.id == id).first()
    return await render_template("main/project.html", project=project)