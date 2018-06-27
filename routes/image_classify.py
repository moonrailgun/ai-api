# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask.blueprints import Blueprint
from ai_clients import image_classify_client
import base64

image_classify = Blueprint('image_classify', __name__)

ALLOWED_EXTENSIONS = ['png', 'jpg', 'bmp']
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@image_classify.route('/general', methods=['post'])
def advanced_general():
    image = request.files.get('image')

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
    res = image_classify_client.advancedGeneral(data)

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })

@image_classify.route('/dishDetect', methods=['post'])
def dish_detect():
    image = request.files.get('image')
    top_num = request.form.get('top_num', 5)

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
    res = image_classify_client.dishDetect(data, {'top_num': top_num})

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })

@image_classify.route('/carDetect', methods=['post'])
def car_detect():
    image = request.files.get('image')
    top_num = request.form.get('top_num', 5)

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
    res = image_classify_client.carDetect(data, {'top_num': top_num})

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })

@image_classify.route('/logoSearch', methods=['post'])
def logo_search():
    image = request.files.get('image')
    custom_lib = request.form.get('custom_lib', False)

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
    res = image_classify_client.logoSearch(data, {'custom_lib': custom_lib})

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })

@image_classify.route('/animalDetect', methods=['post'])
def animal_detect():
    image = request.files.get('image')
    top_num = request.form.get('top_num', 6)

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
    res = image_classify_client.animalDetect(data, {'top_num': top_num})

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })

@image_classify.route('/plantDetect', methods=['post'])
def plant_detect():
    image = request.files.get('image')

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
    res = image_classify_client.plantDetect(data)

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })

@image_classify.route('/objectDetect', methods=['post'])
def object_detect():
    image = request.files.get('image')
    with_face = request.form.get('with_face', False)

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
    res = image_classify_client.objectDetect(data, {'with_face': with_face})

    if res.get('error_code'):
        return jsonify({
            'result': False,
            'msg': res.get('error_msg', ''),
        })

    return jsonify({
        'result': True,
        'data': res,
    })
