#!/usr/bin/env python

"""
- Toggle status codes from 500 to 200, for testing liveness and readiness probes


- requirements
Flask==1.1.1

Run on public ip, so it can be accessed by container
"""

import json
from flask import Flask
app = Flask(__name__)



@app.route('/liveness')
def liveness():
    data = {"msg": "Liveness Check"} 
    return json.dumps(data), 500


@app.route('/readiness')
def readiness():
    data = {"msg": "Readiness Check"} 
    return json.dumps(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
