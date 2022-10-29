from flask import (Flask, request, redirect, Blueprint, jsonify)

import json
from . import models

bp = Blueprint("reptiles", __name__, url_prefix="/reptiles")

@bp.route("/", methods=["POST", "GET"])
def index():
   if request.method == "POST":
      return {
      'common_name': request.form["common_name"],
      'scientific_name': request.form["scientific_name"],
      'conservation_status': request.form["conservation_status"],
      'native_habitat': request.form["native_habitat"],
      'fun_fact': request.form["fun_fact"]
      }

   reptiles = models.Reptile.query.all()
   payload = json.dumps(reptiles)
   return [reptile.common_name for reptile in payload]

@bp.route("/<int:id>")
def find_by_id(id):
   reptiles = models.Reptile.query.get(id)
   payload = json.dumps(reptiles)
   # payload = dict(reptiles)
   return [(reptiles.common_name, reptiles.scientific_name, reptiles.conservation_status, reptiles.native_habitat, reptiles.fun_fact) for reptiles in payload]


