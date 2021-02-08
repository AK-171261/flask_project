from flask_restful import Resource
from logging import info


class Task(Resource):
    def get(self):
        info("Inside  get method")
        return {"message": "inside Get"}, 200

    def post(self):
        info("Inside  post method")
        return {"message": "inside post"}, 200

    def put(self):
        info("Inside  put method")
        return {"message": "inside put"}, 200

    def delete(self):
        info("Inside  delete method")
        return {"message": "inside delete"}, 200
