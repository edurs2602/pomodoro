import os
import environ
import psycopg2

env = environ.Env()
environ.Env.read_env()

conn = psycopg2.connect(
    host="localhost",
    database=env("DB_DATABASE"),
    user=env("DB_USERNAME"),
    password=env("DB_PASSWORD"),)

cur = conn.cursor()
