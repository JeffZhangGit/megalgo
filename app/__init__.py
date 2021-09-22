import logging
from flask import Flask
from app.service.git_client import git_client_instance
from app.service.jira_client import jira_client_instance
from app.api.issue import *
from app.api.ngrinder import *
from app.api.datasource import *

formatter = '%(asctime)s %(levelname)8s [%(filename)18s:%(lineno)04d]: %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

app = Flask(__name__)


def create_app():
    # app.config.from_object('config')
    blueprint.add_url_rule(rule='/create_issue', view_func=create_issue)
    blueprint.add_url_rule(rule='/get_issue_info', view_func=get_issue_info)

    blueprint.add_url_rule(rule='/datasource_zt', view_func=zt)
    blueprint.add_url_rule(rule='/datasource_new_zt', view_func=new_zt)

    blueprint.add_url_rule(rule='/invoke_perf', view_func=invoke_perf)
    blueprint.add_url_rule(rule='/get_result', view_func=get_result)
    logging.info('create app')

    app.register_blueprint(blueprint, url_prefix='/qaapi')
    return app


@app.route('/', methods=['get'])
def health_check():
    return "ok"

