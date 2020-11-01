#2nd Row of graphs
#Look into plot with car on it
#change colors of plot based on car veolocity 


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors = {
    'background' : '#121212',
    'text': '#FFFFFF'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "X": [1, 2, 3, 4, 5, 6],
    "Y": [3, 4, 2, 1, 5, 7]
})

fig = px.line(df, x = "X", y = "Y", title = "Line Graph", height = 350)

fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
)
fig.update_yaxes(automargin = True)
fig.update_xaxes(automargin = True)




app.layout = html.Div( style = { 'backgroundColor': colors['background'], 'textAlign': 'center', 'color': colors['text'], 'height': '100vh', 'width': '100vw'}, children = [

    #html.Div( style = { 'backgroundColor': colors['background'], 'color': colors['text'], 'height': '10vh',}, children = [
    #    html.Div(children = [
    #        html.H3("Controls?"),
    #    ], className = 'two columns'),
    #
    #], className = 'row'),



    #Row 1
    html.Div( style = { 'backgroundColor': colors['background'], 'color': colors['text'], 'height': '45vh'}, children = [
        html.Div(style = {'borderBottom': '5px solid white', 'borderRight': '5px solid white',}, children = [
            html.H3('Graph 1'),
            dcc.Upload(
                id = 'upload-data-G1',
                children = html.Div([
                    html.P('Select a file to be shown on this graph'),
                    html.A('Select file')
                ]),
            ),
            dcc.Graph(
                id = "Graph 1", 
                figure = fig
            )
        ], className = "four columns"),

        html.Div(style = {'borderLeft': '5px solid white','borderRight': '5px solid white','borderBottom': '5px solid white',}, children = [
            html.H3('Graph 2'),
            dcc.Upload(
                id = "upload-data-G2",
                children = html.Div([
                    html.P('Select a file to be shown on this graph'),
                    html.A('Select file')
                ]),
            ),
            dcc.Graph(
                id = "Graph 2",
                figure = fig
            )
        ], className = "four columns"),

        html.Div(style = {'borderLeft': '5px solid white', 'borderBottom': '5px solid white'}, children = [
            html.H3('Graph 3'),
            dcc.Upload(
                id = "upload-data-G3",
                children = html.Div([
                    html.P('Select a file to be shown on this graph'),
                    html.A('Select file')
                ]),
            ),
            dcc.Graph(
                id = "Graph 3",
                figure = fig
            )
        ], className = "four columns"),
    ], className = "row"),

    #Row 2
    html.Div( style = { 'backgroundColor': colors['background'], 'color': colors['text'],'height': '45vh',}, children = [

        html.Div(style = {'borderRight': '5px solid white', "borderBottom": '5px solid white'}, children = [
            html.H3('Graph 4'),
            dcc.Upload(
                id = "upload-graph-G4",
                children = html.Div([
                    html.P('Select a file to be shown on this graph'),
                    html.A('Select file'),
                ]),
            ),
            dcc.Graph(
                id = "Graph 4",
                figure = fig,
            )
        ], className = "four columns"),
        html.Div(style = {'borderLeft': '5px solid white','borderRight': '5px solid white','borderBottom': '5px solid white',}, children = [
            html.H3('Graph 5'),
            dcc.Upload(
                id = "upload-graph-G5",
                children = html.Div([
                    html.P('Select a file to be shown on this graph'),
                    html.A('Select file'),
                ]),
            ),
            dcc.Graph(
                id = "Graph 5",
                figure = fig,
            )
        ], className = "four columns"),
        html.Div( style = {'borderLeft': '5px solid white', 'borderBottom': '5px solid white'}, children = [
            html.H3('Graph 6'),
            dcc.Upload(
                id = "upload-graph-G6",
                children = html.Div([
                    html.P('Select a file to be shown on this graph'),
                    html.A('Select file'),
                ]),
            ),
            dcc.Graph(
                id = "Graph 6",
                figure = fig,
            )
        ], className = "four columns"),
    ], className = "row"),
], className = "twelve columns")





if __name__ == '__main__':
    app.run_server(debug=True)