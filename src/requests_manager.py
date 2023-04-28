import requests


def get_response(context):
    return requests.post(context.url, json=context.payload)


def get_status_code(context):
    response = requests.post(context.url, json=context.payload)
    return response.status_code

