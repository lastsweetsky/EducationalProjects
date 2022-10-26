from Diploma.utils.airport_charges_utils import *
from Diploma.utils.utils import read_parameter_by_parameter_name

ROUND_TO = 2


def airport_charges(aircraft_info, airport_fee_utilization_rate, take_off_landing_maintenance_fees,
                    commercial_service_fees, ground_maintenance_fees, service_charge_on_root_for_100_km,
                    l_i, total_landing_fees):

    airport_charges = calculate_airport_charges(
        take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
        commercial_service_fees=commercial_service_fees,
        ground_maintenance_fees=ground_maintenance_fees,
        airport_fee_utilization_rate=airport_fee_utilization_rate)

    max_take_off_weight = read_parameter_by_parameter_name(aircraft_info, 'MTOW')

    route_service_fees = calculate_route_service_fees(
        service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
        l_i=l_i,
        max_take_off_weight=max_take_off_weight)

    air_navigation_charges = calculate_air_navigation_charges(
        total_landing_fees=total_landing_fees,
        route_service_fees=route_service_fees)

    return {
        'Airport charges': round(airport_charges, ROUND_TO),
        'Route service fees': round(route_service_fees, ROUND_TO),
        'Air navigation charges': round(air_navigation_charges, ROUND_TO)
    }
