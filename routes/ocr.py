# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask.blueprints import Blueprint
from ai_clients import ocr_client
import base64

ocr = Blueprint('ocr', __name__)

ALLOWED_EXTENSIONS = ['png', 'jpg', 'bmp']
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

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

    if ',' in base64str:
        base64str = base64str.rsplit(',', 1)[1]

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

@ocr.route('/general/image', methods=['post'])
def general_image():
    image = request.files.get('image')
    language_type = request.form.get('language_type', 'CHN_ENG')
    detect_direction = request.form.get('detect_direction', False)
    detect_language = request.form.get('detect_language', False)
    probability = request.form.get('probability', False)

    if not image:
        return jsonify({
            'result': False,
            'msg': u'缺少image',
        })

    if not(image and allowed_file(image.filename)):
        return jsonify({
            'result': False,
            'msg': u'文件上传失败,只允许jpg/png/bmp',
        })

    # 不存储
    data = image.read()
    res = ocr_client.basicGeneral(data, {
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

@ocr.route('/accurate/base64', methods=['post'])
def accurate_base64():
    data = request.get_json()
    base64str = data.get('base64')
    detect_direction = data.get('detect_direction', False)
    probability = data.get('probability', False)

    if not base64str:
        return jsonify({
            'result': False,
            'msg': u'缺少base64',
        })

    if ',' in base64str:
        base64str = base64str.rsplit(',', 1)[1]

    image = base64.b64decode(base64str) # 将base64解码

    res = ocr_client.basicAccurate(image, {
        'detect_direction': detect_direction,
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

@ocr.route('/accurate/image', methods=['post'])
def accurate_image():
    image = request.files.get('image')
    detect_direction = request.form.get('detect_direction', False)
    probability = request.form.get('probability', False)

    if not image:
        return jsonify({
            'result': False,
            'msg': u'缺少image',
        })

    if not(image and allowed_file(image.filename)):
        return jsonify({
            'result': False,
            'msg': u'文件上传失败,只允许jpg/png/bmp',
        })

    # 不存储
    data = image.read()
    res = ocr_client.basicAccurate(data, {
        'detect_direction': detect_direction,
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
