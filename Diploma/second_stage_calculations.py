import numpy as np

from Diploma.data.finance_data import FINANCE_DATA
from Diploma.loan_leasing import callculate_annual_loan_amount, calculate_interest_for_each_year, \
    calculate_total_interest_rate, calculate_aircraft_cost_under_loan_structure, calculate_price_of_guaranteed_deposit, \
    calculate_price_aircraft_looses, calculate_aircraft_cost_under_leasing, calculate_residual_value_for_leasing
from Diploma.utils import read_parameter_by_parameter_name


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


def economic_substation(aircraft_info, country='UKR'):

    price = read_parameter_by_parameter_name(aircraft_info, 'Price')
    #interest_rate = float(input('Please input the interest rate for the loan in your country:\n'))
    #years = int(input('For how many years the loan is?\n'))
    interest_rate = FINANCE_DATA[country]["Interest rate"]
    income_tax_rate = FINANCE_DATA[country]["Income tax rate"]

    years = 5

    annual_loan_amount = callculate_annual_loan_amount(price=price, years=years)
    interest_for_each_year = calculate_interest_for_each_year(price=price, annual_loan_amount=annual_loan_amount, interest_rate=interest_rate, years=years)
    total_interest_rate = calculate_total_interest_rate(interest_for_each_year=interest_for_each_year)
    aircraft_cost_under_loan = calculate_aircraft_cost_under_loan_structure(price=price, total_interest_rate=total_interest_rate)

    #guaranteed_deposit = float(input('Please input the guaranteed deposit under leasing (ex.: 25) in %:\n'))
    guaranteed_deposit = 25
    price_of_guaranteed_deposit = calculate_price_of_guaranteed_deposit(price=price, guaranteed_deposit=guaranteed_deposit)

    #rate_on_capital_market = = float(input('Please input the annual rate on the capital market (ex.: 25) in %:\n'))
    annual_rate_on_leasing = 30
    aircraft_price_looses = calculate_price_aircraft_looses(price=price, annual_rate_on_leasing=annual_rate_on_leasing)
    #income_tax_rate = float(input('....\n'))
    annual_interest_rate_on_capital_market = 10

    aircraft_cost_under_leasing = calculate_aircraft_cost_under_leasing(price_of_guaranteed_deposit=price_of_guaranteed_deposit,aircraft_price_looses=aircraft_price_looses,income_tax_rate=income_tax_rate,annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market,years=years)
    residual_value = calculate_residual_value_for_leasing(aircraft_cost_under_leasing= aircraft_cost_under_leasing, price=price)

    return  aircraft_cost_under_loan, aircraft_cost_under_leasing, residual_value
