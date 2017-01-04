""" Teams controller

REST blueprint to do team management.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from flask import Blueprint, jsonify, request

from service import TeamService

teams_blueprint = Blueprint('teams_blueprint', __name__)


@teams_blueprint.route('/teams')
def find_all_teams():
    response_data = []

    for team in TeamService().find_all():
        response_data.append(
            {
                "team_id": team.team_id,
                "name": team.name,
                "type": team.type
            }
        )

    return jsonify(response_data)


@teams_blueprint.route('/teams/<team_id>')
def find_team_by_team_id(team_id):
    try:
        team = TeamService().find_by_team_id(team_id).one()

        return jsonify(
            {
                "team_id": team.team_id,
                "name": team.name,
                "type": team.type
            }
        )

    except:
        return jsonify({"error": "Invalid request"})


@teams_blueprint.route('/teams/')
def find_teams_by_request_parameter():
    response_data = []

    try:
        query_string = request.args.get('type')

        for team in TeamService().find_by_type(query_string):
            response_data.append(
                {
                    "team_id": team.team_id,
                    "name": team.name,
                    "type": team.type
                }
            )

        return jsonify(query_string)

    except:
        return jsonify({"error": "Invalid request"})


@teams_blueprint.route('/teams/new', methods=['POST'])
def add_new_team():
    request_data = request.json

    try:
        new_team = TeamService().add_new(
            request_data["name"],
            request_data["type"]
        )

        return jsonify(
            {
                "team_id": new_team.team_id,
                "name": new_team.name,
                "type": new_team.type
            }
        )

    except:
        return jsonify({"error": "Error while creating team"})


@teams_blueprint.route('/teams/<team_id>/delete', methods=['POST'])
def delete_team_by_team_id(team_id):
    request_data = request.json

    try:
        TeamService().delete_by_team_id(team_id)
        return jsonify(True)

    except:
        return jsonify({"error": "Invalid request"})


@teams_blueprint.route('/teams/<team_id>/update', methods=['POST'])
def update_team_by_team_id(team_id):
    request_data = request.json

    try:
        TeamService().update_by_team_id(
            team_id,
            {
                "name": request_data["name"],
                "type": request_data["type"]
            }
        )
        team = TeamService().find_by_type(team_id)

        return jsonify(
            {
                "name": team.name,
                "type": team.type
            }
        )

    except:
        return jsonify({"error": "Invalid request"})
