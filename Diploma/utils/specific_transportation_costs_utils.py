def calculate_flight_costs(
  c_fh : float,
  t_f : float,
  Q_f : float,
  C_t : float
):
    return c_fh * t_f + Q_f * C_t


def calculate_flight_duration(
        l_i: float,
        v_f: float
):
    return l_i/v_f


def calculate_specific_transportation_costs_at_max_payload(
        c_f: float,
        l_i: float,
        l_ult: float,
        g_p_max: float,
        g_pi: float
):
    if l_i <= l_ult:
        return c_f / (g_p_max * l_i)
    else:
        return c_f / (g_pi * l_i)


def calculate_specific_transportation_costs_at_calculated_payload(
        c_f : float,
        l_i : float,
        g_p_c: float
):
    return c_f / (g_p_c * l_i)
