import json


def get_json_format(diff):
    separators = (',', ': ')
    return json.dumps(diff, separators=separators)