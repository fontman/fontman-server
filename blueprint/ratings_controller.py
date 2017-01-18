""" Ratings controller

REST blueprint to manipulate ratings database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from flask import Blueprint, jsonify, request

from service import RatingService

ratings_blueprint = Blueprint('ratings_blueprint', __name__)


@ratings_blueprint.route('/ratings/<entity>/<entity_id>')
def find_ratings_by_element_id(entity, entity_id):
    response_data = []

    try:
        ratings = RatingService().find_by_entity_id(entity, entity_id)

        for rating in ratings:
            response_data.append(
                {
                    "rating_id": rating.rating_id,
                    "comment": rating.comment,
                    "user_id": rating.user_id,
                    "value": rating.value
                }
            )

        return jsonify(ratings)

    except:
        return jsonify({"error": "Invalid request"})


@ratings_blueprint.route('/ratings/new', methods=['POST'])
def add_new_rating():
    request_data = request.json

    try:
        new_rating = RatingService().add_new(
            request_data["comment"],
            request_data["entity"],
            request_data["entity_id"],
            request_data["user_id"],
            request_data["value"]
        )

        return jsonify(
            {
                "rating_id": new_rating.rating_id,
                "entity": new_rating.entity,
                "entity_id": new_rating.entity_id,
                "comment": new_rating.comment,
                "user_id": new_rating.user_id,
                "value": new_rating.value
            }
        )

    except:
        return jsonify({"error": "Error while rating"})


@ratings_blueprint.route('/ratings/<rating_id>/update')
def update_rating_by_rating_id(rating_id):
    request_data = request.json

    try:
        RatingService().update_by_rating_id(
            rating_id,
            {
                "comment": request_data["comment"],
                "value": request_data["value"]
            }
        )
        rating = RatingService().find_by_rating_id(rating_id).one()

        return jsonify(
            {
                "rating_id": rating.rating_id,
                "comment": rating.comment,
                "value": rating.value
            }
        )

    except:
        return jsonify({"error": "Invalid request"})
