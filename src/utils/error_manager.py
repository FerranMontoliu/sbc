from model.city import City


def check_data_validity(cities: [City], from_city: str, to_city: str) -> None:
    if not cities:
        raise Exception("ERROR. No cities provided.")

    if not from_city:
        raise Exception("ERROR. The origin city cannot be empty.")

    if not to_city:
        raise Exception("ERROR. The destination city cannot be empty.")

    from_found: bool = False
    to_found: bool = False
    for city in cities:
        if city == from_city:
            from_found = True
        elif city == to_city:
            to_found = True

        if from_found and to_found:
            break

    if not from_found:
        raise Exception("ERROR. The origin city does not exist in the dataset.")

    if not to_found:
        raise Exception("ERROR. The destination city does not exist in the dataset.")

    if from_city == to_city:
        raise Exception("ERROR. The origin and the destination cities cannot be the same.")
