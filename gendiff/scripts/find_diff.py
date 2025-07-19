def item_add(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def item_delete(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def items_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def items_modified(key, value_1, value_2):
    return {
        'action': 'modified',
        'name': key,
        'new_value': value_2,
        'old_value': value_1
    }


def items_nested(key, value_1, value_2):
    return {
        'action': 'nested',
        'name': key,
        'children': find_diff(value_1, value_2)
    }


def find_diff(data_1, data_2):
    keys_union = data_1.keys() | data_2.keys()
    keys_added = data_2.keys() - data_1.keys()
    keys_deleted = data_1.keys() - data_2.keys()

    diff = []

    for key in keys_union:
        value_1 = data_1.get(key)
        value_2 = data_2.get(key)

        if key in keys_added:
            diff.append(item_add(key, value_2))
        elif key in keys_deleted:
            diff.append(item_delete(key, value_1))
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            diff.append(items_nested(key, value_1, value_2))
        elif value_1 != value_2:
            diff.append(items_modified(key, value_1, value_2))
        else:
            diff.append(items_unchanged(key, value_1))

    sorted_diff = sorted(diff, key=lambda x: x['name'])

    return sorted_diff