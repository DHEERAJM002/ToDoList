"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrpu6o2qv2dcb91bnh0-a.oregon-postgres.render.com",
        database="todolist_zs1s",
        user="todolist_zs1s_user",
        password="vxffnyRMLjv5H30jhmFIXp7MrBFqu164")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
