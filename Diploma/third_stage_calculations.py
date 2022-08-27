import numpy as np

from Diploma.airport_charges import calculate_airport_charges, calculate_route_service_fees, \
    calculate_air_navigation_charges
from Diploma.utils import read_parameter_by_parameter_name

def calculate_flight_costs(
  c_fh : float,
  t_f : np.array,
  Q_f : np.array,
  C_t : float
):
    return c_fh * t_f + Q_f * C_t


def calculate_flight_duration(
        l_i: np.array,
        v_f: np.array
):
    return l_i/v_f


def calculate_specific_transportation_costs_at_max_payload(
        c_f : np.array,
        l_i : np.array,
        l_ult: float,
        g_p_max: float,
        g_pi: np.array
):
    return np.array([
        c_f[i] / (g_p_max * l_buf)
        if l_buf <= l_ult
        else c_f[i] / (g_pi * l_buf)
        for i, l_buf in enumerate(l_i)])


def calculate_specific_transportation_costs_at_calculated_payload(
        c_f : np.array,
        l_i : np.array,
        g_p_c: float
):
    return c_f / (g_p_c * l_i)


def airport_charges(aircraft_info):
    airport_fee_utilization_rate = 0.5
    take_off_landing_maintenance_fees = 20 #input
    commercial_service_fees = 10 #input
    ground_maintenance_fees = 140 #input
    airport_charges = calculate_airport_charges(take_off_landing_maintenance_fees=take_off_landing_maintenance_fees, commercial_service_fees=commercial_service_fees, ground_maintenance_fees=ground_maintenance_fees, airport_fee_utilization_rate=airport_fee_utilization_rate)

    service_charge_on_root_for_100_km = 15 #input
    orthodomic_distance = 36 #input
    max_take_off_weight = read_parameter_by_parameter_name(aircraft_info, 'MTOW')
    route_service_fees = calculate_route_service_fees(service_charge_on_root_for_100_km=service_charge_on_root_for_100_km, orthodomic_distance=orthodomic_distance, max_take_off_weight=max_take_off_weight)

    total_landing_fees = 15 #input
    air_navigation_charges = calculate_air_navigation_charges(total_landing_fees=total_landing_fees, route_service_fees=route_service_fees)

    return airport_charges, route_service_fees, air_navigation_charges
