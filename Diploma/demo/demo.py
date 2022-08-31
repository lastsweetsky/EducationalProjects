# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash import Dash, dash_table
from geopy import distance

from Diploma.calculations.calculations import info_for_company

import plotly.express as px
import geopandas as gpd

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

fig = px.scatter_geo(geo_df,
                     lat=geo_df.geometry.y,
                     lon=geo_df.geometry.x,
                     hover_name="name")

column_groups = {
    'Flight info': ['Productivity',
                    'Productivity to ideal',
                    'Fuel burnt per flight',
                    'Fuel economy to ideal',
                    'Flight cost',
                    'Ecost for trasnp 1 unit'],
    'Leasing info': ['Cost under loan',
                     'Cost under leasing',
                     'Residual leasing value'],
    'Charges': ['Airport charges',
                'Route service fees',
                'Air navigation charges']
}

app = Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

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
                'color': colors['text']
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
        # html.Div(
        #     [
        #         html.Label("Input weight of cargo in tons: ",
        #                    style={
        #                        'textAlign': 'center',
        #                        'color': colors['text']
        #                    }
        #                    ),
        #         dcc.Input(id="input_g_p_c",
        #                   type='number',
        #                   placeholder="Weight of cargo",
        #                   min=0,
        #                   max=10000
        #                   ),
        #
        #         html.Label("Input length of flight: ",
        #                    style={
        #                        'textAlign': 'center',
        #                        'color': colors['text']
        #                    }
        #                    ),
        #         dcc.Input(id="input_l_i",
        #                   type='number',
        #                   placeholder="Length of route",
        #                   min=0,
        #                   max=50000
        #                   ),
        #
        #         html.Label("Choose info to show:  ",
        #                    style={
        #                        'textAlign': 'center',
        #                        'color': colors['text']
        #                    }
        #                    ),
        #         dcc.Dropdown(
        #             id='groups-to-show',
        #             searchable=False,
        #             multi=True,
        #             options=[{'label': a, 'value': a} for a in column_groups.keys()],
        #             style={
        #                 'color': colors['text']
        #             }
        #         )
        #
        #     ], style={'display': 'flex', 'justifyContent': 'center'}
        # ),

        # dcc.Dropdown(
        #     options=[
        #         {'label': a, 'value': a} for a in
        #         ['Airbus', 'Boeing', 'Ilyushin', 'Antonov', 'ALL']],
        #     searchable=False,
        #     id='company-selection',
        #     style={
        #         'textAlign': 'center',
        #         'color': colors['text']
        #     }),
        #
        # dash_table.DataTable(
        #     id='calculations-results',
        #     sort_action='native'
        # )
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
        html.Div(id='hidden-div3',
                 children='',
                 style={
                     'textAlign': 'center',
                     'color': colors['text']
                 })
    ])


# @app.callback(
#     Output(component_id='calculations-results', component_property='data'),
#     Output(component_id='calculations-results', component_property='columns'),
#     Input(component_id='company-selection', component_property='value'),
#     Input("input_g_p_c", "value"),
#     Input("input_l_i", "value"),
#     Input("groups-to-show", "value"),
# )
# def generate_results(aircraft_company, g_p_c, l_i, groups):
#     if not aircraft_company or not g_p_c or not l_i:
#         return dash.no_update
#
#     to_return = info_for_company(aircraft_company, g_p_c, l_i)
#
#     if groups:
#         to_return = to_return[['Aircraft'] + [column for group in groups for column in column_groups[group]]]
#
#     return to_return.to_dict('records'), [{"name": i, "id": i} for i in to_return.columns]


@app.callback(
    Output('hidden-div1', 'children'),
    Output('hidden-div2', 'children'),
    Output('hidden-div3', 'children'),
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

        lon1 = float(info1[info1.find('Lon') + 4: info1.find(',')])
        lat1 = float(info1[info1.find('Lat') + 4: info1.find(')')])

        lon2 = float(city_info[city_info.find('Lon') + 4: city_info.find(',')])
        lat2 = float(city_info[city_info.find('Lat') + 4: city_info.find(')')])

        return info1, info2 + city_info, f'Distance: {distance.distance((lat1, lon1), (lat2, lon2)).km}'

    return 'From: ' + city_info, 'To: ', None


if __name__ == '__main__':
    app.run_server(debug=True)
