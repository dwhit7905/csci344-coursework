from models import User
import flask_jwt_extended
from flask import Response, request
from flask_restful import Resource
import json
from datetime import timezone, datetime, timedelta


class AccessTokenEndpoint(Resource):

    # Create a route to authenticate your users and return JWT Token. The
    # create_access_token() function is used to actually generate the JWT.
    def post(self):
        body = request.get_json() or {}
        username = body.get("username")
        password = body.get("password")
        print(username, password)

        # Your code here to set the access / refresh token...



        # Modify the response to give the user their credentials:
        return Response(
            json.dumps(
                {
                    "access_token": "?????",
                    "refresh_token": "?????",
                }
            ),
            mimetype="application/json",
            status=200,
        )


class RefreshTokenEndpoint(Resource):

    def post(self):
        # Done for you! You're welcome!
        body = request.get_json() or {}
        refresh_token = body.get("refresh_token")
        if not refresh_token:
            return Response(
                json.dumps({"message": "missing refresh_token"}),
                mimetype="application/json",
                status=400,
            )
        try:
            decoded_token = flask_jwt_extended.decode_token(refresh_token)
            exp_timestamp = decoded_token.get("exp")
            now = datetime.timestamp(datetime.now(timezone.utc))
        except:
            return Response(
                json.dumps(
                    {
                        "message": "Invalid refresh_token={0}. Could not decode.".format(
                            refresh_token
                        )
                    }
                ),
                mimetype="application/json",
                status=400,
            )

        # if the refresh token is valid and hasn't expired, issue a
        # new access token:
        if exp_timestamp > now:
            identity = decoded_token.get("sub")
            access_token = flask_jwt_extended.create_access_token(
                identity=identity
            )
            return Response(
                json.dumps(
                    {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    }
                ),
                mimetype="application/json",
                status=200,
            )
        else:
            return Response(
                json.dumps({"message": "refresh_token has expired"}),
                mimetype="application/json",
                status=401,
            )


def initialize_routes(api):
    api.add_resource(AccessTokenEndpoint, "/api/token", "/api/token/")

    api.add_resource(
        RefreshTokenEndpoint, "/api/token/refresh", "/api/token/refresh/"
    )
