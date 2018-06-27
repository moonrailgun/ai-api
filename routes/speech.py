# -*- coding: utf-8 -*-
from flask import request, jsonify, send_file
from flask.blueprints import Blueprint
from ai_clients import speech_client
import io
import hashlib

speech = Blueprint('speech', __name__)

@speech.route('/synthesis', methods=['get'])
def speech_synthesis():
    name = request.args.get('name')
    tex = request.args.get('tex', '')
    cuid = request.args.get('cuid') #用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
    spd = request.args.get('spd', 5) #语速
    pit = request.args.get('pit', 5) #音调
    vol = request.args.get('vol', 5) #音量
    per = request.args.get('per', 0) #发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫

    if not tex:
        return jsonify({
            'result': False,
            'msg': u'缺少合成文本',
        })

    result = speech_client.synthesis(tex, 'zh', 1, {
        'cuid': cuid,
        'spd': spd,
        'pit': pit,
        'vol': vol,
        'per': per,
    })

    if not isinstance(result, dict):
        return send_file(io.BytesIO(result), attachment_filename=(name or hashlib.md5(result).hexdigest()) + '.mp3')
    else:
        return jsonify({
            'result': False,
            'msg': u'合成失败',
            'data': result
        })
