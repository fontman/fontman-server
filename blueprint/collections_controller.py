""" collections controller

REST blueprint to manipulate collections database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from flask import Blueprint, jsonify, request

from service import CollectionService

collections_blueprint = Blueprint('collections_blueprint', __name__)


@collections_blueprint.route('/collections')
def find_all_collections():
    response_data = []

    for collection_id in CollectionService().find_all():
        response_data.append(collection_id[0])

    return jsonify(response_data)


@collections_blueprint.route('/collections/<collection_id>')
def find_collection_by_collection_id(collection_id):
    collection = CollectionService().find_by_collection_id(collection_id).one()
    response_data = (
        {
            "collection_id": collection.collection_id,
            "name": collection.name,
            "team_id": collection.team_id,
            "type": collection>type
        }
    )

    return jsonify(response_data)


@collections_blueprint.route('/collections/')
def find_collections_by_request_parameter():
    response_data = []
    error1, error2 = False, False

    try:
        query_string = request.args.get('team_id')
        collections = CollectionService().find_by_team_id(query_string)
        for collection in collections:
            response_data.append(
                {
                    "collection_id": collection.collection_id,
                    "name": collection.collection_id,
                    "type": collection.type,
                    "team_id": collection.team_id}
            )

    except:
        error1 = True

    try:
        query_string = request.args.get('type')
        collections = CollectionService().find_by_type(query_string)
        for collection in collections:
            collection_data = {
                "collection_id": collection.collection_id,
                "name": collection.collection_id,
                "type": collection.type,
                "team_id": collection.team_id
            }

            if collection_data not in response_data:
                response_data.append(collection_data)
            else:
                continue

    except:
        error2 = True

    if error1 and error2:
        return jsonify({"error": "Invalid request"})

    else:
        return jsonify(response_data)


@collections_blueprint.route('/collections/new', methods=['POST'])
def add_new_collection():
    request_data = request.json

    try:
        collection = CollectionService().add_new(
            team_id=request_data["team_id"],
            name=request_data["name"],
            type=request_data["type"]
        )

        return jsonify(
            {
                "collection_id": collection.collection_id,
                "name": collection.name,
                "team_id": collection.team_id,
                "type": collection.type,
            }
        )

    except:
        return jsonify({"error": "Error while creating collection"})


@collections_blueprint.route(
    '/collections/<collection_id>/delete', methods=['POST']
)
def delete_collection_by_collection_id(collection_id):
    request_data = request.json

    try:
        CollectionService().delete_by_collection_id(collection_id)
        return jsonify(True)

    except:
        return jsonify({"error": "Invalid request"})


@collections_blueprint.route(
    '/collections/<collection_id>/update', methods=['POST']
)
def update_collection_by_collection_id(collection_id):
    request_data = request.json

    try:
        CollectionService().update_by_collection_id(
            collection_id,
            {"name": request_data["name"], "type": request_data["type"]}
        )
        collection = CollectionService().find_by_collection_id(
            collection_id
        ).one()

        return jsonify(
            {
                "collection_id": collection.collection_id,
                "name": collection.name,
                "type": collection.type
            }
        )

    except:
        return jsonify({"error": "Invalid request"})
