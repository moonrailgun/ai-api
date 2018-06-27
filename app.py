# -*- coding: utf-8 -*-
import sys
from flask import Flask, request, jsonify
import json
import requests
from routes.ocr import ocr
from routes.speech import speech

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.register_blueprint(ocr, url_prefix='/api/ocr')
app.register_blueprint(speech, url_prefix='/api/speech')

@app.errorhandler(404)
def no_found(error):
    return jsonify({
        'result': False,
        'msg': u'请求地址不存在'
    }), 404

@app.errorhandler(Exception)
@app.errorhandler(500)
def error(error):
    print '======error======'
    print error
    print '================='
    return jsonify({
        'result': False,
        'msg': u'系统忙'
    }), 500

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 4233,
        debug = True,
        threaded=True
    )
