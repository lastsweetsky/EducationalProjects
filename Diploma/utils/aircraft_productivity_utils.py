import numpy as np


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
