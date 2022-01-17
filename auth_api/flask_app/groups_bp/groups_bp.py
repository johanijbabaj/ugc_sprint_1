from db_models import Group
from flasgger.utils import swag_from
from flask import Blueprint, render_template
from flask.json import jsonify

groups_bp = Blueprint("groups_bp", __name__)


@swag_from("../schemes/groups_get.yaml")
@groups_bp.route("/", methods=["GET"])
def list_groups():
    """
    Список всех пользовательских групп
    """
    groups = []
    for group in Group.query.all():
        groups.append(group.to_json())
    return jsonify(groups)
