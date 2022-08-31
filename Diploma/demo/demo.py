# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash import Dash

from Diploma.calculations.calculations import info_for_company


app = Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.P(children="✈️",
           className="header-emoji",
           style={
               'textAlign': 'center'
           }),

    html.H1(
        children= "Diploma",
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

    html.Div(
        [
            html.Label("Input weight of cargo in tons: ",
                       style={
                           'textAlign': 'center',
                           'color': colors['text']
                       }),
            html.Br(),
            dcc.Input(id="input_g_p_c",
                      type='number',
                      placeholder="Weight of cargo",
                      min = 0,
                      max = 10000
                      ),

        ],
    style = {'display' : 'flex', 'justifyContent' : 'center' }
    ),
    html.Hr(),

    dcc.Dropdown(
        options=[
            {'label': a, 'value': a} for a in
            ['Airbus', 'Boeing', 'Ilyushin', 'Antonov']],
        searchable=False,
        id='company-selection',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(id='calculations-results',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             })

])


@app.callback(
    Output(component_id='calculations-results', component_property='children'),
    Input("input_g_p_c", "value"),
    Input(component_id='company-selection', component_property='value')
)
def generate_results(aircraft_company, g_p_c):
    if not aircraft_company or not g_p_c:
        return dash.no_update

    return info_for_company(aircraft_company, g_p_c)


if __name__ == '__main__':
    app.run_server(debug=True)
