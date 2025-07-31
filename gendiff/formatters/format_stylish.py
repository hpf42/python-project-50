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
        list_string.append(
            f"{indent}{k}: {format_dic(v, replacer, deep_indent_size)}"
        )
    result = itertools.chain('{', list_string, [current_indent + '}'])
    return '\n'.join(result)


def is_bool(diff):
    if type(diff) is bool:
        return str(diff).lower()
    elif diff is None:
        return 'null'
    else:
        return str(diff)


def get_stylish_format(diff, replacer=' ', add='+ ', remove='- '):

    def iter_(current_item, depth):
        if not isinstance(current_item, dict):
            return str(current_item)

        deep_indent_size = depth + INDENT_STEP
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth

        list_string = []
        for key, val in current_item.items():
            status = val.get(STATUS)
            if status == REMOVED:
                values = is_bool(val.get(VALUE))
                list_string.append(
                    f"{deep_indent[:-2]} \
                        {remove}{key}: \
                            {format_dic(values, replacer, deep_indent_size)}"
                )
            elif status == ADDED:
                values = is_bool(val.get(VALUE))
                list_string.append(
                    f"{deep_indent[:-2]} \
                        {add}{key}: \
                            {format_dic(values, replacer, deep_indent_size)}"
                )
            elif status == UNCHANGED:
                values = is_bool(val.get(VALUE))
                list_string.append(
                    f"{deep_indent}{key}: \
                        {format_dic(values, replacer, deep_indent_size)}"
                )
            elif status == UPDATED:
                value1 = is_bool(val.get(VALUE))
                value2 = is_bool(val.get(UPDATED_VALUE))
                list_string.append(
                    f"{deep_indent[:-2]} \
                        {remove}{key}: \
                            {format_dic(value1, replacer, deep_indent_size)}"
                )
                list_string.append(
                    f"{deep_indent[:-2]} \
                        {add}{key}: \
                            {format_dic(value2, replacer, deep_indent_size)}"
                )
            elif status == NESTED:
                list_string.append(
                    f"{deep_indent}{key}: \
                        {iter_(val.get(VALUE), deep_indent_size)}"
                )
            else:
                raise ValueError(f"{ERROR}: key={key}, val={val}")
        result = itertools.chain('{', list_string, [current_indent + '}'])
        return '\n'.join(result)

    return iter_(diff, 0)
