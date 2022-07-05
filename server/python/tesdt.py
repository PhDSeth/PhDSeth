
import locale
from matplotlib.pyplot import text
import pandas as pd
import numpy as np
import dash                     #(version 1.0.0)
import dash_table as dt
import dash_core_components as dcc

import dash_html_components as html
from dash.dependencies import Input, Output, State
import pprint


import plotly.offline as py     #(version 4.4.1)
import plotly.graph_objs as go

from firebase import Auth, Firebase


# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask_cors import CORS, cross_origin
from flask import Flask, redirect, url_for, request, session
from flask_session import Session
from flask_caching import Cache
import os
from datetime import timedelta

from scipy.fftpack import diff
# Flask constructor takes the name of
# current module (__name__) as argument.
flask_app = Flask(__name__)
flask_app.secret_key = 'v&7yhgbdn_fdfefkdjhdui' #Session needs it. We cannot erase a session, if we want we can change the key to 
 #Session needs it. We cannot erase a session, if we want we can change the key to 
#reset the session key
flask_app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 7)
# flask_app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=False)
flask_app.config['SESSION_TYPE']='filesystem'
Session(flask_app)
CORS(flask_app,supports_credentials=True)





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

df = pd.DataFrame(
            {"labels": ["Kurs", "Kurskod", "Betyg", "Poäng"],}
        )

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




#---------------------------------------------------ORDINARY FUNCTIONS----------------------------
def create_map():
#Check first if logged in and authoirized
    schools = db.child("schoolsContactInfo/").get()
    coordinates_all = []
    cities = []

    i = 0
    for school in schools.each():
        if i < 2:
            coord = []
            contact_json = school.val()
            coordinate = contact_json["coordinates"]
            lat = coordinate["lat"]
            long = coordinate["long"]
            coord.append(lat)
            coord.append(long)
            coordinates_all.append(coord)

            city = contact_json["visitAdress"]["town"]
            cities.append(city)
        


            i +=1
    print(cities)
    print(coordinates_all)
    data = {"city":cities, "coord":coordinates_all}
    df = pd.DataFrame(data)
    
    return df

df_map = create_map()
#----------------------------------------------END ON     ORDINARY FUNCTIONS-----------------------

initial_active_cell = {"row":0, "column":0}
#Här lacerar vi alla dic/element på webbsidan


app.layout = html.Div([
    dcc.Interval(id="interval-db", interval=50000000*7, n_intervals=0),
    dcc.Location(id='url'),
    html.Div(id="tables", children = []),
    html.Button('Lägg till ny rad', id='editing-rows-button', n_clicks=0),
    html.Button('Radera tabell', id='delete-button', n_clicks=0),
    html.Div(id='datatable-interactivity-container'),
    dcc.Store(id='store-data', storage_type='memory')
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



#Every signed in user have a set session with uid
@flask_app.route('/register_activity', methods =['GET','POST'])
@cross_origin(supports_credentials=True)
def register():

    session['from_db'] = False
    #Check if the user has been registered earlier
    # uid = jsonData["uid"]
    # if db.child("users/").child("ggg").get().val() != None: #if the user exists
    print("SESSION INNAN",session)
    jsonData = request.get_json()
    print(jsonData)

    # uid = jsonData["uid"]
    session['uid'] = jsonData["uid"]
    session['loggedIn'] = True

    if db.child("users/").child(jsonData["uid"]).get().val() == None: #not existing in database
        db.child("users/").child(jsonData["uid"]).set(jsonData)


    #If the user has not previously added their grades set se   
    #session["grade-dash-table"] = False
    if db.child("users/").child(jsonData["uid"]).child("Betyg").get().val() == None: #first time 
        session["grade-dash-table"] = False
    else:
        session["grade-dash-table"] = True
    
    #A newly registered user should have their sessio[grade-dash-table] == False
    #before they have added their grades
    print("SESSION EFTER",session)

    return "hej"

#Session is a live here, so we can use that
@flask_app.route('/delete_account',  methods = ['GET'])
@cross_origin(supports_credentials=True)
def delete():
    uid =  session.get('uid')
    #Fixa till...
    db.child("users/").child(uid).set(None)

    return "200"



@flask_app.route('/hej', methods = ['GET','POST']) #The order GET, POST is Important, not POST, GET
@cross_origin(supports_credentials=True)
def check():
    jsonData = request.get_json()
    print("jsonData", jsonData)
    uid = jsonData["uid"]
    session['uid'] = uid


    print(session)
    if session['uid'] != uid:
        session['uid'] = uid
        print(session)
      
    else:
        print("redan satt")
        # session.clear()
    
    #should propably retrn 200 or something
    return session['uid']


@flask_app.route('/logout',) #The order GET, POST is Important, not POST, GET
# @cross_origin(supports_credentials=True)
def logout():

    session['from_db'] = False
    session['loggedIn'] = False
    session["grade-dash-table"] = False
    print("Logga ut", session)
    return "hej"


#Every time we refresh the app, this function is triggered
@app.callback(Output('tables','children'),
Input('interval-db', 'n_intervals'),
Input('delete-button', 'n_clicks'))
def update_graphs(url, n_clicks):
    df = pd.DataFrame(
            {"labels": ["Kurs", "Kurskod", "Betyg", "Poäng"],}
        )
    
    # print(url)
    if  session.get('loggedIn') == True and db.child("users/").child(session["uid"]).child("Betyg").get().val() != None:
        print("VÅR NYA")
        data_db = db.child("users/").child(session["uid"]).child("Betyg").get()
        row_grades = []
        row_courses = []
        row_codes = []
        row_points = []

        for obj in data_db.each():

            print(obj.key()) #Biologi - breddning
            print(obj.val()) #{'Betyg': 'VG', 'Kursnamn': 'Biologi - breddning', 'Poäng': '50'}
            row_grades.append(obj.val()["Betyg"])
            row_courses.append(obj.val()["Kursnamn"])
            row_codes.append(obj.val()["Kurskod"])
            row_points.append(obj.val()["Poäng"])


        my_data = {
            "column-0": row_courses,
            "column-2":row_grades,
            "column-3": row_points,
            "column-1":row_codes
        }
            # for key in course_dict.keys():
            #     value_row = course_dict.values()
            #     print(value_row)#dict_values(['VG', 'BI1203', 'Biologi - breddning', '50'])
            #     for i in value_row:
            #         # rows.append(i)
            #         print(i)
 
        my_data = pd.DataFrame(data=my_data)

        print(my_data)


        return [ 
            dt.DataTable(
            id='adding-rows-table',
            columns=[{
                'name': df["labels"][i],
                'id': 'column-{}'.format(i),
                'deletable': False,
                'renamable': False,
                'clearable':True,
            } for i in range(0, 4)],
            data=my_data.to_dict('records'),
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
        ]

    elif n_clicks >= 1:
        return[

        dt.DataTable(
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
        ),]
    
    else:
        return[

        dt.DataTable(
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
        ),]

        




#This callback fires when we change data
#returns a graph
@app.callback(
    Output('datatable-interactivity-container','children'),
    # Output('adding-rows-table', "data"),
    Input('adding-rows-table', 'derived_virtual_data'),
    Input('adding-rows-table', 'active_cell'),
    # State('adding-rows-table', 'active_cell'),s
    Input("store-data", "data"),

    #STATE DOESNT TRIGGER CALLBACK, ONLY INPUT DOES
    State('adding-rows-table', "derived_virtual_selected_rows"),
    State('adding-rows-table', "derived_virtual_data"))
# @cross_origin(supports_credentials=True)
def update_graphs(rows,active_cell,coord,derived_virtual_selected_rows,derived_virtual_data):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.

    #if the user have alrdy entered grades


    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    
    print(derived_virtual_data)

    dff = df if rows is None else pd.DataFrame(rows)
    dff= dff.replace(np.nan,"")
    print("....................")
    print(dff)
    print("....................")

    #Empty cell is == None
    #If we erase a column, that column disapears from df
    if "column-0" not in dff:
        print("0 saknas")
        dff["column-0"] = ""
    
    if "column-1" not in dff: #dont use "elif", use if, otherwise they will not be evaluated
        print("1 saknas")
        dff["column-1"] = ""
    
    if "column-2" not in dff:
        print("2 saknas")
        dff["column-2"] = ""

    if "column-3" not in dff:
        print("3 saknas")
        dff["column-3"] = ""
 
    print(dff)
    course_name = dff["column-0"].tolist()
    code = dff["column-1"].tolist()
    grades = dff["column-2"].tolist()
    credits = dff["column-3"].tolist()

    i = 0
    for c in course_name:
        if i > len(course_name):
            i = 0
        
        
        my_data = {
            "Kursnamn": c,
            "Betyg":grades[i],
            "Poäng": credits[i],
            "Kurskod":code[i]
        }
        
        # if c != "" or c != None:
            #we need to update the previous
        db.child("users/").child(session["uid"]).child("Betyg").child(c).set(my_data)
            
        i += 1

    #This sections is required to update the database and to ensure that the database is up to date with the
    #dash-table
    all_objects = db.child("users/").child(session["uid"]).child("Betyg").get()
    for obj in all_objects.each():
                #If the updated cours in data table does not include a particular course in firebase, remove this
                #from firebase
 
        if obj.key() not in list(dff["column-0"]):
            print(obj.key(), "not in course name")
            db.child("users/").child(session["uid"]).child("Betyg").child(obj.key()).remove()
    print("...................................")
    session["grade-dash-table"] = True
    # derived_virtual_selected_rows = dff   

    #the data_table changes when the user interacts with the table
   

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
        for column in ["column-0"] if column in dff
    ]




# # ‘/’ URL is bound with hello_world() function.
# def Hello():
#     return data_updated_table
if __name__ == '__main__':
    app.run_server(debug=False)

