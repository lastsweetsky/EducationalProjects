
def calculate_fuel_burn_per_flight(
        q_f : float,
        q_cr_km : float,
        l_cruise: float
):
    return (q_f + q_cr_km * l_cruise) * 1e-3


def calculate_distance_cruise_flight(
        l_i : float,
        l_tl: float
):
    return l_i - l_tl


def calculate_specific_fuel_consumption_at_max_payload(
        Q_f: float,
        g_p_max: float,
        l_i: float,
        l_ult: float,
        g_pi: float
):
    if l_i <= l_ult:
        return (Q_f * 10e6)/(g_p_max * l_i)
    else:
        return (Q_f * 10e6)/(g_pi * l_i)



def calculate_specific_fuel_consumption_at_calculated_payload(
        Q_f : float,
        g_p_c : float,
        e_c : float,
        g_pi : float,
        l_i : float,
        l_ult : float
):
    if l_i <= l_ult:
        return (Q_f * 10e6)/(g_p_c * l_i)
    else:
        return (Q_f * 10e6)/(e_c * g_pi * l_i)

