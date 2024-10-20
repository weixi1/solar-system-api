from flask import Blueprint, abort, make_response
from .models.planet import planets

solar_system_bp = Blueprint("solar_system_bp", __name__, url_prefix="/solar-system")

@solar_system_bp.get("")
def get_all_list():
    results_list = []
    for planet in planets:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            flag=planet.flag
        ))

    return results_list

@solar_system_bp.get("/planets/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return{
        "id":planet.id,
        "name":planet.name,
        "description":planet.description,
        "flag":planet.flag
    }
        
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))