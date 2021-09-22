# coding:utf-8

from . import blueprint
from app.api.resp import secure_reject, secure_response
from app.service.git_client import git_client_instance
from app.service.jira_client import jira_client_instance
from app.api.base import *
from app import logging

# create issue, return issue id
@blueprint.route('/jira/create_issue', methods=['post'])
def create_issue():
    try:
        summary, assignee, description, = get_arguments(['summary', 'assignee', 'description'])

        if not summary or not assignee or not description:
            return secure_reject(400, 1002)
        logging.info('summary:' + summary)
        logging.info('assignee:' + assignee)
        logging.info('description:' + description)

        issue_dict = {
            'project': {'key': 'CSGQA'},
            'summary': summary,
            'issuetype': {'name': 'Task'},
            'assignee': {'name': assignee},
            'description': description,
        }

        new_issue = jira_client_instance.jira_create_issue(issue_dict)
        return secure_response({'issue_id': new_issue.raw['key']})
    except Exception, err:
        logging.info(err)
        return secure_reject(400, 2002)


# get issue id, summary, description, related issue id
@blueprint.route('/jira/get_issue_info', methods=['post'])
def get_issue_info():
    try:
        issue_id, project_name, branch_name, bill_code_base_commit_id, bill_commit_id = get_arguments(
            ['issue_id', 'project_name', 'branch_name', 'bill_code_base_commit_id', 'bill_commit_id'])
        if not issue_id:
            return secure_reject(400, 1002)

        issue = jira_client_instance.jira_find_issue_by_id(issue_id)
        temp = {}
        temp['summary'] = issue.raw['fields']['summary']
        temp['description'] = issue.raw['fields']['description']
        temp['status'] = issue.raw['fields']['status']['name']
        temp['creator'] = issue.raw['fields']['creator']['name']
        temp['assignee'] = issue.raw['fields']['assignee']['name']
        links = issue.raw['fields']['issuelinks']
        bugs = []
        for link in links:
            key = link['inwardIssue']['key']
            summary = link['inwardIssue']['fields']['summary']
            status = link['inwardIssue']['fields']['status']['name']
            bug = {"key": key, "summary": summary, "status": status, }
            bugs.append(bug)
        temp['bugs'] = bugs
        code_change, last_commit = git_client_instance.get_commit_change(project_name=project_name,
                                                                         branch_name=branch_name,
                                                                         bill_code_base_commit_id=bill_code_base_commit_id,
                                                                         bill_commit_id=bill_commit_id)
        temp['code_change'] = code_change
        temp['last_commit'] = last_commit
        return secure_response(temp)

    except Exception, err:
        return secure_reject(400, 2001)


# get issue related chart
@blueprint.route('/jira/get_issue_chart', methods=['post'])
def get_issue_chart():
    return "ok"
