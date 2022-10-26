def callculate_annual_loan_amount(
        price : float,
        years : int
):
    return price/years


def calculate_interest_for_each_year(
    price : float,
    annual_loan_amount : float,
    interest_rate : float,
    years : int
):
    interest_for_each_year = []
    for year in range(years):
        if year==0:
            interest_for_each_year.append(price*interest_rate/100)
            continue
        interest_for_each_year.append(
            (price-annual_loan_amount*year)*interest_rate/100
        )
    return interest_for_each_year


def calculate_total_interest_rate(interest_for_each_year):
    return sum(interest_for_each_year)


def calculate_aircraft_cost_under_loan_structure(
        price : float,
        total_interest_rate : float
):
    return price + total_interest_rate


def calculate_price_of_guaranteed_deposit(
        price:float,
        guaranteed_deposit: float
):
    return price * guaranteed_deposit/100


def calculate_price_aircraft_looses(
        price : float,
        annual_rate_on_leasing : float
):
    return price * annual_rate_on_leasing/100


def calculate_aircraft_cost_under_leasing(
        price_of_guaranteed_deposit : float,
        aircraft_price_looses : float,
        income_tax_rate : float,
        annual_interest_rate_on_capital_market : float,
        years: int
):
    return price_of_guaranteed_deposit + sum([
        (aircraft_price_looses * (1-income_tax_rate/100))
        /
        (1 + annual_interest_rate_on_capital_market/100)**(year+1)
        for year in range(years)
    ])


def calculate_residual_value_for_leasing(
        aircraft_cost_under_leasing : float,
        price : float
):
    return  price - aircraft_cost_under_leasing
