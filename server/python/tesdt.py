
import locale
from matplotlib.pyplot import text
import pandas as pd
import numpy as np
import dash                     #(version 1.0.0)
import dash_table
import dash_core_components as dcc

import dash_html_components as html
from dash.dependencies import Input, Output, State
import pprint


import plotly.offline as py     #(version 4.4.1)
import plotly.graph_objs as go

from firebase import Auth, Firebase



# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask_cors import CORS
from flask import Flask, redirect, url_for, request

 
# Flask constructor takes the name of
# current module (__name__) as argument.
flask_app = Flask(__name__)
CORS(flask_app)

 
data_updated_table = "hej"
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


# main driver function


config = {
  "apiKey": "AIzaSyDLxaaJgllch4UfzsMApfRMjX1HVtwhdyk",
  "authDomain": "test-api-4e6bf.firebaseapp.com",
  "databaseURL": "https://test-api-4e6bf-default-rtdb.europe-west1.firebasedatabase.app",
  "storageBucket": "test-api-4e6bf.appspot.com",

}



firebase = Firebase(config)

db = firebase.database()

mapbox_access_token= 'pk.eyJ1IjoicGx1Z2drb2xsIiwiYSI6ImNrbDhjMXFxbDJyYm8ybmxidjc1cDQ0MTIifQ.70M-epXA36GR8LVOQ64ZTg'

# mapbox_access_token = 'insert_your_mapbox_token_here'
# mapbox_access_token = 'insert_your_mapbox_token_here'



# df = pd.read_csv("finalrecycling.csv")

#So we can have icons
FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"

app = dash.Dash(__name__,meta_tags=[{'name': 'viewport',
                            'content': 'initial-scale=0.9'}], 
                external_stylesheets=[FA], server=flask_app, routes_pathname_prefix="/dash/")

blackbold={'color':'black', 'font-weight': 'bold'}

#app.css.append_css({'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'})


df = pd.DataFrame(
    {"labels": ["Kurs", "Kurskod", "Betyg", "Poäng"],}
)

initial_active_cell = {"row":0, "column":0}
#Här lacerar vi alla dic/element på webbsidan

app.layout = html.Div([

    dash_table.DataTable(
        id='adding-rows-table',
        columns=[{
            'name': df["labels"][i],
            'id': 'column-{}'.format(i),
            'deletable': False,
            'renamable': False,
            'clearable':True,
        } for i in range(0, 4)],
        data=[
            {'column-{}'.format(i): "" for i in range(1, 5)}
            for j in range(5)
        ],
        editable=True,
        export_format='xlsx',
        export_headers='display',
        merge_duplicate_headers=False,
        row_deletable=True,
        active_cell= initial_active_cell,
        sort_action='native',
        sort_mode='multi',
        sort_by=[{'direction': 'asc'}]
    ),

    html.Button('Add Row', id='editing-rows-button', n_clicks=0),
    html.Button('DELETE', id='delete-button', n_clicks=0),
    html.Div(id='datatable-interactivity-container'),
])


@app.callback(
    Output('adding-rows-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns'))
def add_row(n_clicks, rows, columns):
    print(rows)
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows


@app.callback(
    Output('adding-rows-table', 'columns'),
    Input('adding-rows-button', 'n_clicks'),
    State('adding-rows-name', 'value'),
    State('adding-rows-table', 'columns'))
def update_columns(n_clicks, value, existing_columns):
    if n_clicks > 0:
        existing_columns.append({
            'id': value, 'name': value,
            'renamable': True, 'deletable': True
        })
    return existing_columns

#--------------------------------------------------------------------------------------------------------------------------------------

@app.callback(Output('adding-rows-table', 'children'), Input('adding-rows-table', 'active_cell'),
Input('adding-rows-table', 'derived_virtual_data'))
def update_graphs(active_cell, derived_virtual_data):
    row_index = derived_virtual_data
    col_index = str(active_cell["column"])
    data_table = derived_virtual_data

    # for row in data_table:
    #     if "column1" in row:
    #         print(row["column1"])
    #         print("---------------------------")

    for row in data_table:
     for col in row:
        print(col)
        print("---------------------------")

    # if "column1" in data_table:
    #     print("COLUMN 1: !!!!!!!!!!!!!!!!", data_table["column1"])

    data_updated_table = data_table
    # for row in data_table:
    #     print(row)
    #     print("---------------")
        # print(row["column1"], row["column3"], row["column4"])
        # if row["column1"] != None:
        #     print(row)
        #     print("-------------------------")
    # row_index = pd.DataFrame(data=derived_virtual_data)
    # db.child("tables/").set(data_table)
    return data_updated_table

@flask_app.route('/', methods = ['GET', 'POST']) #The order GET, POST is Important, not POST, GET
def check():
    if request.method == 'POST':
       jsonData = request.get_json()
       uid = jsonData["uid"]
       db.child("users/").child(uid).child("BASJ FRÅN DAQSH").set(data_updated_table)
    

    return "hi"


@app.callback(
    Output('datatable-interactivity-container', "children"),
    Input('adding-rows-table', "derived_virtual_data"),
    Input('adding-rows-table', 'active_cell'),
    Input('adding-rows-table', "derived_virtual_selected_rows"))
def update_graphs(rows, active_cell,derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    print(active_cell)
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)
    # print(type(dff["column-0"].to_frame()))
    # print("HÄR")
    # print(dff["column-0"].tolist())
    
    course_name = dff["column-0"].tolist()
    grades = dff["column-2"].tolist()
    credits = dff["column-3"].tolist()

    new_df = pd.DataFrame(list(zip(course_name, grades,credits)),
               columns =['Kurs', 'Betyg',"Poäng"])

    bajs = {
        "Kurs":course_name,
        "Betyg":grades,
        "Poäng": credits
    }

    db.child("users/").child("Betyg").set(bajs)

    print("---------------")
    # print(dff["column-1"])
    # print("---------------")
    # print(dff["column-2"])
    # print("---------------")
    # print(dff["column-3"])
    # print("---------------")
    # print(dff["column-4"])

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]


    for grade in dff.index:
        if dff["column-2"][grade] == "MVG" or dff["column-2"][grade] == "A":
            dff["column-2"][grade] = 20
        
        if dff["column-2"][grade] == "B":
            dff["column-2"][grade] = 17.5

        if dff["column-2"][grade] == "VG" or dff["column-2"][grade] == "C":
            dff["column-2"][grade] = 15
        
        if dff["column-2"][grade] == "D":
            dff["column-2"][grade] = 12.5
        
        if dff["column-2"][grade] == "E" or dff["column-2"][grade] == "G":
            dff["column-2"][grade] = 10

        if dff["column-2"][grade] == "IG" or dff["column-2"][grade] == "F":
            dff["column-2"][grade] = 0


    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["column-0"],
                        "y": dff["column-2"],
                        "type": "bar",
                        "marker": {"color": colors},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": column}
                    },
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ["column-3"] if column in dff
    ]



# # ‘/’ URL is bound with hello_world() function.
# def Hello():
#     return data_updated_table
   
    
    

if __name__ == '__main__':
    app.run_server(debug=False)


    
# if __name__ == '__main__':
#     flask_app.run_server(debug=False)





























if __name__ == '__main__':
    app.run_server(debug=True)
