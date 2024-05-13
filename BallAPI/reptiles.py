from flask import (Blueprint, request)
from . import models

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

@bp.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']

        new_reptile = models.Reptile(
            common_name = common_name,
            scientific_name = scientific_name,
            conservation_status = conservation_status,
            native_habitat = native_habitat,
            fun_fact = fun_fact
        )
        models.db.session.add(new_reptile)
        models.db.session.commit()
        
        return 'Reptile Added Successfully'

    results = models.Reptile.query.all()

    reptile_data = []
    for result in results:
        reptile_dict = {
            'common_name': result.common_name, 
            'scientific_name': result.scientific_name, 
            'conservation_status': result.conservation_status, 
            'native_habitat': result.native_habitat, 
            'fun_fact': result.fun_fact
        }
        reptile_data.append(reptile_dict)

    return reptile_data

@bp.route('/<int:id>')
def show(id):
    reptile = models.Reptile.query.filter_by(id=id).first()
    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific_name': reptile.scientific_name, 
        'conservation_status': reptile.conservation_status, 
        'native_habitat': reptile.native_habitat, 
        'fun_fact': reptile.fun_fact
    }

    return reptile_dict