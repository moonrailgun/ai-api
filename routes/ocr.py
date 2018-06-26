# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask.blueprints import Blueprint
from ai_clients import ocr_client
import base64

ocr = Blueprint('ocr', __name__)

@ocr.route('/general/url', methods=['post'])
def general_url():
    data = request.get_json()
    url = data.get('url')
    language_type = data.get('language_type', 'CHN_ENG')
    detect_direction = data.get('detect_direction', False)
    detect_language = data.get('detect_language', False)
    probability = data.get('probability', False)

    if not url:
        return jsonify({
            'result': False,
            'msg': u'缺少url',
        })

    res = ocr_client.basicGeneralUrl(url, {
        'language_type': language_type,
        'detect_direction': detect_direction,
        'detect_language': detect_language,
        'probability': probability,
    })

    return jsonify({
        'result': True,
        'data': res,
    })

@ocr.route('/general/base64', methods=['post'])
def general_base64():
    data = request.get_json()
    base64str = data.get('base64')
    language_type = data.get('language_type', 'CHN_ENG')
    detect_direction = data.get('detect_direction', False)
    detect_language = data.get('detect_language', False)
    probability = data.get('probability', False)

    if not base64str:
        return jsonify({
            'result': False,
            'msg': u'缺少base64',
        })
    image = base64.b64decode(base64str) # 将base64解码

    res = ocr_client.basicGeneral(image, {
        'language_type': language_type,
        'detect_direction': detect_direction,
        'detect_language': detect_language,
        'probability': probability,
    })

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })
