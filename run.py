#!.virtualenv/bin/python
# -*- coding: utf-8 -*-
'''
    The main 'run' start script for the server.
'''

import sys
reload(sys)
sys.setdefaultencoading('utf-8') #pylint: disable=no-member

from app import app

def main(which_server='dev'):
    '''
        Run the appropraite server (either gevent or dev)
    '''
    if which_server == 'gevent':
        import gevent.monkey

        gevent.monkey.patch_all()
        gevent.monkey.patch_subprocess()

        from gevent.wsgi import WSGIServer

        server = WSGIServer(('', 5000), app)
        server.serve_forever()

    else:
        app.run(debug=True)

if __name__ == '__main__':
    ARGS = sys.argv
    ARGS.pop()
    main(*ARGS) # pylint: disable=star-args
