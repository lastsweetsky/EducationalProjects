import pandas as pd

from Diploma.data.companies_data import COMPANIES_DATA
from Diploma.calculus.productivity_fuel_costs import test_first_phase_of_calculations
from Diploma.calculus.loan_leasing import economic_substation
from Diploma.calculus.airport_charges import airport_charges
from Diploma.data.aircrafts_data import AIRCRAFT_DATA
from Diploma.utils.utils import read_parameter_by_parameter_name

l_i = 500
g_p_c = 40

years = 5
guaranteed_deposit = 25
annual_rate_on_leasing = 30
annual_interest_rate_on_capital_market = 10

airport_fee_utilization_rate = 0.5
take_off_landing_maintenance_fees = 20
commercial_service_fees = 10
ground_maintenance_fees = 140
service_charge_on_root_for_100_km = 15
total_landing_fees = 15


def info_for_aircraft(
        aircraft_type,
        country = 'UKR',
        l_i=l_i,
        g_p_c=g_p_c,
        years=years,
        guaranteed_deposit=guaranteed_deposit,
        annual_rate_on_leasing=annual_rate_on_leasing,
        annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market,
        take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
        commercial_service_fees=commercial_service_fees,
        ground_maintenance_fees=ground_maintenance_fees,
        service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
        total_landing_fees=total_landing_fees
):

    df_dict = {'Aircraft': aircraft_type}

    aircraft_info = [aircraft
                     for aircraft in AIRCRAFT_DATA
                     if aircraft["aircraft name"] == aircraft_type
                     ][0]["aircraft info"]

    g_p_max = read_parameter_by_parameter_name(aircraft_info, 'G_p_max')
    l_l = read_parameter_by_parameter_name(aircraft_info, 'L_l')

    if g_p_c > g_p_max:
        return pd.DataFrame()

    if l_i > l_l:
        return pd.DataFrame()

    df_dict.update(test_first_phase_of_calculations(aircraft_info, l_i=l_i, g_p_c=g_p_c))
    df_dict.update(economic_substation(
        aircraft_info,
        years=years,
        country=country,
        guaranteed_deposit=guaranteed_deposit,
        annual_rate_on_leasing=annual_rate_on_leasing,
        annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market))

    df_dict.update(airport_charges(
        aircraft_info,
        airport_fee_utilization_rate=airport_fee_utilization_rate,
        take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
        commercial_service_fees=commercial_service_fees,
        ground_maintenance_fees=ground_maintenance_fees,
        service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
        l_i=l_i,
        total_landing_fees=total_landing_fees))

    df_dict = {key: [value] for key, value in df_dict.items()}
    df = pd.DataFrame.from_dict(df_dict)
    return df


def info_for_company(country,
        company_to_test='Airbus',
        l_i=l_i,
        g_p_c=g_p_c,
        years=years,
        guaranteed_deposit=guaranteed_deposit,
        annual_rate_on_leasing=annual_rate_on_leasing,
        annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market,
        take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
        commercial_service_fees=commercial_service_fees,
        ground_maintenance_fees=ground_maintenance_fees,
        service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
        total_landing_fees=total_landing_fees
):
    df = pd.DataFrame()

    if company_to_test == 'ALL':
        for company in COMPANIES_DATA.keys():
            for aircraft_type in COMPANIES_DATA[company]:
                df = df.append(info_for_aircraft(
                    aircraft_type,
                    g_p_c=g_p_c,
                    l_i=l_i,
                    years=years,
                    country=country,
                    guaranteed_deposit=guaranteed_deposit,
                    annual_rate_on_leasing=annual_rate_on_leasing,
                    annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market,
                    take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
                    commercial_service_fees=commercial_service_fees,
                    ground_maintenance_fees=ground_maintenance_fees,
                    service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
                    total_landing_fees=total_landing_fees
                ))
        return df

    for aircraft_type in COMPANIES_DATA[company_to_test]:
        df = df.append(info_for_aircraft(
            aircraft_type,
            g_p_c=g_p_c,
            l_i=l_i,
            years=years,
            country=country,
            guaranteed_deposit=guaranteed_deposit,
            annual_rate_on_leasing=annual_rate_on_leasing,
            annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market,
            take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
            commercial_service_fees=commercial_service_fees,
            ground_maintenance_fees=ground_maintenance_fees,
            service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
            total_landing_fees=total_landing_fees
        ))
    return df
