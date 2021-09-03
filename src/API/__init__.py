from flask import Flask, app

app = Flask(__name__)

from .Routes import routes