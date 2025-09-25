"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*param):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(param)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # extract wagon list
    [end_id_one, end_id_two, *rest] = each_wagons_id

    # move these to the end
    *rest, = *rest, *[end_id_one, end_id_two]

    # extract first ID
    [first_id, *rest] = rest 

    # join rest to the second list
    *rest, = *missing_wagons, *rest 

    return [first_id, *rest]


def add_missing_stops(route, **param):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    result = {"stops": list(param.values())}

    # add the result to the route dict
    route = {**route, **result}

    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    
    # unpack the list
    x, y, z = wagons_rows

    result = []

    # pack them in the desired order
    for ii in range(len(wagons_rows)):
        *result, = *result, *[[x[ii], y[ii], z[ii]]]
    
    return result
