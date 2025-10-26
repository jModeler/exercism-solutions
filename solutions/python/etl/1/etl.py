def transform(legacy_data):
    result = {}
    for key, values in legacy_data.items():
        for value in values:
            value = value.lower()
            result[value] = key 
    return result