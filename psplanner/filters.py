from urllib.parse import urlencode
from decimal import Decimal

from quart import Blueprint
from arrow import get as arrow_get

from psplanner.models import User
from psplanner.helpers import generate_avatar


bp = Blueprint('filters', 'filters')


@bp.app_template_filter('get_avatar')
def get_avatar(handle):
    return f'data:image/png;base64,{generate_avatar(96, handle)}'

@bp.app_template_filter('humanize')
def humanize(d):
    if not d:
        return 'never'
    return arrow_get(d).humanize()

@bp.app_template_filter('show_user')
def show_user(s):
    _u = User.query.filter(User.id == s).first()
    if not _u:
        return None
    else:
        return _u.username

@bp.app_template_filter('as_formatted')
def as_formatted(s):
    return arrow_get(int(s)).format('YYYY-MM-DD')

@bp.app_template_filter("fix_args")
def trim_arg(all_args):
    d = all_args.to_dict()
    if d:
        return '?' + urlencode(d)
    else:
        return ''
