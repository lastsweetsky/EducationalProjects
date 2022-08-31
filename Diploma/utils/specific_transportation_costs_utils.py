import numpy as np


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
