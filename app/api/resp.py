#! -*- coding=utf-8

import json
from flask import Response, jsonify

err_dict_zh = {
    # common
    '1000': u'success',
    '1001': u'api failed',
    '1002': u'invalid parameter',
    '2001': u'issue not exist',
    '2002': u'create issue failed',
    '3001': u'invoke qa perf failed',
}
err_unknown_zh = u'unknown issue'


def get_err_msg(err_code, language='zh'):
    err_dict = err_dict_zh
    err_unknown = err_unknown_zh
    return err_dict[str(err_code)] if str(err_code) in err_dict else err_unknown


def secure_response(raw_response=None):
    if type(raw_response) is not list and not raw_response:
        raw_response = ""
    raw_json_str = json.dumps({'data':raw_response})
    return Response(raw_json_str, mimetype='application/json')


def secure_reject(status_code, code):
    res = jsonify({
        "error_code": code,
        "error_message": get_err_msg(code)
    })
    res.status_code = status_code
    return res

def secure_reject_with_message(status_code, message):
    res = jsonify({
        "error_code": status_code,
        "error_message": message
    })
    res.status_code = status_code
    return res


def data_response(raw_response=None):
    if type(raw_response) is not list and not raw_response:
        raw_response = ""
    raw_json_str = json.dumps(raw_response)
    return Response(raw_json_str, mimetype='application/json')