#!/usr/bin/python
#
#	                            _
#	   ____                    | |
#	  / __ \__      _____  _ __| | __ ____
#	 / / _` \ \ /\ / / _ \| '__| |/ /|_  /
#	| | (_| |\ V  V / (_) | |  |   <  / /
#	 \ \__,_| \_/\_/ \___/|_|  |_|\_\/___|
#	  \____/
#
#			http://www.atworkz.de
#			   info@atworkz.de
#	________________________________________
#	     Screenly OSE Monitoring Add-On
#		      Monitor Output 3.2
#	________________________________________


from flask import Flask, send_file, redirect, url_for

_VERSION='3.2'

app = Flask('__name__')

#app.debug = True # Uncomment to debug
filename = 'output.png'

@app.route('/')
def home():
    return 'Screenly OSE Monitoring Add-on - Monitor Output V' + _VERSION

@app.route('/screen/screenshot.png')
def output():
    _FILE = '/home/pi/soma/monitor-output/tmp/' + filename
    try:
        f = open(_FILE)
        return send_file(_FILE, mimetype='image/png')
    except IOError:
        return send_file('/home/pi/soma/monitor-output/error.png', mimetype='image/png')
    finally:
        f.close()

@app.route('/show')
def show():
    return redirect(url_for('output'))

@app.route('/version')
def version():
    return str(_VERSION)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=9020)
