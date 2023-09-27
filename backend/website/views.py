from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    pass
    return render_template('home.html')

@views.route('/feminino')
def feminino():
    return render_template('feminino.html')


@views.route('/masculino')
def masculino():
    return render_template('masculino.html')

@views.route('/compra')
def compra():
    return render_template('compra.html')

@views.route('/desconto')
def desconto():
    return render_template('desconto.html')