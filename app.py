from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'STRINgqUENINGUémsAbe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/CR"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLACHEMY_TRACK_MODIFICATIOS'] = False
from database import db
from flask_migrate import Migrate
from models import Clientes, Reclamacoes
db.init_app(app)
migrate = Migrate(app, db)
from modulos.clientes.clientes import bp_cliente
app.register_blueprint(bp_cliente, url_prefix='/clientes')
from modulos.reclamacoes.reclamacoes import bp_reclamacao
app.register_blueprint(bp_reclamacao, url_prefix='/reclamacoes')

@app.route('/')
def index():
    return render_template("ola.html")


