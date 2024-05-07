from flask import Blueprint, jsonify
from funcoes import mostrar_lista, contador_de_idade, counter_salario, tres_maiores_salarios, calcular_media_salarios, imprimir_media, intervalo_de_idade
from random_data import pessoas

bp = Blueprint("api", __name__)

# @bp.route("/api/index", methods = ["GET"])
# def index():
#     mostrar_pessoas = mostrar_lista(pessoas)
#     return jsonify({"Status":200, "Pessoas":mostrar_pessoas})

@bp.route("/api/idades", methods = ["GET"])
def idades():
    idades_maior_50 = contador_de_idade(pessoas)
    return jsonify({"Status":200, "Pessoas com mais de 50 anos":idades_maior_50})

@bp.route("/api/salarios", methods = ["GET"])
def salarios():
    counter_salarios = counter_salario(pessoas)
    contador_percent = counter_salarios[0]
    total_percent = counter_salarios[1]
    contador_total = counter_salarios[2]
    return jsonify({"Status":200, "Salario maior que 2000": contador_percent, 
                    "Total de pessoas":contador_total, 
                    "porcentagem":total_percent })

@bp.route("/api/maiores_salarios", methods = ["GET"])
def maioresSalarios():
    maiores_salarios = tres_maiores_salarios(pessoas)
    return jsonify({"Status":200, "Três maiores salarios": maiores_salarios})

@bp.route("/api/media_salarios", methods = ["GET"])
def calcular_media_de_salarios():
    media_salarios = calcular_media_salarios(pessoas)
    return jsonify({"Status":200, "Media de salários":media_salarios})

@bp.route("/api/medias", methods = ["GET"])
def medias():
    medias = imprimir_media(pessoas)
    return jsonify({"Status":200, "Media de salários":medias})

@bp.route("/api/intervalo_de_idade/<string:sexo>", methods = ["GET"])
def intervalo_idade(sexo:str):
    intervalos_de_idades = intervalo_de_idade(pessoas)
    idade_media = intervalos_de_idades[0]
    sexo_frequente = intervalos_de_idades[1]
    sexo_menos_frequente = intervalos_de_idades[2]
    if sexo == "f":
        return jsonify({"Status":200,"Sexo menos frequente": sexo_menos_frequente})
    elif sexo == "m":
        return jsonify({"Status":200, "idades media": idade_media, "sexo frequente": sexo_frequente, "Sexo menos frequente": sexo_menos_frequente})
