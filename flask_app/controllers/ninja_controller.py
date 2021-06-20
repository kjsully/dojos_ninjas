from flask import render_template, request, session, redirect

from flask_app import app
from ..models.dojo import Dojo
from ..models.ninja import Ninja


@app.route('/ninja/new')
def new_ninja_form():
    return render_template('new_ninja.html', all_dojos = Dojo.get_all_dojos())


@app.route('/ninja/create', methods = ['POST'])
def create_ninja():
    Ninja.create(request.form)

    return redirect('/')