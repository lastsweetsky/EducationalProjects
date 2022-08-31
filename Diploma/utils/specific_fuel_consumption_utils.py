import numpy as np


def calculate_fuel_burn_per_flight(
        q_f : float,
        q_cr_km : float,
        l_cruise: np.array
):
    return (q_f + q_cr_km * l_cruise) * 1e-3


def calculate_distance_cruise_flight(
        l_i : np.array,
        l_tl: float
):
    return l_i - l_tl


def calculate_specific_fuel_consumption_at_max_payload(
        Q_f: float,
        g_p_max: float,
        l_i: np.array,
        l_ult: float,
        g_pi: np.array
):
    return np.array([
        (Q_f[i] * 10e6)/(g_p_max * l_buf)
        if l_buf <= l_ult
        else (Q_f[i] * 10e6)/(g_pi[i] * l_buf)
        for i, l_buf in enumerate(l_i)])


def calculate_specific_fuel_consumption_at_calculated_payload(
        Q_f : np.array,
        g_p_c : float,
        e_c : float,
        g_pi : np.array,
        l_i : np.array,
        l_ult : float
):
    return np.array([
        (Q_f[i] * 10e6)/(g_p_c * l_buf)
        if l_buf <= l_ult
        else (Q_f[i] * 10e6)/(e_c * g_pi[i] * l_buf)
        for i, l_buf in enumerate(l_i)])
