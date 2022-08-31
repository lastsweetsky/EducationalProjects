from Diploma.data.finance_data import FINANCE_DATA
from Diploma.utils.loan_leasing_utils import *
from Diploma.utils.utils import read_parameter_by_parameter_name

ROUND_TO = 2

def economic_substation(aircraft_info, years, guaranteed_deposit, annual_rate_on_leasing,
                        annual_interest_rate_on_capital_market, country='UKR'):

    price = read_parameter_by_parameter_name(aircraft_info, 'Price')

    interest_rate = FINANCE_DATA[country]["Interest rate"]
    income_tax_rate = FINANCE_DATA[country]["Income tax rate"]

    annual_loan_amount = callculate_annual_loan_amount(price=price, years=years)
    interest_for_each_year = calculate_interest_for_each_year(
        price=price,
        annual_loan_amount=annual_loan_amount,
        interest_rate=interest_rate,
        years=years)

    total_interest_rate = calculate_total_interest_rate(interest_for_each_year=interest_for_each_year)

    aircraft_cost_under_loan = calculate_aircraft_cost_under_loan_structure(
        price=price,
        total_interest_rate=total_interest_rate)

    price_of_guaranteed_deposit = calculate_price_of_guaranteed_deposit(
        price=price,
        guaranteed_deposit=guaranteed_deposit)

    aircraft_price_looses = calculate_price_aircraft_looses(
        price=price,
        annual_rate_on_leasing=annual_rate_on_leasing)

    aircraft_cost_under_leasing = calculate_aircraft_cost_under_leasing(
        price_of_guaranteed_deposit=price_of_guaranteed_deposit,
        aircraft_price_looses=aircraft_price_looses,
        income_tax_rate=income_tax_rate,
        annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market,
        years=years)

    residual_value = calculate_residual_value_for_leasing(
        aircraft_cost_under_leasing=aircraft_cost_under_leasing,
        price=price)

    return {
        'Cost under loan': round(aircraft_cost_under_loan, ROUND_TO),
        'Cost under leasing': round(aircraft_cost_under_leasing, ROUND_TO),
        'Residual leasing value': round(residual_value, ROUND_TO)
    }
