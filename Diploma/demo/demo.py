# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash import Dash, dash_table
from geopy import distance
import geopandas as gpd
from dash import dcc
from plotly import express as px
from Diploma.calculations.calculations import info_for_company
from Diploma.data.finance_data import FINANCE_DATA

from Diploma.demo.demo_info import STAGES

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
fig = px.scatter_geo(
    geo_df,
    lat=geo_df.geometry.y,
    lon=geo_df.geometry.x,
    hover_name="name"
)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundColor': colors['background']
    },
    children=[
        html.P(children="✈️",
               className="header-emoji",
               style={
                   'textAlign': 'center'
               }),

        html.H1(
            children="Diploma",
            className="header-title",
            style={
                'textAlign': 'center',
                'color': 'Gold'
            }
        ),

        html.Div(
            children='Techno-economic assessment  of freight types of aircraft utilization on air routes',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),
        html.Br(),
        html.Hr(),
        html.Br(),
        html.Div(
            [
                html.Label("Input weight of cargo in tons: ",
                           style={
                               'textAlign': 'center',
                               'color': colors['text']
                           }
                           ),
                dcc.Input(id="input_g_p_c",
                          type='number',
                          placeholder="Weight of cargo",
                          min=0,
                          max=10000
                          ),

                html.Label("Input length of flight: ",
                           style={
                               'textAlign': 'center',
                               'color': colors['text']
                           }
                           ),
                dcc.Input(id="input_l_i",
                          type='number',
                          placeholder="Length of route",
                          min=0,
                          max=50000
                          ),
            ], style={'display': 'flex', 'justifyContent': 'center'}
        ),

        dcc.Dropdown(
            options=[
                {'label': a, 'value': a} for a in
                ['Airbus', 'Boeing', 'Ilyushin', 'Antonov', 'ALL']],
            searchable=False,
            id='company-selection',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

        dcc.Graph(figure=fig, id='graph'),

        html.Div(id='hidden-div1',
                 children='From: ',
                 style={
                     'textAlign': 'center',
                     'color': colors['text']
                 }),

        html.Div(id='hidden-div2',
                 children='To: ',
                 style={
                     'textAlign': 'center',
                     'color': colors['text']
                 }),

        # html.Label("Choose info to show:  ",
        #            style={
        #                'textAlign': 'center',
        #                'color': colors['text']
        #            }
        #            ),

        # dcc.Dropdown(
        #     id='groups-to-show',
        #     searchable=False,
        #     multi=True,
        #     options=[{'label': a, 'value': a} for a in column_groups.keys()],
        #     style={
        #         'color': colors['text']
        #     }
        # ),

        html.Label("Choose what to do:  ",
                   style={
                       'textAlign': 'center',
                       'color': colors['text']
                   }
                   ),
        dcc.Dropdown(
            id='what-to-do',
            searchable=False,
            multi=False,
            options=[{'label': el, 'value': el} for el in STAGES],
            style={
                'color': colors['text']
            }
        ),
        html.Br(),

        dcc.Checklist(
            id='default',
            options=[{'label': 'Use default values', 'value': 'Default'}],
            style={'color': 'Gold',
                   'font-size': '16'}),

        html.Br(), html.Br(),

        html.Div(id='error-div',
                 style={
                     'textAlign': 'center',
                     'color': colors['text']
                 }),
        #
        html.Label("Inputs for calculations of loan or leasing:  ",
                   style={
                       'textAlign': 'center',
                       'color': colors['text']
                   }
                   ),

        html.Br(),

        dcc.Input(
            id="s2-years",
            type='number',
            placeholder="years",
            min=0,
            max=200
        ),
        #
        dcc.Input(
            id="s2-gdeposit",
            type='number',
            placeholder="guaranteed deposit",
            min=0,
            max=100
        ),

        dcc.Input(
            id="s2-annual-rate-leasing",
            type='number',
            placeholder="annual rate leasing",
            min=0,
            max=100
        ),

        dcc.Input(
            id="s2-annual-irocm",
            type='number',
            placeholder="annual interest rate",
            min=0,
            max=100
        ),
        dcc.Dropdown(
            options=[
                {'label': a, 'value': a} for a in FINANCE_DATA.keys()],
            searchable=False,
            id='s2-country',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Label("Inputs for calculations of airport charges:  ",
                   style={
                       'textAlign': 'center',
                       'color': colors['text']
                   }
                   ),
        html.Br(),

        dcc.Input(
            id="s3-takeoff-land-maint",
            type='number',
            placeholder="take off, landing, maint fees",
            min=0,
            max=500
        ),

        dcc.Input(
            id="s3-commercial-service",
            type='number',
            placeholder="commercial service fees",
            min=0,
            max=500
        ),

        dcc.Input(
            id="s3-ground-maint",
            type='number',
            placeholder="ground maint. fees",
            min=0,
            max=500
        ),

        dcc.Input(
            id="s3-service-charge-100",
            type='number',
            placeholder="service charge per 100km",
            min=0,
            max=500
        ),

        dcc.Input(
            id="s3-landing-fees",
            type='number',
            placeholder="total landing fees",
            min=0,
            max=500
        ),

        dash_table.DataTable(
            id='calculations-results',
            sort_action='native'
        ),
    ])


@app.callback(
    [
        Output(component_id='calculations-results', component_property='data'),
        Output(component_id='calculations-results', component_property='columns'),
        Output(component_id='error-div', component_property='children'),
    ],
    [
        Input(component_id='company-selection', component_property='value'),
        Input("input_g_p_c", "value"),
        Input("input_l_i", "value"),

        Input("s2-years", "value"),
        Input("s2-country", 'value'),
        Input("s2-gdeposit", "value"),
        Input("s2-annual-rate-leasing", "value"),
        Input("s2-annual-irocm", "value"),

        Input("s3-takeoff-land-maint", "value"),
        Input("s3-commercial-service", "value"),
        Input("s3-ground-maint", "value"),
        Input("s3-service-charge-100", "value"),
        Input("s3-landing-fees", "value")
        # Input("groups-to-show", "value"),
    ]
)

def generate_results(
        aircraft_company,
        g_p_c,
        l_i,
        years,
        country,
        guaranteed_deposit,
        annual_rate_on_leasing,
        annual_interest_rate_on_capital_market,
        take_off_landing_maintenance_fees,
        commercial_service_fees,
        ground_maintenance_fees,
        service_charge_on_root_for_100_km,
        total_landing_fees):  # groups):

    if not aircraft_company or not g_p_c or not l_i:
        return dash.no_update

    to_return = info_for_company(company_to_test=aircraft_company, g_p_c=g_p_c, l_i=l_i, years=years,
                                 country=country,
                                 guaranteed_deposit=guaranteed_deposit,
                                 annual_rate_on_leasing=annual_rate_on_leasing,
                                 annual_interest_rate_on_capital_market=annual_interest_rate_on_capital_market,
                                 take_off_landing_maintenance_fees=take_off_landing_maintenance_fees,
                                 commercial_service_fees=commercial_service_fees,
                                 ground_maintenance_fees=ground_maintenance_fees,
                                 service_charge_on_root_for_100_km=service_charge_on_root_for_100_km,
                                 total_landing_fees=total_landing_fees)
    print(l_i)
    if to_return.empty:
        return None, None, 'No aircrafts with such parameters'

    # if groups:
    #     to_return = to_return[['Aircraft'] + [column for group in groups for column in column_groups[group]]]

    return to_return.to_dict('records'), [{"name": i, "id": i} for i in to_return.columns], None


@app.callback(
    Output('hidden-div1', 'children'),
    Output('hidden-div2', 'children'),
    Output('input_l_i', 'value'),
    Input('graph', 'clickData'),
    Input('hidden-div1', 'children'),
    Input('hidden-div2', 'children'),
)
def print_callback(value, info1, info2):
    if not value and info1 == 'From: ' and info2 == 'To: ':
        return dash.no_update

    city_info = f"{value['points'][0]['hovertext']}(Lon:{value['points'][0]['lon']}, Lat:{value['points'][0]['lat']})"

    if info1 == 'From: ':
        return info1 + city_info, info2, None
    elif info2 == 'To: ':
        lon1 = float(info1[info1.find('Lon:') + 4: info1.find(',')])
        lat1 = float(info1[info1.find('Lat') + 4: info1.find(')')])

        lon2 = float(city_info[city_info.find('Lon:') + 4: city_info.find(',')])
        lat2 = float(city_info[city_info.find('Lat') + 4: city_info.find(')')])

        return info1, info2 + city_info, round(distance.distance((lat1, lon1), (lat2, lon2)).km)

    return 'From: ' + city_info, 'To: ', None


@app.callback(
    [Output("s2-years", 'value'),
     Output("s2-gdeposit", 'value'),
     Output("s2-annual-rate-leasing", 'value'),
     Output("s2-annual-irocm", 'value'),
     Output("s2-country", 'value'),

     Output("s3-takeoff-land-maint", 'value'),
     Output("s3-commercial-service", 'value'),
     Output("s3-ground-maint", 'value'),
     Output("s3-service-charge-100", 'value'),
     Output("s3-landing-fees", 'value'),
     Output("input_g_p_c", 'value')],

    Input("default", 'value'),
)
def update_default_values(use_default):
    if use_default:
        return 5, 25, 30, 10, 'UKR', 20, 10, 140, 15, 15, 40
    else:
        return None, None, None, None, None, None, None, None, None, None, None


if __name__ == '__main__':
    app.run_server(debug=True)
