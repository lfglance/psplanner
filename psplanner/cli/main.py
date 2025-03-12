import click
from quart import Blueprint

from psplanner.models import *
from psplanner.factory import db


bp = Blueprint("cli", "cli", cli_group=None)


@bp.cli.command("generate", with_appcontext=True)
def generate():
    u = User(
        email="lance@acme.com"
    )
    db.session.add(u)
    db.session.commit()
    p = Project(
        name="ACME Corp Heroku Migration Q2 2025",
        description="Cloud migration. Postgres DMS to Aurora, Rails app to ECS Fargate, CI pipeline implementation.",
        funding_program="MAP Mobilize",
        funding_amount="200000",
        user_id=u.id
    )
    db.session.add(p)
    db.session.commit()
    csa = ProjectRole(
        title="Cloud Solutions Architect",
        description="Technical project oversight, thought leadership, design, consulting and advisory",
        hourly_rate=325,
        currency="USD",
        project_id=p.id
    )
    ce = ProjectRole(
        title="Cloud Engineer",
        description="Project delivery, IaC development, CI/CD pipeline implementation, cloud deployment",
        hourly_rate=235,
        currency="USD",
        project_id=p.id
    )
    de = ProjectRole(
        title="Data Engineer",
        description="Postgres migration support, data validation",
        hourly_rate=235,
        currency="USD",
        project_id=p.id
    )
    pm = ProjectRole(
        title="Project Manager",
        description="Administrative project oversight, customer success",
        hourly_rate=235,
        currency="USD",
        project_id=p.id
    )
    m1 = Milestone(
        title="Discovery and Design",
        description="Getting access to systems/platforms, documenting the migration and cutover path",
        start_week=1,
        duration=2,
        project_id=p.id
    )
    m2 = Milestone(
        title="Infrastructure-as-Code",
        description="Develop the required Terraform templates and modules in order to deploy the needed cloud infrastructure, start deploying foundational infra",
        start_week=3,
        duration=4,
        project_id=p.id
    )
    m3 = Milestone(
        title="Database Replication",
        description="Establish replication/WAL forwarding for the Postgres DB into new Aurora db",
        start_week=5,
        duration=3,
        project_id=p.id
    )
    m4 = Milestone(
        title="Application Infrastructure + CI",
        description="Provision compute infrastructure to host the Rails application, develop CI pipelines for release automation",
        start_week=5,
        duration=3,
        project_id=p.id
    )
    m5 = Milestone(
        title="Testing and Validation",
        description="Go through all environments and fully test and validate the data integrity and full application functionality",
        start_week=8,
        duration=2,
        project_id=p.id
    )
    m6 = Milestone(
        title="Cutover",
        description="Document the cutover plan and perform it for each environment, ending with production; make the AWS infrastructure fully live and accepting traffic",
        start_week=10,
        duration=5,
        project_id=p.id
    )
    objs = [csa, ce, de, pm, m1, m2, m3, m4, m5, m6]
    for obj in objs:
        db.session.add(obj)
        db.session.commit()
    # Task
    # AcceptanceCriterion
    # Assumption
    click.echo(p.id)

