from flask import Blueprint
import logging

formatter = '%(asctime)s %(levelname)8s [%(filename)18s:%(lineno)04d]: %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter, filename='log.log',filemode='a')
blueprint = Blueprint('qaapi', __name__)