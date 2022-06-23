
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
app.layout = html.Div(style={'backgroundColor':'white'}, children=[
#---------------------------------------------------------------
    html.Div([

        html.Div([
                 html.Div([
               
                    
                    html.Button('Radera tabell', id='delete-button', n_clicks=0)
                ], style={'height': 50}),

                 dash_table.DataTable(
                     #Vi behöver ett ID för att kunna kalla i @Callback
                    id='table',
                    columns=[{'name': df["labels"][0],'id': 'column1', 'clearable':True,},
                            {'name': df["labels"][1],'id': 'column2', 'clearable':True,},
                            {'name': df["labels"][2],'id': 'column3', 'clearable':True,},
                            {'name': df["labels"][3],'id': 'column4', 'clearable':True,},
                            # {'name': df["labels"][3],'id': 'column4', 'deletable': True,'renamable': True,'clearable':True,},
                    ], 
                    data=[
                        {'column-{}'.format(i): df.to_dict() for i in range(1, 5)}
                        for j in range(6)
                        ],
                    editable=True,
                    export_format='xlsx',
                    export_headers='display',
                    merge_duplicate_headers=False,
                    row_deletable=True,
                    active_cell= initial_active_cell,
                 
                    #column_deletable=True
    
                ),
                #html.Div(dcc.Input(id='input-on-submit', type='text')),
                html.Button('Beräkna mina betyg', id='submit-val', n_clicks=0),        
                html.Div(id='editing-prune-data-output')
                ]),

                
    ], className='row'),


], className='ten columns offset-by-one')


#This is needed in ordet for the update_columns function to run
@app.callback( 
    Output('editing-columns', 'columns'),
    Output('editing-columns', 'value'),
    Input('editing-columns-button', 'n_clicks'),#columns is passed as paramter 1 below
    State('editing-columns-name', 'value'),#columns is passed as paramter 2 below
    State('editing-columns', 'columns')) #columns is passed as paramter 3 below


#After every callback, we need a function. The parameters to the function (3) must
#be equal to the number of Input and state in callback
#This fucntions runs every time the table loads, or the table changes
def update_columns(n_clicks, value, existing_columns):

    if n_clicks > 0:
        existing_columns.append({
            'id': value, 'name': value,
            'renamable': True, 'deletable': True
        })
    return existing_columns, value #The thing we return is equal to the otput in above callback



@app.callback(Output('table', 'children'), Input('table', 'active_cell'),
Input('table', 'derived_virtual_data'))
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
       db.child("users/").child(uid).child("Data från flask/dash").set(data_updated_table)
    

    return "hi"



@app.callback(
    Output('table', 'data'),
    [Input('delete-button', 'n_clicks')]
)
def delete_table_data(n_clicks):
    if n_clicks == 0:
        raise dash.exceptions.PreventUpdate()
    data = pd.DataFrame().to_dict("bajs")  #empty dataframe
    return data

        



# # ‘/’ URL is bound with hello_world() function.
# def Hello():
#     return data_updated_table
   
    
    

if __name__ == '__main__':
    app.run_server(debug=False)


    
# if __name__ == '__main__':
#     flask_app.run_server(debug=False)


