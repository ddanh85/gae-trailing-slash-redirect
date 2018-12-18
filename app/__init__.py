from flask import Flask, abort
app = Flask(__name__)

@app.route('/<path:path>/')
def redirect(path):
    # will never reach this code, as /path/ is intercepted at app.yaml
    abort(404)