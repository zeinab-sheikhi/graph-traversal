def sort_dict_keys_by_list_order(dictionary, order_list):
    return {key: dictionary[key] for key in order_list if key in dictionary}


def sort_dict_keys(dictionary, reverse=True):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse)).keys()
