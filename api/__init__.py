from flask_restful import Api
from app import flaskAppInstance
from .Task import Task
from .taskById import TaskByid

restServer = Api(flaskAppInstance)
restServer.add_resource(Task, '/api/v1.0/task')
restServer.add_resource(TaskByid, '/api/v1.0/taskByid/id/<string:task_id>')
