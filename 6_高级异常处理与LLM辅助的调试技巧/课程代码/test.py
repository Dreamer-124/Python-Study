def complex_algorithm(data):
    result = []
    for i, item in enumerate(data):
        processed = process_item(item)
        result.append(processed)
    return result
