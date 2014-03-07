from flask import render_template, url_for, request, jsonify, safe_join, json
from subprocess import check_output
from ConfigParser import RawConfigParser
from app import app

@app.route('/')
@app.route('/index.html')
def index():
    dash = RawConfigParser()
    dash.read('dash.ini')

    return render_template('dashboard.html', dash=dash)

@app.route('/script/<scriptname>')
def script_get(scriptname):
    dash = RawConfigParser()
    dash.read('dash.ini')

    if not scriptname in dash.sections():
       return jsonify({"error": "Unknown scriptname!"})

    script = safe_join(app.config['SCRIPTPATH'], scriptname)
    print script
    output = check_output(script)

    try:
        data = json.parse(output)
        check = data['data']
        return jsonify(data)
    except:
        return jsonify({"data": output})
