from Diploma.data.companies_data import COMPANIES_DATA
from Diploma.calculus.productivity_fuel_costs import test_first_phase_of_calculations
from Diploma.calculus.loan_leasing import economic_substation
from Diploma.calculus.airport_charges import airport_charges
from Diploma.data.aircrafts_data import AIRCRAFT_DATA

import numpy as np

l_i = np.array([1900, 2600, 3300, 4000, 4700, 5400])
g_p_c = 40

years = 5
# country
guaranteed_deposit = 25
annual_rate_on_leasing = 30
annual_interest_rate_on_capital_market = 10

airport_fee_utilization_rate = 0.5  # constant
take_off_landing_maintenance_fees = 20
commercial_service_fees = 10
ground_maintenance_fees = 140
service_charge_on_root_for_100_km = 15
orthodomic_distance = 36
total_landing_fees = 15


def info_for_company(g_p_c=g_p_c, company_to_test='Airbus'):
    result = f'{company_to_test}\n'
    for aircraft_type in COMPANIES_DATA[company_to_test]:
        aircraft_info = [aircraft
                         for aircraft in AIRCRAFT_DATA
                         if aircraft["aircraft name"] == aircraft_type
                         ][0]["aircraft info"]

        result += str(test_first_phase_of_calculations(aircraft_info, l_i=l_i, g_p_c=g_p_c))
        result += str(economic_substation(aircraft_info, years=years, guaranteed_deposit=guaranteed_deposit,
                                  annual_rate_on_leasing=annual_rate_on_leasing,
                                  annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market))

        result += str(airport_charges(aircraft_info, airport_fee_utilization_rate=airport_fee_utilization_rate,
                              take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
                              commercial_service_fees=commercial_service_fees,
                              ground_maintenance_fees=ground_maintenance_fees,
                              service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
                              orthodomic_distance=orthodomic_distance, total_landing_fees=total_landing_fees))
    return result


if __name__ == "__main__":
    info_for_company()
