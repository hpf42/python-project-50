import json


def get_json_format(diff):
    indent = 4
    separators = (',', ': ')
    return json.dumps(diff, indent=indent, separators=separators)