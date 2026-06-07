from flask import Flask   # noqa
app = Flask(__name__)   # noqa
import hello_world.views  # noqa
