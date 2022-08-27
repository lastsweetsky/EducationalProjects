from Diploma.data.company_data import COMPANIES_DATA
from Diploma.first_stage_calculations import test_first_phase_of_calculations
from Diploma.second_stage_calculations import economic_substation
from Diploma.third_stage_calculations import airport_charges
from Diploma.data.aircrafts_data import AIRCRAFT_DATA


def main():
    company_to_test = "Airbus"
    for aircraft_type in COMPANIES_DATA[company_to_test]:
        aircraft_info = [aircraft
                         for aircraft in AIRCRAFT_DATA
                         if aircraft["aircraft name"] == aircraft_type
                         ][0]["aircraft info"]

        print(test_first_phase_of_calculations(aircraft_info))
        print(economic_substation(aircraft_info))
        print(airport_charges(aircraft_info))


if __name__ == "__main__":
    main()
