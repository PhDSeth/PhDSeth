
import locale
from matplotlib.pyplot import text
import pandas as pd
import numpy as np
import dash  
from dash import no_update                   #(version 1.0.0)
import dash_table as dt
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
from data_for_training import traning_data_courses

from calculations import norm_grade, calc_grade_diff, grade, calc_grade, remove_HighestGrades, what_to_focus_on, bayes, return_d
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pprint
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem.lancaster import LancasterStemmer
from numpy.core.fromnumeric import shape
from nltk.stem import SnowballStemmer
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn import preprocessing #convert text to numerical inputs
import pandas as pd
import numpy as np
from itertools import chain
import mplcursors
import json 
from prerequisite_courses import pre_edu, prerequisite_data
import nltk
from educationData import education_data_engineering
from educationData import education_data_health
from educationData import education_data_social


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

# word stemmer
stemmer = SnowballStemmer("swedish")
#stemmer = LancasterStemmer()
nltk.download('punkt')



training_data = traning_data_courses()
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
            {"labels": ["Kurs", "Kurskod", "Betyg", "Storlek"],}
        )

    
grade_and_their_score_dict= {
  'Betyg': ['MVG', 'VG', 'G', 'IG', 'A', 'B', 'C', 'D', 'E', 'F'],
  'Score': [ 20,   15,    10,   0, 20, 17.5, 15,  12.5, 10,  0] 
}

grade_and_their_score_dict_df = pd.DataFrame(data=grade_and_their_score_dict)

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


#
#
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
    data = {"city":cities, "coord":coordinates_all}
    df = pd.DataFrame(data)
    
    return df

df_map = create_map()


def blank_fig():
    fig = go.Figure(go.Scatter(x=[], y = []))
    fig.update_layout(template = None)
    fig.update_xaxes(showgrid = False, showticklabels = False, zeroline=False)
    fig.update_yaxes(showgrid = False, showticklabels = False, zeroline=False)
    
    return fig


#From dict to dataframe
#Convert grades from dash table to dataframe
def d_to_df(d):
    courses = pd.DataFrame(data =d)
    return courses
#------------------------------------------------------------------------------------------------------------------------
#Output: A dict with classes and corresponding words that belongs to each class. Based on our traning data
#Ex: {'naturvetenskap' : ['fysik, matematik, biologi]}
def tokenize_stem_trainingData():

    # capture unique stemmed words in the training corpus
    #corpus_words = {}
    class_words_training_data = {}
    index = 0
    # turn a list into a set (of unique items) and then a list again (this removes duplicates)
    #Classes is the names of every unique class we have identified in our grade
    classes = list(set([a['class'] for a in training_data]))
    for c in classes:
        # prepare a list of words within each class
        class_words_training_data[c] = []
        # loop through each sentence in our training data
        #Training data conains all data, where data is one line class: blabla, word: blabla

    for data in training_data:
        
        if 'breddning' in data['word'] or 'specialisering' in data['word'] or '5' in data['word'] or '4' in data['word'] or '3' in data['word'] or '2' in data['word']:
            #APPEND insert a word as a ONE, for exmpale "biologi" is added as "biologi", while EXTEND will add "b","i","o","l","o","g","i"
            # print('tr??ningsdata', data)
            # time.sleep(2)
            class_words_training_data[data['class']].append(data['word'])
        
        else:
            # tokenize each sentence in our traning data into words
            #For example: "matematik specialisering" => "matematik", "specialisering"
            for word in nltk.word_tokenize(data['word']):  
                # stem and lowercase each word
                stemmed_word = stemmer.stem(word.lower())
                # print('word in tokenized wordk',  word)
                # time.sleep(2)
                # print('stemmed',  stemmed_word)
                # time.sleep(2)
                # have we not seen this word already?
                #if stemmed_word not in corpus_words:
                #corpus_words[stemmed_word] = 1
                #corpus_words[stemmed_word] += 1
                # add the word to our words in class list
                class_words_training_data[data['class']].extend([stemmed_word])
    return class_words_training_data

    #------------------------------------------------------------------------------------------------------------------------
    #A function that returns each class with corresponding scores. Summarizes all class scores. 
    #Input: A collected_all_list, eg a list with courses and their correspodning score and class
    #Input: a dict, class|score|course fr??n collect_all_list funktionen
    #        milj??| 0,6 | Biologi A
    #Output: Klass | Nbr of courses | Averg. score | Included courses ()
    #Summerar alla kurser som tillh??r en speciell klass. 
    #Can be used to list all courses within a given class.
def summarize_class_scores(dic):
    pd.set_option('display.max_colwidth', None)
    courses_with_scores = pd.DataFrame({
    'Klass: ': [],
    'Score: ': [],
    'Nbr of courses: ': [],
    #Eftersom po??ngen inom varje klasss ??r eorende av antalet kurser (och inte enbart betygen) s?? beh??ver vi r??kna ut ett snitt f??r varje klass.
    'Averg. score: ': [],
    'Included courses ': [],
    })
    
    #Will be the same length as the number of classes
    klass = []
    #Will be the same length as the number of classes
    scores = []
    averg_score =[]
    nbr_of_courses =[]
    #Inlcuded_courses is a list that will contain lists (courses), => A list of lists
    included_courses = []

    for ind in dic.index:
        #For each unique class. Keeps track of which array to fill in duplicates
        if dic['Klass'][ind] not in klass:
            klass.append(dic['Klass'][ind])
            scores.append(dic['Score'][ind])
            nbr_of_courses.append(1)
            averg_score.append(dic['Score'][ind])
            courses = [dic['Kurs'][ind]]
            included_courses.append(courses)

        else:
            #If the class alrdy existe within the list, add the scores to the end of the score list
            #Get the index where the first class is laying
            class_index = klass.index(dic['Klass'][ind])
        
            #Get index where course should be inserted
            #The new score equals the old score + the new one. The index is the same as the index for the class
            new_score = scores[class_index] + dic['Score'][ind]
            #Update the class score
            scores[class_index] = new_score
            averg_score[class_index] = new_score
            nbr_of_courses[class_index] =  nbr_of_courses[class_index] +1 
            averg_score[class_index] = new_score/nbr_of_courses[class_index]
            #use append, since included_courses is a list of lists
            if dic['Kurs'][ind] not in included_courses:
                included_courses[class_index].append(dic['Kurs'][ind])

    #print("COURSE DATA-----------", course_data)
    courses_with_scores['Klass'] = klass
    courses_with_scores['Score'] = scores
    courses_with_scores['Nbr of courses'] = nbr_of_courses
    courses_with_scores['Averg. score'] =  averg_score
    courses_with_scores['Included courses'] =  included_courses
    courses_with_scores.dropna(how='all', axis=1, inplace=True) 

    return courses_with_scores
    #print(courses_with_scores)

#--------------------------------------------------------------------------------------------------


def qualification(df, your_grade):

  d = return_d(your_grade)
#   print(d["Kurs"])
#   import time
#   time.sleep(100)

  #En lista d??r vi l??gger in alla v??ra beh??righeter. Ex [A1, A2, A3].
  qual_list = []
  ind = -1
#   inner_counter = 0
  counter_to_fullfull = 0
  import time
  
  for courses in df['Kurser']: 
    counter_to_fullfull = 0
    ind +=1  #    courses =  "Kurser" : [ ["Fysik B"], ["kemi A"], ["Matematik D"] ], 'Education':["H??gskoleingenj??r", "Ortopedingenj??r"]})
    # df["Kurser] =     
    #in order for someone to fullfill this beh??righet, we need a counter. The counter must me equal to the lenght of courses, in the example above counter = 4
    print("courses", courses)
    print("len courses", len(courses))
    print("-------")
    
    for course in courses:#   course = #ONLY ONE COURSE MUST BE FULLFILLED
        # course = ["Fysik B"] 
        # course = ["fysikA A", "Kemi A", "Biologi A"]
        print("course", course)
        inner_counter = 0


        #Det r??cker att minst 1 av kurserna ??terfinns
        #count ar bara ett argument
        # i ??r av typen "list", kan vara nestlade listor
        for i in course: # 
            print("i",i)
            print("len course", len(course))

            # print(i.lower())
            # print("-----")
            # print(d["Kurs"])
            # time.sleep(5)
            if i.lower() in list(d["Kurs"]): #If the course exist in our grades
                print("Inne")
                inner_counter += 1
                print("inner_counter", inner_counter)

                if inner_counter >= len(course):
                    counter_to_fullfull += 1
                    print("counter_to_fullfull", counter_to_fullfull)
                    # print("counter_to_fullfull",counter_to_fullfull)

        if counter_to_fullfull >= len(courses):
            #Beh??righet upfylls
            qual_list.append(df["Omr??desbeh??righet"][ind])
            counter_to_fullfull = 0
            print("Du uppfyller kraven f??r:", qual_list)


    
    # return qual_list















education_class_dataFrame1 = education_data_engineering.create_engi()
education_class_dataFrame2 = education_data_health.create_health()
education_class_dataFrame3 = education_data_social.create_social()
frames = [education_class_dataFrame1, education_class_dataFrame2,education_class_dataFrame3]
education_class_dataFrame= pd.concat(frames, ignore_index=True)

education_class_dataFrame = pd.DataFrame(data=education_class_dataFrame)


def lower_case_Education_df():


  return education_class_dataFrame

education_class_dataFrame = lower_case_Education_df()









#--------------END ORDINARY FUNCTIONS---------------------






initial_active_cell = {"row":0, "column":0}
#H??r lacerar vi alla dic/element p?? webbsidan

default_fig_1 = go.Figure(
    data=[go.Bar(y=[0, 0, 0,0,0,0])],
    layout_title_text="Fyll i dina betyg ovan..."
)


default_fig_2 = go.Figure(
    data=[go.Bar(y=[0, 0, 0,0,0,0])],
    layout_title_text="Fyll i dina betyg ovan..."
)

app.layout = html.Div([
    dcc.Interval(id="interval-db", interval=50000000*7, n_intervals=0),
    dcc.Location(id='url'),
    html.Div(id="tables", children = []),
    html.Button('L??gg till ny rad', id='editing-rows-button', n_clicks=0),
    html.Button('Radera tabell', id='delete-button', n_clicks=0),
    html.Div([
            html.H1(children='Din betygsf??rdelning'),
            dcc.Loading(children=[
                html.Div(id='datatable-interactivity-container'),
                dcc.Graph(
                id='graph-classes',
                figure = default_fig_1,
            ),

                dcc.Graph(
                id='graph-classes-grade-occurence',
                figure = {},
            ),  


            ], type ="graph"),



            html.H1(children='Ditt betyg'),
            html.Div(id="your_grade", children=[]),

            html.Div([
            html.H1(children='ANTAL BETYG'),
            html.Div(id="nbr_grades", children=[]),
            html.Div(id="qual-list", children=[])

            ]),
        ], className='six columns'),
    html.Button('Matcha mot utbildning', id='match-edu-button', n_clicks=0),
    html.Div(id="match-edu-div", children=[]),
    # html.Div(id='datatable-interactivity-container2'),
    dcc.Store(id='store-data', storage_type='local')
])


@app.callback(
    Output('adding-rows-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns'))
def add_row(n_clicks, rows, columns):
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
    session["times-page-refreshed"] = 0
    session['from_db'] = False
    session["grade-dash-table"] = False
    session["page-refreshed"] = False
    #Check if the user has been registered earlier
    # uid = jsonData["uid"]
    # if db.child("users/").child("ggg").get().val() != None: #if the user exists
    # print("SESSION INNAN",session)
    jsonData = request.get_json()
    # print(jsonData)

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
    # print("SESSION EFTER",session)

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
    # print("jsonData", jsonData)
    uid = jsonData["uid"]
    session['uid'] = uid


    # print(session)
    if session['uid'] != uid:
        session['uid'] = uid
        # print(session)
      
    else:
        print("redan satt")
        # session.clear()
    
    #should propably retrn 200 or something
    return session['uid']


@flask_app.route('/logout',) #The order GET, POST is Important, not POST, GET
# @cross_origin(supports_credentials=True)
def logout():

    session["page-refreshed"] = False
    session['from_db'] = False
    session['loggedIn'] = False
    session["grade-dash-table"] = False
    session["dash-table-reloaded"] = False
    session["dash-table-updated"] = False
    session["times-page-refreshed"] = 0
    # print("Logga ut", session)
    return "hej"


#Every time we refresh the app, this function is triggered
@app.callback(Output('tables','children'),
Output('store-data', 'data'),
Input('interval-db', 'n_intervals'),
Input('delete-button', 'n_clicks'))
def update_graphs(url, n_clicks):
    df = pd.DataFrame(
            {"labels": ["Kurs", "Kurskod", "Betyg", "Storlek"],}
        )

    print(n_clicks)
    
    session["dash-table-reloaded"] = True

    #first time the page loads, session["times-page-refreash"] = 1
    session["times-page-refreshed"] = session.get("times-page-refreshed") + 1

    if session.get("times-page-refreshed") > 1:
        session["page-refreshed"] = True
        

    session["grade-dash-updated"] = False

    if n_clicks >= 1:
        db.child("users/").child(session["uid"]).child("Betyg").set(None), # must match other if statemenyt
        n_clicks=0
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
        ),], n_clicks

    #B??R HA EN TRY CATCH ELLER N??GOT; OM MAN SKULLE SKRIVA IN KONSTIGA SAKER S?? M??STE TABELLEN ??ND?? KOMMA UPP

    # print(url)
    if  session.get('loggedIn') == True and db.child("users/").child(session["uid"]).child("Betyg").get().val() != None:
        # print("V??R NYA")
        data_db = db.child("users/").child(session["uid"]).child("Betyg").get()
        row_grades = []
        row_courses = []
        row_codes = []
        row_points = []

        for obj in data_db.each():

            # print(obj.key()) #Biologi - breddning
            # print(obj.val()) #{'Betyg': 'VG', 'Kurs': 'Biologi - breddning', 'Storlek': '50'}
            row_grades.append(obj.val()["Betyg"])
            row_courses.append(obj.val()["Kurs"])
            row_codes.append(obj.val()["Kurskod"])
            row_points.append(obj.val()["Storlek"])


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
        # print("---------")
        # print("MY DATA: ", my_data)
        # print("---------")


        return [ 
            dcc.Loading(children = [
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
            persistence=True, 
            persistence_type="local",
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
            ],
            type = "cube")
           
        ], session["dash-table-reloaded"] #gets in the store (session)
    
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
        ),], session["dash-table-reloaded"]

        



#This callback fires when we press the "find education" button, to match our profile to educations
@app.callback(Output("match-edu-div", "children"),
State('adding-rows-table', 'derived_virtual_data'),
State('adding-rows-table', "derived_virtual_selected_rows"),
Input("match-edu-button", "n_clicks")
)
def find_education(rows,derived_virtual_selected_rows, n_clicks):

    if n_clicks >= 1:
        print("CLIKED")

        if derived_virtual_selected_rows is None:
            derived_virtual_selected_rows = []



        #Every time we reload the page, the dff = df since it's empty
        dff = df if rows is None else pd.DataFrame(rows)

        #SINCE ROWS GET NONE ON PAGE LOAD
        if rows is None and db.child("users/").child(session["uid"]).child("Betyg").get().val() != None:
            data_db = db.child("users/").child(session["uid"]).child("Betyg").get()
            row_grades = []
            row_courses = []
            row_codes = []
            row_points = []

            for obj in data_db.each():

                # print(obj.key()) #Biologi - breddning
                # print(obj.val()) #{'Betyg': 'VG', 'Kurs': 'Biologi - breddning', 'Storlek': '50'}
                row_grades.append(obj.val()["Betyg"])
                row_courses.append(obj.val()["Kurs"])
                row_codes.append(obj.val()["Kurskod"])
                row_points.append(obj.val()["Storlek"])


            my_data = {
                "column-0": row_courses,
                "column-2":row_grades,
                "column-3": row_points,
                "column-1":row_codes
            }

            dff = pd.DataFrame(data = my_data)

        dff= dff.replace(np.nan,"")

        if rows is None and db.child("users/").child(session["uid"]).child("Betyg").get().val() == None:
            dff = df
        elif rows is not None and db.child("users/").child(session["uid"]).child("Betyg").get().val() == None:
            dff = pd.DataFrame(data = rows)
            
        dff= dff.replace(np.nan,"")

        #Empty cell is == None
        #If we erase a column, that column disapears from df
        if "column-0" not in dff:
            dff["column-0"] = ""

        if "column-1" not in dff: #dont use "elif", use if, otherwise they will not be evaluated
            dff["column-1"] = ""

        if "column-2" not in dff:
            dff["column-2"] = ""

        if "column-3" not in dff:
            dff["column-3"] = ""

        course_name = dff["column-0"].tolist()
        code = dff["column-1"].tolist()

        dff["column-2"]= dff["column-2"].replace('',0)
        grades = dff["column-2"].tolist()
        print(grades)

        dff["column-3"]= dff["column-3"].replace('',0)
        credits = dff["column-3"].tolist()
        print(credits)

        import time

    

        d = {
            "Kurs": course_name,
            "Betyg":grades,
            "Storlek": list(map(int, credits)), #change from strings to ints
            "Kurskod":code
        }


        class_words_training_data = tokenize_stem_trainingData()

        def course_score_class():
            dict_all_courses_points = pd.DataFrame({
                'Betyg: ': [],
                'Kurs: ': [],
                'Score: ': [],
                'Klass: ': [],
                })
            return dict_all_courses_points

        dict_all_courses_points = course_score_class()



            #creates a list with all courses and their corresponding class and score
        #This function is called upon in the "summarize_class_scores" function
        #INput: A grade dict   kurs    | storlek | betyg
        #                    Biologi A      50        VG
        #Output: class |score|course
        #        milj?? | 15 | Biologi A
        #naturvetenskap| 15 | Biologi A
        #Mappar alla kurser vi har l??st mot olika klasser
        def map_course_to_classes(list_course):
            #Create some glabal attributes, which will be used in the calculate_class_score function

            #Courses that contains any of the following words, will not be tokenized or stemmed
            excluding_words = ['breddning', 'specialisering', '5', '4','3','2',]

            i = 0
            course_list = []
            grade_list = []
            class_list = []
            score_list = []

            
            for ind in list_course.index:
                nb_classes_iterated = 0
                token = False
                true_false = []
                token_words = []

            
                #Each course in our grades is separately stored in these three variables
                course = list_course['Kurs'][ind]
                grades = list_course['Betyg'][ind]
                size = list_course['Storlek'][ind]
                data = {'Kurs': [course], 'Storlek': [size],'Betyg': [grades]}
                #add all courses to the datafram
                #For each course in our grade, we loop thorugh each class_name in our training data to see if there are any courses that match
                #for every course, we loop through each class to see if we have a match
                for word in nltk.word_tokenize(course):
                    word = word.replace('och', '')
                    word = word.replace('-', '')
                    word = word.replace('p??', '')
                    token_words.append(word)
                    #If our course contains any of the words included in the excluding_words array,
                    #we want to append the course directly, without any further stemming etc.
                    if word in excluding_words:
                        true_false.append(True)
                    else:
                        true_false.append(False)

                #iterate through every key in our training data
                import time
                #we want to find what class our course belongs to
                # class_words_training_data contains all traing data (data_for_training)
                for class_name in class_words_training_data.keys():

                    nb_classes_iterated +=1
                



                    #Iterate thorugh each word (value) in key
                    #for class_word in class_words_training_data[class_name]:

                    #All words in excludin_words are stored in the traing data as is, without being stemmed/tokenized, see function "stokenize_stem_trainingData"
                    if (course in class_words_training_data[class_name] and any(true_false)): #any gives true if the list contains any true
                        
                        #Add class name, course name and score to each list, so these can be put into adatafram later
                        score = calc_grade(data)
                        #we want to se which class the course corresponds to
                        class_list.append(class_name)
                        grade_list.append(grades)
                        course_list.append(course)
                        score_list.append(score)
                        # time.sleep(2)

                    #if the word doesn't contain any of the words in exckluding_words array, tokenize and stem it!
                    if (any(true_false)==False):


                        for token_word in token_words:


                            # check to see if the stem of the word (the course in our grades that has been stemmed) is in any of our classes (from trainng data stemmed)
                            #Iterate through all classes and see if we have a match, that is, if the stemmed word is present in any class
                            if stemmer.stem(token_word.lower()) in class_words_training_data[class_name]:

                                token = True #this should always be true, since we want the courses to be mapped to a class
                                score = calc_grade(data)
                                #Add class name, course name and score to each list, so these can be put into adatafram later
                                class_list.append(class_name)
                                grade_list.append(grades)
                                course_list.append(course)
                                score_list.append(score)

                            # #If the word doesnt match any of the specified classes add the course to "??vrigt"
                            #if we have iterated trhough every class, and not found any mathing classes
                            if nb_classes_iterated == len(class_words_training_data) and token == False: #the course has not been added..
                                score = calc_grade(data)
                                #Add class name, course name and score to each list, so these can be put into adatafram later
                                class_list.append("??vrigt")
                                grade_list.append(grades)
                                course_list.append(course)
                                score_list.append(score)
                        

            dict_all_courses_points['Klass']=class_list
            dict_all_courses_points['Score']=score_list
            dict_all_courses_points['Kurs']=course_list
            #Drop all rows/columns that contain NaN-values
            dict_all_courses_points.dropna(how='all', axis=1, inplace=True) 
            #returns a dict with all courses/grades/classes
            return dict_all_courses_points.drop_duplicates() #drop all duplicates, so we dont need to worry about the structure/format of the training data 
        
                #------------------------------------------------------------------------------------------------------------------------
        #A function that suggests what you should study, based on your grades
        #The function match your grades/interest with different education attributes, and calculates educzation matches
        #Input: Sorted DataFrame with data, education_data
        #Output, 
        #--------------------??NDRA H??R S?? VI INTE TITTAR P?? TOPP KLASSERNA (M??STE H??RDKODA VILKA NIV??ER VI VILL HA)-------------------------------------
        def suggest_education(dframe,normed_grades):

            match = 0
            #print("d_frame", dframe)

            #Sort by averag. class score, and number of courses. We want to suggest an education based on 
            #the person's strongest area
            sorted_dframe = dframe.sort_values(by=['Averg. score', 'Nbr of courses',], ascending=(False, False))
            #print(sorted_dframe.head(5))

            normed_grades = normed_grades


            excluding_words = ['breddning', 'specialisering', '5', '4','3','2',]


            nbr_classes = len(sorted_dframe) # ex, 10 rows (10 different classes)
            #We want to split up the number of classes into 4 different groups, so we can use those groups in class1_classes, class2_classes etc

            class1_classes = sorted_dframe.head(int(round(0.2*nbr_classes)))
            #print("class1_classes",class1_classes)
            best_class1 = class1_classes['Klass']
            #convert df to array, so we can compare in for loop
            #numpy_clas1 contains the top 3 classes, to be compared with the data in the education_class_dataframe
            numpy_class1 = best_class1.to_numpy()
            #print('NUMPY_CLASS1', numpy_class1)

            class2_classes = sorted_dframe.iloc[0:int(round(0.3*nbr_classes))] #3 is included, 5 is excluded
            best_class2 = class2_classes['Klass']
            numpy_class2 = best_class2.to_numpy()

            #print('NUMPY_CLASS2', numpy_class2)

            #----Class 1 and class 2 icludes classes, whil class3 and class4 contains courses:-------------------

            #find courses from your 2 best classes, only unique courses, since the same course can be present in multiple classes
            numpy_courses3 = []
            #Class3_courses is a part of a dataframe
            class3_courses = sorted_dframe.head(int(round(0.3*nbr_classes)))

            #best_courses3 is a column from a dataframe, a list of lists
            best_courses3 = class3_courses['Included courses']

            #to_numpy converrts dataframe to numpy array, list of lists
            numpy_courses3_not_unique = best_courses3.to_numpy()

            #from list of list to one list
            numpy_courses3_not_unique= list(chain.from_iterable(numpy_courses3_not_unique))

            numpy_courses4 = []
            class4_courses = sorted_dframe.iloc[int(round(0.31*nbr_classes)):nbr_classes] #all courses included in the classes from top 21% to 50%
            best_courses4 = class4_courses['Included courses']
            #to_numpy converrts dataframe to numpy array, list of lists
            numpy_courses4_not_unique = best_courses4.to_numpy()
            numpy_courses4_not_unique= list(chain.from_iterable(numpy_courses4_not_unique))
            

            for x in numpy_courses3_not_unique:
                if x not in numpy_courses3:
                    numpy_courses3.append(x)
            
            for x in numpy_courses4_not_unique:
                if x not in numpy_courses4:
                    numpy_courses4.append(x)

            #Iterate through each row in education_class_dataFrame (lower_case_Education_df(), we want lower case) to
            #calculate matches for every education class
            for row in education_class_dataFrame.index:

                #OBS TA BORT "OCH", och ev andra ord
            
                #Iterate through class1 (your top 3 classes)
                #We dont need to tokenize class names, since its standarized
                #x = spr??k, samh??llsvetenskap, kultur
                for x in numpy_class1:
            
                    #Tokenize each word: "Till??mpad programmering" => "till??mpad", "programmering"
                    #If we have a match, each match is "worth" 20%
                    if (x.lower() in education_class_dataFrame['class1'][row]):
                
                        #Max 20 * 3 = 60% match
                        match += 12
                

                #Iterate through class2 (your top 4-5 classes)
                #Instead of iterating thorugh the courses in top classes, iterate trough all of your grades (since you can have good grades in courses in bottom list)
                for x in numpy_class2:
                    #If we have a match, each match is "worth" 20%
                    #NO need to use stem for classes
                    if (x.lower() in education_class_dataFrame['class2'][row]):
                        #Max 2 * 5 = 10% match
                        match += 9

                #Iterate through class3 (courses in your 2 best classes)---------------
                words3 = []

                for word3 in list(education_class_dataFrame['class3'][row]):

                    #We use stem for courses
                    for word in nltk.word_tokenize(word3):
                        words3.append(stemmer.stem(word))

                occurance3 = 0
                #iterate thorugh the courses, included in our top classes
                for x in numpy_courses3:

                    index = list(normed_grades['Kurs']).index(x) #get the index where the course is 
                    normed_score = normed_grades['Betyg'][index]
            
                    for word in nltk.word_tokenize(x):
                        #count the number of times 
                        occurance3 += words3.count(word)
                    
                initial_match3 = 12
                match += initial_match3*occurance3*normed_score
                #----------------------------------------------------------------------
                #Iterate through class3 (courses in your 2 best classes)---------------
                words4 = []
                for word4 in education_class_dataFrame['class3'][row]:
            
                    for word in nltk.word_tokenize(word4):
                        words4.append(stemmer.stem(word))

                occurance4 = 0
                for x in numpy_courses4:

                    index = list(normed_grades['Kurs']).index(x) #get the index where the course is 
                    normed_score = normed_grades['Betyg'][index]
            
                    for word in nltk.word_tokenize(x):
                        #count the number of times 
                        occurance4 += words4.count(word)
                        
                initial_match4 = 2
                match += initial_match4*occurance4*normed_score

                #match cannot be greated than 100%      
                if match > 100:
                    match = 100

                print('Matchen f??r ', education_class_dataFrame['Education'][row], 'vid',education_class_dataFrame['Schools'][row] ,' ??r ', round(match,0),'%')
                match = 0


        suggest_education(summarize_class_scores(map_course_to_classes(d_to_df(d))), norm_grade(d))






#This callback fires when we change data in the data table, i.e change a VG to a G or something like that
#returns a graph
@app.callback(
    Output('datatable-interactivity-container','children'),
    Output('your_grade', "children"),
    Output('graph-classes', "figure"),
    Output('graph-classes-grade-occurence', "figure"),
    Output('nbr_grades', "children"),
    Output('qual-list', "children"),
    Input('adding-rows-table', 'derived_virtual_data'),
    State('adding-rows-table', 'active_cell'), #Change from input to state, since we dont want everything inside
    #this callback to run everytime we press something, only when we change data
    # State('adding-rows-table', 'active_cell'),s 
    Input("store-data", "data"),

    #STATE DOESNT TRIGGER CALLBACK, ONLY INPUT DOES
    State('adding-rows-table', "derived_virtual_selected_rows"),
    State('adding-rows-table', "derived_virtual_data"))
# @cross_origin(supports_credentials=True)
def update_graphs(rows,active_cell,n_clicks,derived_virtual_selected_rows,derived_virtual_data):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.

     #kolla bara p?? time pag erefreshed, uppdatera i slutet h??r

    #if the user have alrdy entered grades
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    


    #Every time we reload the page, the dff = df since it's empty
    dff = df if rows is None else pd.DataFrame(rows)

    #SINCE ROWS GET NONE ON PAGE LOAD
    if rows is None and db.child("users/").child(session["uid"]).child("Betyg").get().val() != None:
        data_db = db.child("users/").child(session["uid"]).child("Betyg").get()
        row_grades = []
        row_courses = []
        row_codes = []
        row_points = []

        for obj in data_db.each():

            # print(obj.key()) #Biologi - breddning
            # print(obj.val()) #{'Betyg': 'VG', 'Kurs': 'Biologi - breddning', 'Storlek': '50'}
            row_grades.append(obj.val()["Betyg"])
            row_courses.append(obj.val()["Kurs"])
            row_codes.append(obj.val()["Kurskod"])
            row_points.append(obj.val()["Storlek"])


        my_data = {
            "column-0": row_courses,
            "column-2":row_grades,
            "column-3": row_points,
            "column-1":row_codes
        }

        dff = pd.DataFrame(data = my_data)
    
    dff= dff.replace(np.nan,"")

    if rows is None and db.child("users/").child(session["uid"]).child("Betyg").get().val() == None:
        dff = df
    elif rows is not None and db.child("users/").child(session["uid"]).child("Betyg").get().val() == None:
        dff = pd.DataFrame(data = rows)
     
    dff= dff.replace(np.nan,"")

    #Empty cell is == None
    #If we erase a column, that column disapears from df
    if "column-0" not in dff:
        dff["column-0"] = ""
    
    if "column-1" not in dff: #dont use "elif", use if, otherwise they will not be evaluated
        dff["column-1"] = ""
    
    if "column-2" not in dff:
        dff["column-2"] = ""

    if "column-3" not in dff:
        dff["column-3"] = ""
 
    course_name = dff["column-0"].tolist()
    code = dff["column-1"].tolist()
    dff["column-2"]= dff["column-2"].replace('',"IG")
    grades = dff["column-2"].tolist()
    print(grades)

    dff["column-3"]= dff["column-3"].replace('',0)
    credits = dff["column-3"].tolist()
    # print(credits)


    # d is used to calculate grades etc
    d = {
            "Kurs": course_name,
            "Betyg":grades,
            "Storlek": list(map(int, credits)), #change from strings to ints
            "Kurskod":code
        }

    i = 0
    for c in course_name:
        if i > len(course_name):
            i = 0
        
        
        my_data = {
            "Kurs": c,
            "Betyg":grades[i],
            "Storlek": credits[i],
            "Kurskod":code[i]
        }
        
        
        if c != "" and c != None:
            # print("MY DATA FR??N KLICK_FUNKTIONEN", my_data)
            # print(my_data["Kurs"])
            # print(type(my_data["Kurs"]))
            # we need to update the previous
            db.child("users/").child(session["uid"]).child("Betyg").child(c).set(my_data)
            
        i += 1

    #This sections is required to update the database and to ensure that the database is up to date with the
    #dash-table
    all_objects = db.child("users/").child(session["uid"]).child("Betyg").get()
    for obj in all_objects.each():
                #If the updated cours in data table does not include a particular course in firebase, remove this
                #from firebase
        # print("OBJ KEY",obj.key())
        # print("kol0",list(dff["column-0"]))
        if obj.key() not in list(dff["column-0"]):
            # print(obj.key(), "not in course name")
            db.child("users/").child(session["uid"]).child("Betyg").child(obj.key()).remove()
    # print("...................................")
    session["grade-dash-table"] = True
    session["dash-table-updated"] = True
    # derived_virtual_selected_rows = dff   

    #the data_table changes when the user interacts with the table
   

    #
    #
    #------------FUNCTIONS TO CALCULATE YOUR GRADE BASED ON DASH TABLE INPUT-----------------------------------

    #***********CALC GRADE****************************

    #Your grades is updated everytime the dash tables is updated
    your_grade = calc_grade(d)
    #***********CALC GRADE****************************



    #***********STEM TRANING DATA TO GET THE CLASSES THAT EACH COURSE BELONGS TO*************

    def course_score_class():
        dict_all_courses_points = pd.DataFrame({
            'Betyg: ': [],
            'Kurs: ': [],
            'Score: ': [],
            'Klass: ': [],
            })
        return dict_all_courses_points

    dict_all_courses_points = course_score_class()



    class_words_training_data = tokenize_stem_trainingData()
    #creates a list with all courses and their corresponding class and score
    #This function is called upon in the "summarize_class_scores" function
    #INput: A grade dict   kurs    | storlek | betyg
    #                    Biologi A      50        VG
    #Output: class |score|course
    #        milj?? | 15 | Biologi A
    #naturvetenskap| 15 | Biologi A
    #Mappar alla kurser vi har l??st mot olika klasser
    def map_course_to_classes(list_course):
        #Create some glabal attributes, which will be used in the calculate_class_score function

        #Courses that contains any of the following words, will not be tokenized or stemmed
        excluding_words = ['breddning', 'specialisering', '5', '4','3','2',]

        i = 0
        course_list = []
        grade_list = []
        class_list = []
        score_list = []

        
        for ind in list_course.index:
            nb_classes_iterated = 0
            token = False
            true_false = []
            token_words = []

        
            #Each course in our grades is separately stored in these three variables
            course = list_course['Kurs'][ind]
            grades = list_course['Betyg'][ind]
            size = list_course['Storlek'][ind]
            data = {'Kurs': [course], 'Storlek': [size],'Betyg': [grades]}
            #add all courses to the datafram
            #For each course in our grade, we loop thorugh each class_name in our training data to see if there are any courses that match
            #for every course, we loop through each class to see if we have a match
            for word in nltk.word_tokenize(course):
                word = word.replace('och', '')
                word = word.replace('-', '')
                word = word.replace('p??', '')
                token_words.append(word)
                #If our course contains any of the words included in the excluding_words array,
                #we want to append the course directly, without any further stemming etc.
                if word in excluding_words:
                    true_false.append(True)
                else:
                    true_false.append(False)

            #iterate through every key in our training data
            import time
            #we want to find what class our course belongs to
            # class_words_training_data contains all traing data (data_for_training)
            for class_name in class_words_training_data.keys():

                nb_classes_iterated +=1
            



                #Iterate thorugh each word (value) in key
                #for class_word in class_words_training_data[class_name]:

                #All words in excludin_words are stored in the traing data as is, without being stemmed/tokenized, see function "stokenize_stem_trainingData"
                if (course in class_words_training_data[class_name] and any(true_false)): #any gives true if the list contains any true
                    
                    #Add class name, course name and score to each list, so these can be put into adatafram later
                    score = calc_grade(data)
                    #we want to se which class the course corresponds to
                    class_list.append(class_name)
                    grade_list.append(grades)
                    course_list.append(course)
                    score_list.append(score)
                    # time.sleep(2)

                #if the word doesn't contain any of the words in exckluding_words array, tokenize and stem it!
                if (any(true_false)==False):


                    for token_word in token_words:


                        # check to see if the stem of the word (the course in our grades that has been stemmed) is in any of our classes (from trainng data stemmed)
                        #Iterate through all classes and see if we have a match, that is, if the stemmed word is present in any class
                        if stemmer.stem(token_word.lower()) in class_words_training_data[class_name]:

                            token = True #this should always be true, since we want the courses to be mapped to a class
                            score = calc_grade(data)
                            #Add class name, course name and score to each list, so these can be put into adatafram later
                            class_list.append(class_name)
                            grade_list.append(grades)
                            course_list.append(course)
                            score_list.append(score)

                        # #If the word doesnt match any of the specified classes add the course to "??vrigt"
                        #if we have iterated trhough every class, and not found any mathing classes
                        if nb_classes_iterated == len(class_words_training_data) and token == False: #the course has not been added..
                            score = calc_grade(data)
                            #Add class name, course name and score to each list, so these can be put into adatafram later
                            class_list.append("??vrigt")
                            grade_list.append(grades)
                            course_list.append(course)
                            score_list.append(score)
                    

        dict_all_courses_points['Klass']=class_list
        dict_all_courses_points['Score']=score_list
        dict_all_courses_points['Kurs']=course_list
        #Drop all rows/columns that contain NaN-values
        dict_all_courses_points.dropna(how='all', axis=1, inplace=True) 
        #returns a dict with all courses/grades/classes
        return dict_all_courses_points.drop_duplicates() #drop all duplicates, so we dont need to worry about the structure/format of the training data 


    #classes contains all classes (can appear several times)
    classes = map_course_to_classes(d_to_df(d))["Klass"]
    
    input_pie_chart_function = map_course_to_classes(d_to_df(d))

    def set_grades_df(d):
        df = pd.DataFrame(data=d)
        return df

    number_of_grades = {
        "Betyg":[],
        "Antal":[]
    }

    #Ex output: {'Betyg': ['G', 'MVG', 'VG', 'IG'], 'Antal': [6, 12, 7, 1]}
    def calc_nbr_grade(d,g):
        df = set_grades_df(d)
        nbr_of_grade = 0
        for ind in df.index:
            if g == df['Betyg'][ind]:
                nbr_of_grade += 1
                number_of_grades["Betyg"].append(g)
        number_of_grades["Betyg"] = list(set(number_of_grades["Betyg"])) #remove duplicates
        if nbr_of_grade != 0: #dont add grades we dont have
            number_of_grades["Antal"].append(nbr_of_grade)
        return number_of_grades #return number of MVG, VG etc
    #Description: Antal "VG" (exempelvis) i dina betyg
    #INput: grade dic, och ett betyg, ex "VG", eller "G"

    #Iterate thorugh MVG, VG, G, IG , A, B ,C,D,F
    for g in grade_and_their_score_dict["Betyg"]: #MVG, VG, G, IG, A, B etc
        number_of_grades = calc_nbr_grade(d,g)

    
      # print("NUMBER OF GRADES", number_of_grades)
    #NUMBER OF GRADES {'Betyg': ['G', 'MVG', 'VG', 'IG'], 'Antal': [6, 12, 7, 1]}

    #prepare the plotting of classes and coresponding number of grades in each class:
    #for example class A has 1 MVG and 1 VG, while class B has 3 IG
    #for this we need to find the corresponding classes which contains all these grades

    def pie_chart_classes(map_course_to_classes):
        averg_grade_df = summarize_class_scores(map_course_to_classes)

        #We want to put each unique class in this list want to put the number of occurences in this list
        classes_df = { "??mnesomr??de" :[],
                    "Antal kurser": [],
                    "Medelbetyg":[]
            }



    #   index = list(normed_grades['Kurs']).index(x) #get the index where the course is 
    #   normed_score = normed_grades['Betyg'][index]

        #Find unique classes
        for ind in map_course_to_classes["Klass"]:
            if ind not in classes_df["??mnesomr??de"]:
                index = list(averg_grade_df["Klass"]).index(ind)
                aver_grade = averg_grade_df["Averg. score"][index]
                classes_df["??mnesomr??de"].append(ind)
                classes_df["Antal kurser"].append(1)
                classes_df["Medelbetyg"].append(aver_grade)
            else:
                index = list(classes_df["??mnesomr??de"]).index(ind)
                updated_nbr = classes_df["Antal kurser"][index] + 1
                classes_df["Antal kurser"][index] = updated_nbr
        
        fig = px.pie(classes_df, values= "Antal kurser", names="??mnesomr??de", title="hej",hover_data=["Medelbetyg"],hole =.3)
        return {"fig":fig, "classes_df":classes_df["??mnesomr??de"]}
    
    pie_chart = pie_chart_classes(input_pie_chart_function)["fig"]


    #Med denna funktionen f??r vi alla betyg som finns i respektive klass.
    #Anv??nds i funktionen: nbr_grade_in_givven_class 
    def calc_nbr_grades_in_each_class(d):
        courses = d_to_df(d)
        df1 = summarize_class_scores(map_course_to_classes(courses))
        df2 = set_grades_df(d)
        grade_list = []
        #Iterera igenom alla klasser
        for ind in df1.index:
            #F??r varje klass skapar vi en lista d??r vi kan ha betygen
            nbr_grades = []
            for x in df1['Included courses'][ind]:
                #Index f??r kursen. M??ste g??ra om till e lista f??r att kunna anv??nda .index
                index_course = list(df2['Kurs']).index(x)
                #H??mta betyget
                grade_course = df2['Betyg'][index_course]
                nbr_grades.append(grade_course)

            #Vi vill ha en lista av listor..
            grade_list.append(nbr_grades)
            
        df1['Antal betyg'] =grade_list
        return df1



    #With this function we get number of grades in a given class (a_class)
    #Related function: calc_nbr_grades_in_each_class
    def nbr_grade_in_givven_class(d,a_grade, a_class):
        
        df1 = calc_nbr_grades_in_each_class(d)

        #f?? index f??r den klassen vi ??r intresserad av
        index = list(df1['Klass']).index(a_class)
        counter = 0

        #h??mta antalet betyg i den klassen
        grade_list = df1['Antal betyg'][index]
        for x in grade_list:
            if x == a_grade:
                counter +=1

        return counter



    colors_grade_occurence_plot = {
    'background': '#FFFFFF',
    'text': '#000000'
        }
    #"Fruit": ["class A", "Class B", "Class C", "Class A", "Class B", "Class C"], 
    #get unique classes and make it larger accoring to following rule: unique classes * nbr unique grades
    #where nbr unique grades is equal to len(number_of_grades["Betyg"])

    #taken from map_course_to_classes function
    #find uniqe classes, used also in the pie chart (classes and number of courses in each class)
    # allow us to plot it
    unique_class_occurence_plot = list(set(classes))*len(number_of_grades["Betyg"]) #4 * 11 = 44
    # print("unique_class_occurence_plot", unique_class_occurence_plot)
    # print("list(set(classes))", list(set(classes))) #['beteende', 'fysisk h??lsa', 'tr??ning', 'medicin', 'spr??k', 'mental h??lsa', 'juridik', 'ekonomi', 'naturvetenskap', 'samh??llsvetenskap', 'humanioria']
    grades_class_amount_occurence_plot = []


    #NUMBER OF GRADES {'Betyg': ['G', 'MVG', 'VG', 'IG'], 'Antal': [6, 12, 7, 1]}
    #iterate thorugh your unique grades
    for a_grade in number_of_grades["Betyg"]:
        for a_class in list(set(classes)):
            #For example IG in class "milj??", we want to iterate every grade, not only the first
            nbr_grade_in_class = nbr_grade_in_givven_class(d,a_grade, a_class)
            grades_class_amount_occurence_plot.append(nbr_grade_in_class)


    #number_of_grades = {'Betyg': ['G', 'MVG', 'VG', 'IG'], 'Antal': [6, 12, 7, 1]}

    #M??ste ha r??tt mappning
    grades_occurence_plot = []
    for i in number_of_grades["Betyg"]:
        for j in list(set(classes)):
            grades_occurence_plot.append(i)


    df_grade_class_occurence_plot = pd.DataFrame({
            "??mnesomr??den": unique_class_occurence_plot,#string
            "Antal kurser": grades_class_amount_occurence_plot, #int
            "Betyg": grades_occurence_plot #string
        })



    fig_grade_occurence = px.bar(df_grade_class_occurence_plot, x="??mnesomr??den", y="Antal kurser", color="Betyg", barmode="group")
    # fig_grade_occurence.update_layout(yaxis_range=[0,20])
    
    fig_grade_occurence.update_layout(
        plot_bgcolor=colors_grade_occurence_plot['background'],
        paper_bgcolor=colors_grade_occurence_plot['background'],
        font_color=colors_grade_occurence_plot['text']
    )


     #------------ END FUNCTIONS TO CALCULATE YOUR GRADE BASED ON DASH TABLE INPUT END---------------------------



    colors = ['#7f9bff' if i in derived_virtual_selected_rows else '#7f9bff'
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

    session["page-refreshed"] = False
    dff.rename(columns = {'column-0':'Kurs'}, inplace = True)
    dff.rename(columns = {'column-1':'Kurskod'}, inplace = True)
    dff.rename(columns = {'column-2':'Betyg'}, inplace = True)
    dff.rename(columns = {'column-3':'Score'}, inplace = True)


    
    #Input to pre_edu is a dict and a dataframe with all prerequisite courses is returned
    #d in qualification is your grades
    print(dff)
    print(pre_edu(prerequisite_data))
    qual_list = qualification(pre_edu(prerequisite_data), dff)
    print(qual_list)

    return [
      
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["Kurs"],
                        "y": dff["Betyg"],
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
        for column in ["Kurs"] if column in dff
    ], your_grade, pie_chart, fig_grade_occurence,[number_of_grades["Betyg"][0], ":" ,number_of_grades["Antal"][0]], qual_list
    




# # ???/??? URL is bound with hello_world() function.
# def Hello():
#     return data_updated_table
if __name__ == '__main__':
    app.run_server(debug=False)

