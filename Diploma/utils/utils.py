def read_parameter_by_parameter_name(aircraft_info, parameter_name):
    return [parameter["parameter value"]
            for parameter in aircraft_info
            if parameter["parameter name"] == parameter_name
            ][0]
