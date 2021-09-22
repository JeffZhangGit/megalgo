# coding:utf-8

from flask import request


def get_arguments(fields, default=None):
    values = []
    for field in fields:
        v = request.values.get(field) or request.files.get(field)
        if v is None:
            v = default
        values.append(v)

    return tuple(values)
