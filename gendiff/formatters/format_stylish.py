import itertools


STATUS = 'status'
ADDED = 'added'
NESTED = 'nested'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
VALUE = 'value'
UPDATED_VALUE = 'updated_value'
ERROR = 'Object has no STATUS'
INDENT_STEP = 4


def format_dic(diff, replacer, depth=0):
    if not isinstance(diff, dict):
        return str(diff)
    deep_indent_size = depth + INDENT_STEP
    indent = replacer * deep_indent_size
    current_indent = replacer * depth
    list_string = []
    for k, v in diff.items():
        if not isinstance(diff, dict):
            list_string.append(f'{indent}{k}: {v}')
        else:
            list_string.append(
                f"{indent}{k}: "
                f"{format_dic(v, replacer, deep_indent_size)}"
            )
    result = itertools.chain('{', list_string, [current_indent + '}'])
    return '\n'. join(result)


def is_bool(diff):
    if type(diff) is bool:
        return str(diff).lower()
    elif diff is None:
        return 'null'
    else:
        return diff


def get_stylish_format(diff, replacer=' ', add='+ ', remove='- '):

    def iter_(current_item, depth):
        if not isinstance(current_item, dict):
            return str(current_item)

        deep_indent_size = depth + INDENT_STEP
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth

        list_string = []
        for key, val in current_item.items():
            if val[STATUS] == REMOVED:
                values = is_bool(val[VALUE])
                list_string.append(
                    f"{deep_indent[: - 2]}{remove}{key}: "
                    f"{format_dic(values, replacer, deep_indent_size)}"
                )
            elif val[STATUS] == ADDED:
                values = is_bool(val[VALUE])
                list_string.append(
                    f"{deep_indent[: - 2]}{add}{key}: "
                    f"{format_dic(values, replacer, deep_indent_size)}"
                )
            elif val[STATUS] == UNCHANGED:
                values = is_bool(val[VALUE])
                list_string.append(
                    f"{deep_indent}{key}: "
                    f"{format_dic(values, replacer, deep_indent_size)}"
                )
            elif val[STATUS] == UPDATED:
                value1 = is_bool(val[VALUE])
                value2 = is_bool(val[UPDATED_VALUE])
                list_string.append(
                    f"{deep_indent[: - 2]}{remove}{key}: "
                    f"{format_dic(value1, replacer, deep_indent_size)}"
                )
                list_string.append(
                    f"{deep_indent[: -2]}{add}{key}: "
                    f"{format_dic(value2, replacer, deep_indent_size)}")
            elif val[STATUS] == NESTED:
                list_string.append(
                    f"{deep_indent}{key}: "
                    f"{iter_(val[VALUE], deep_indent_size)}"
                )
            else:
                raise ERROR
        result = itertools.chain('{', list_string, [current_indent + '}'])
        return '\n'.join(result)

    return iter_(item, 0)