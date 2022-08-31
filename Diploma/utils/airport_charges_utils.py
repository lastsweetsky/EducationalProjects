def calculate_airport_charges(
        take_off_landing_maintenance_fees : float,
        commercial_service_fees : float,
        ground_maintenance_fees : float,
        airport_fee_utilization_rate : float
):
    return (take_off_landing_maintenance_fees + commercial_service_fees + ground_maintenance_fees) * airport_fee_utilization_rate


def calculate_route_service_fees(
        service_charge_on_root_for_100_km : float,
        orthodomic_distance : float,
        max_take_off_weight : float
):
    return service_charge_on_root_for_100_km * orthodomic_distance * (max_take_off_weight/5)**(1/2)


def calculate_air_navigation_charges(
        total_landing_fees: float,
        route_service_fees: float
):
    return total_landing_fees + route_service_fees
