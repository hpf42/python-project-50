from gendiff.formatters.json_formatter import get_json_format
from gendiff.formatters.plain_formatter import get_plain_format
from gendiff.formatters.stylish_formatter import get_stylish_format


def format_identifier(diff, formatter):
    if formatter == 'stylish':
        return get_stylish_format(diff)
    if formatter == 'plain':
        return get_plain_format(diff)
    if formatter == 'json':
        return get_json_format(diff)
    else:
        raise ValueError(f"Unsupported formatter: {formatter}")