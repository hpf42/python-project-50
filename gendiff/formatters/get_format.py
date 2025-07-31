from gendiff.formatters.format_json import get_json_format
from gendiff.formatters.format_plain import get_plain_format
from gendiff.formatters.format_stylish import get_stylish_format


def get_format(diff, format: str):
    if format == 'stylish':
        return get_stylish_format(diff)
    if format == 'plain':
        return get_plain_format(diff)
    if format == 'json':
        return get_json_format(diff)
    return None