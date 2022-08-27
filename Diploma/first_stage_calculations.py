import numpy
import numpy as np

from Diploma.data.finance_data import FINANCE_DATA
from Diploma.second_stage_calculations import calculate_distance_cruise_flight, calculate_fuel_burn_per_flight, \
    calculate_specific_fuel_consumption_at_max_payload, calculate_specific_fuel_consumption_at_calculated_payload
from Diploma.third_stage_calculations import calculate_flight_duration, calculate_flight_costs, \
    calculate_specific_transportation_costs_at_max_payload, \
    calculate_specific_transportation_costs_at_calculated_payload
from Diploma.utils import read_parameter_by_parameter_name


def calculate_coef_max_payload(g_p_c, g_p_max):
    return g_p_c / g_p_max


def calculate_aircraft_productivity_per_flight(g_pi, v_f):
    return g_pi * v_f


def calculate_flight_speed(l_i, t_tl, t_cf):
    return l_i / (t_tl + t_cf)


def calculate_time_of_cruise_flight(l_i, l_tl, v_cr):
    return (l_i - l_tl) / v_cr


def calculate_payload_after_ultimate_range_at_max_payload(
        g_p_max: float,
        q_cr_km: float,
        l_i: np.array,
        l_ult: float,
) -> np.array:
    m_coef = q_cr_km * 0.001
    return np.array(
        [g_p_max
         if l_buf <= l_ult
         else g_p_max - m_coef * (l_buf - l_ult)
         for i, l_buf in enumerate(l_i)]
    )


def calculate_aircraft_productivity_per_flight_at_calculated_payload(
        l_i: np.array,
        l_ult: float,
        g_p_c: float,
        v_f: np.array,
        e_c: float,
        g_pi: np.array
):
    return np.array([
        g_p_c * v_f[i]
        if l_buf <= l_ult
        else e_c * g_pi[i] * v_f[i]
        for i, l_buf in enumerate(l_i)])


def test_first_phase_of_calculations(aircraft_info, country="UKR"):
    g_p_max = read_parameter_by_parameter_name(aircraft_info, 'G_p_max')
    l_i = np.array([1900, 2600, 3300, 4000, 4700, 5400])
    l_ult = read_parameter_by_parameter_name(aircraft_info, 'L_ult')
    q_cr_km = read_parameter_by_parameter_name(aircraft_info, 'q_cr_km')
    g_pi = calculate_payload_after_ultimate_range_at_max_payload(q_cr_km=q_cr_km, g_p_max=g_p_max, l_i=l_i, l_ult=l_ult)

    v_cr = read_parameter_by_parameter_name(aircraft_info, 'V_cr')
    l_tl = read_parameter_by_parameter_name(aircraft_info, 'L_tl')
    t_cf = calculate_time_of_cruise_flight(l_i=l_i, v_cr=v_cr, l_tl=l_tl)

    t_tl = read_parameter_by_parameter_name(aircraft_info, 't_tl')
    v_f = calculate_flight_speed(l_i=l_i, t_tl=t_tl, t_cf=t_cf)

    #TODO: compare g_p_c to max weight => choose aircrafts
    g_p_c = 40
    e_c = calculate_coef_max_payload(g_p_c=g_p_c, g_p_max=g_p_max)

    a_ftk_max = calculate_aircraft_productivity_per_flight(g_pi=g_pi, v_f=v_f)
    a_ftk_c = calculate_aircraft_productivity_per_flight_at_calculated_payload(l_i=l_i, l_ult=l_ult, g_p_c=g_p_c,
                                                                               v_f=v_f, e_c=e_c, g_pi=g_pi)

    l_cruise = calculate_distance_cruise_flight(l_i=l_i, l_tl=l_tl)

    q_f = read_parameter_by_parameter_name(aircraft_info, 'q_f')
    Q_f = calculate_fuel_burn_per_flight(q_f=q_f, q_cr_km=q_cr_km, l_cruise=l_cruise)

    q_sp_1 = calculate_specific_fuel_consumption_at_max_payload(Q_f=Q_f, g_p_max=g_p_max, l_i=l_i, l_ult=l_ult, g_pi=g_pi)
    q_sp_2 = calculate_specific_fuel_consumption_at_calculated_payload(Q_f=Q_f, g_p_c=g_p_c, l_i=l_i, l_ult=l_ult, e_c=e_c, g_pi=g_pi)


    t_f = calculate_flight_duration(l_i=l_i, v_f=v_f)

    C_t = FINANCE_DATA[country]["C_t"]

    c_fh = read_parameter_by_parameter_name(aircraft_info, 'C_fh')
    c_f = calculate_flight_costs(c_fh=c_fh, t_f=t_f, Q_f=Q_f, C_t=C_t)

    c_sp_1 = calculate_specific_transportation_costs_at_max_payload(c_f=c_f, g_p_max=g_p_max,g_pi=g_pi, l_i=l_i, l_ult=l_ult)
    c_sp_2 = calculate_specific_transportation_costs_at_calculated_payload(c_f=c_f, g_p_c=g_p_c, l_i=l_i)

    return a_ftk_c/a_ftk_max, q_sp_1/q_sp_2, (Q_f*C_t)/c_f
