from Diploma.calculus.loan_leasing import *
from Diploma.utils.aircraft_productivity_utils import *
from Diploma.utils.specific_fuel_consumption_utils import *
from Diploma.utils.specific_transportation_costs_utils import *
from Diploma.utils.utils import read_parameter_by_parameter_name

ROUND_TO = 2


def test_first_phase_of_calculations(aircraft_info, l_i, g_p_c, country="UKR"):
    g_p_max = read_parameter_by_parameter_name(aircraft_info, 'G_p_max')

    l_ult = read_parameter_by_parameter_name(aircraft_info, 'L_ult')
    q_cr_km = read_parameter_by_parameter_name(aircraft_info, 'q_cr_km')
    g_pi = calculate_payload_after_ultimate_range_at_max_payload(q_cr_km=q_cr_km, g_p_max=g_p_max, l_i=l_i, l_ult=l_ult)

    v_cr = read_parameter_by_parameter_name(aircraft_info, 'V_cr')
    l_tl = read_parameter_by_parameter_name(aircraft_info, 'L_tl')
    t_cf = calculate_time_of_cruise_flight(l_i=l_i, v_cr=v_cr, l_tl=l_tl)

    t_tl = read_parameter_by_parameter_name(aircraft_info, 't_tl')
    v_f = calculate_flight_speed(l_i=l_i, t_tl=t_tl, t_cf=t_cf)

    e_c = calculate_coef_max_payload(g_p_c=g_p_c, g_p_max=g_p_max)

    a_ftk_max = round(calculate_aircraft_productivity_per_flight(g_pi=g_pi, v_f=v_f), ROUND_TO)

    a_ftk_c = round(calculate_aircraft_productivity_per_flight_at_calculated_payload(
        l_i=l_i,
        l_ult=l_ult,
        g_p_c=g_p_c,
        v_f=v_f,
        e_c=e_c,
        g_pi=g_pi), ROUND_TO)

    l_cruise = calculate_distance_cruise_flight(l_i=l_i, l_tl=l_tl)

    q_f = read_parameter_by_parameter_name(aircraft_info, 'q_f')

    Q_f = round(calculate_fuel_burn_per_flight(
        q_f=q_f,
        q_cr_km=q_cr_km,
        l_cruise=l_cruise), ROUND_TO)

    q_sp_1 = round(calculate_specific_fuel_consumption_at_max_payload(
        Q_f=Q_f,
        g_p_max=g_p_max,
        l_i=l_i,
        l_ult=l_ult,
        g_pi=g_pi), ROUND_TO)

    q_sp_2 = round(calculate_specific_fuel_consumption_at_calculated_payload(
        Q_f=Q_f,
        g_p_c=g_p_c,
        l_i=l_i,
        l_ult=l_ult,
        e_c=e_c,
        g_pi=g_pi), ROUND_TO)

    t_f = calculate_flight_duration(l_i=l_i, v_f=v_f)
    C_t = FINANCE_DATA[country]["C_t"]
    c_fh = read_parameter_by_parameter_name(aircraft_info, 'C_fh')
    c_f = round(calculate_flight_costs(c_fh=c_fh, t_f=t_f, Q_f=Q_f, C_t=C_t), ROUND_TO)

    c_sp_1 = round(calculate_specific_transportation_costs_at_max_payload(
        c_f=c_f,
        g_p_max=g_p_max,
        g_pi=g_pi,
        l_i=l_i,
        l_ult=l_ult), ROUND_TO)

    c_sp_2 = round(calculate_specific_transportation_costs_at_calculated_payload(
        c_f=c_f,
        g_p_c=g_p_c,
        l_i=l_i), ROUND_TO)


    return {
        'Productivity': a_ftk_c,
        'Productivity to ideal': round(a_ftk_c / a_ftk_max, ROUND_TO),
        'Fuel burnt per flight': Q_f,
        'Fuel economy to ideal': round(q_sp_2 / q_sp_1, ROUND_TO),
        'Flight cost': c_f,
        'Ecost for trasnp 1 unit': q_sp_2
    }
