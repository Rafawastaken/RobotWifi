from flask import Blueprint
from flask_restful import Resource, reqparse, abort, marshal_with, fields
from .models import RobotModel
from server import db

# Blueprint
api_bp = Blueprint('api', __name__)

# Resource add command
robot_args = reqparse.RequestParser()
robot_args.add_argument('nome', type=str, help="Nome do comando")
robot_args.add_argument('estado', type = bool, help = "Estado do comando")

robot_resource_fields = {
    "nome":fields.String,
    "estado":fields.Boolean
}


class ComunicarRobot(Resource):
    def get(self):
        comandos = RobotModel.query.all()
        resp = []

        for comando in comandos:
            nome = comando.nome
            estado = comando.estado

            if estado == 0: estado = False
            if estado == 1: estado = True

            resp.append({"nome":nome, "estado":estado})

        return resp, 200

    @marshal_with(robot_resource_fields)
    def post(self):
        args = robot_args.parse_args()
        nome = args['nome']
        estado = args['estado']

        new_commando = RobotModel(
            nome = nome,
            estado = estado
            )
        
        db.session.add(new_commando)
        db.session.commit()

        return new_commando, 200

    @marshal_with(robot_resource_fields)
    def patch(self):
        args = robot_args.parse_args()

        comando = RobotModel.query.filter_by(nome = args['nome']).first()
        comandos = RobotModel.query.all()

        for com in comandos: com.estado = 0
        comando.estado = 1

        db.session.commit()

        return comandos, 200
