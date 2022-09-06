def read_parameter_by_parameter_name(aircraft_info, parameter_name):
    try:
        return [parameter["parameter value"]
                for parameter in aircraft_info
                if parameter["parameter name"] == parameter_name
                ][0]
    except KeyError:
        print('No such parameter')
