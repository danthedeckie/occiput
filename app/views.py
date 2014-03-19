'''
    The views (routes) that we're using.


'''

from flask import render_template, jsonify, safe_join, json
from os.path import join as pathjoin
from subprocess import check_output
from ConfigParser import RawConfigParser
from app import app

import simplegcache

DASH_INI = RawConfigParser()
DASH_INI.read('dash.ini')

# Here, as we are displaying views, we may not care what the error is,
# but simply want to wrap it in a sane way:
# pylint: disable=bare-except, broad-except
# pylint: disable= no-member

def runscript(scriptname):
    ''' run a script, and return the result as a dict, which can then be sent
        as JSON to the client. '''

    if not scriptname in DASH_INI.sections():
        return jsonify({"error": "Unknown scriptname!"})

    try:
        script = safe_join(app.config['SCRIPTPATH'],
                           pathjoin(DASH_INI.get(scriptname, 'script'),
                                    'dashboard'))

        try:
            args = DASH_INI.get(scriptname, 'args').split()
        except:
            args = []

        output = check_output([script] + args)

    except Exception as excp:
        return {"error": str(excp), "data": str(excp)}

    # either this *is* proper JSON with a data block, or else
    # we'll send it as text.
    try:
        data = json.parse(output)
        if not 'data' in data:
            raise KeyError('missing data!')
        return data
    except:
        return {"data": output}


################################################################################
#
# The actual views:
#

@app.route('/')
@app.route('/index.html')
def index():
    ''' the main dashboard view (very simple) '''
    return render_template('dashboard.html', dash=DASH_INI)


@app.route('/script/<scriptname>')
def script_get(scriptname):
    ''' get a result from the cache, or if that's exired, then run the script
        for a new value '''

    result = simplegcache.get(scriptname, lambda: runscript(scriptname), 10)
    return jsonify(result)
