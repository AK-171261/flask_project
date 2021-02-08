from flask_restful import Resource
from logging import info


class TaskByid(Resource):
    def get(self, task_id):
        info("Inside  get method")
        return {"message": "inside Get task_id:{}".format(task_id)}, 200

    def post(self, task_id):
        info("Inside  post method")
        return {"message": "inside post task_id:{}".format(task_id)}, 200

    def put(self, task_id):
        info("Inside  put method")
        return {"message": "inside put task_id:{}".format(task_id)}, 200

    def delete(self, task_id):
        info("Inside  delete method")
        return {"message": "inside delete task_id:{}".format(task_id)}, 200
