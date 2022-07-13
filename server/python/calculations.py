
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import pickle
import numpy as np




def return_d(df):
     # d = {'Kurs': ['kultur- och idéhistoria', 'politik hållbar utveckling', 'Biologi - breddning', 'kost, måltid och munhälsa', 
     # 'ENGELSKA B', 'Estetisk verksamhet','Företagsekonomi A','FRANSKA STEG 3','visuell kommunikation','Fysik 2',
     # 'Historia A','leda','Idrott och hälsa A','Idrott och hälsa B','vårdpedagogik och handledning',
     # 'Kemi 2','Aktivitetsledarskap','Matematik A', ' konstarterna och samhället', 'MATEMATIK 3','MATEMATIK 4',
     # 'MATEMATIK 5','NATURKUNSKAP A','Projektarbete','PSYKOLOGI A','RELIGIONSKUNSKAP A','kroppen som uttrycksmedel','Affärsjuridik','Rättskunskap',
     # 'Samhällskunskap A','Svenska A','Svenska B'], 
     # 'Storlek': [100,50,50,100,100,50,50,100,100,150,100,50,50,100,50,100,100,100,100,50,100,100,50,50,100,50,50,50,50,100,100,100], 
     # 'Betyg': ['VG','G','VG','VG','VG','MVG','G','G','G','G','G','vg','MVG','MVG','VG','G','MVG','VG','VG','G','G','IG','VG','VG','VG',
     # 'MVG','G','MVG','VG','VG','VG','VG']}



     lower_words=[]
     
     for value in df['Kurs']:
     
          value =value.lower()
          lower_words.append(value)

          print('value',value)
     df['Kurs']=lower_words

     return df


tot_points = 2500 #Nbr of course points included in a high school diploma


#Omvandligsdict, används för att omvandla kvalitativ betyg till kvantitativ
grade_and_their_score_dict= {
  'Betyg': ['MVG', 'VG', 'G', 'IG', 'A', 'B', 'C', 'D', 'E', 'F'],
  'Score': [ 20,   15,    10,   0, 20, 17.5, 15,  12.5, 10,  0] 
}
print(grade_and_their_score_dict)



grade_and_their_score_dict_df = pd.DataFrame(data=grade_and_their_score_dict)



#Omvandla dina kvalitativa inlästa betyg (MVG-IG eller A-F) till kvantitativ (20-0).
#INPUT: Dict, betyg
#OUTPUT: En dataframe, där dina betyg har ersatts av siffror MVG = 20, VG = 15 osv
#ANVÄNDNING: Används som hjälpfunktion till norm_grade
def grade(df):

     #Om betygen INTE är en String, betyder det att vi har använt oss av grade-funkionen en gång innan. Då ska vi 
     #bara returnera df utan att gå in och ändra
     if type(df['Betyg'][0]) != str:
          return df
          
     
     #Loopa igenom dina betyg, dataframe
     for ind in df.index:

          string_grade = df['Betyg'][ind] # T.ex "VG" eller "B"

          int_grade_index = list(grade_and_their_score_dict_df['Betyg']).index(string_grade.upper()) #Få fram index för där "VG" Ligger, så vi kan hämta motsvarande score
          #int_grade_index = 2 #Få fram index för där "VG" Ligger, så vi kan hämta motsvarande score
          
          int_grade = grade_and_their_score_dict_df['Score'][int_grade_index]
          df['Betyg'][ind] = int_grade
       
     
     return df

# print("Grad",grade(pd.DataFrame(data=d)))



#En funktion som räknar ut dina totala kurspoäng. För att personer ska kunna följa sina betyg,
#INPUT: betyg dict
#OUTPUT: en siffra
#ANVÄNDNING: Används som hjälpfunktion till norm_grade
def calc_tot_points(d):
     df = pd.DataFrame(data=d) #en lokal kopia av betygen
     tot_points = 0
     for ind in df['Storlek']:
          tot_points += ind
     return tot_points



     

#Normalisera betygen, dvs betyg*storlek/totala antalet kurspoäng
#HJÄLPERFUNKTIONER: calc_tot_points och grade_df
def norm_grade(d):
     df = pd.DataFrame(data=d)
     #Använder hjälpfunktionen för att beräkna
     df1 = grade(df)
     tot_points = calc_tot_points(d)
     for ind in df1.index:
          grade1 = df1['Betyg'][ind] #T.ex "MVG" eller "A"
          points =df1['Storlek'][ind] #T.ex 100 eller 50
          normed_grade = grade1*points/tot_points
          df1['Betyg'][ind] = normed_grade
     return df1



# sätt alla kurser till max-betyget
#Input: d = grades (type dict), df = a dataframe with your grades 
#OUTPUT: En dataframe, där vi satt alla betyg till norm max
def set_max_grade(d):
     df = pd.DataFrame(data = d)
     for ind in df.index:
          df['Betyg'][ind] = 20*df['Storlek'][ind]/tot_points
     return df


def set_B_grade(d):
     df = pd.DataFrame(data = d)
     for ind in df.index:
          df['Betyg'][ind] = 17.5*df['Storlek'][ind]/tot_points
     return df


def set_VG_C_grade(d):
     df = pd.DataFrame(data = d)
     for ind in df.index:
          df['Betyg'][ind] = 15*df['Storlek'][ind]/tot_points

     return df

def set_D_grade(d):
     df = pd.DataFrame(data = d)
     for ind in df.index:
          df['Betyg'][ind] = 12.5*df['Storlek'][ind]/tot_points
     return df


def set_G_E_grade(d):
     df = pd.DataFrame(data = d)
     for ind in df.index:
          df['Betyg'][ind] = 10*df['Storlek'][ind]/tot_points
     return df


#print(set_max_grade(d))

#------------------------------------------------------------------------------------------------------------------------
#Calculate grade diff (max grade - your grade), omitt the courses where the grade is MVG. Also sort the list. 
#Output typ: dataframe
#Output shape:         Kurs | Betyg diff 1 steg | Betyg diff 2 steg | betyg diff 3 steg
#                  cad/cam  |      0,2          | Kan inte höjas mer
# 
#Användning: Används för att beräkna vilken kurs som du bör plugga upp.
#Relaterad Funktion(er) "set_grade_diff_to_each_course" 

#LÄGG TILL SÅ VI HAR 5 STEG OCH SLÅ SAMMAN A-F MED MVG - IG
#OMBS man kan ha betyg från blandade skalor! Men om man har betyg i skala IG-MVG och ska plugga upp blir betygen i nya skalan

def calc_grade_diff(d):
     df = pd.DataFrame(data=d)
     df_act = norm_grade(d)
     df_grade = grade(df)
     df_max = set_max_grade(d)
     df_B = set_B_grade(d)
     df_VG = set_VG_C_grade(d)
     df_D = set_D_grade(d)
     df_G = set_G_E_grade(d)
     grade_diff_5_step = []
     grade_diff_4_step = []
     grade_diff_3_step = []
     grade_diff_2_step = []
     grade_diff_1_step = []
     course_list = []

     for ind in df_act.index:
          #Räkna diff från dina aktuella betyg, upp till max betyg (MVG)
          #Räkna diff från dina aktuella betyg, upp till VG
          grade_MVG_A_diff = df_max['Betyg'][ind]-df_act['Betyg'][ind]
          grade_B_diff = df_B['Betyg'][ind]-df_act['Betyg'][ind]
          grade_VG_C_diff = df_VG['Betyg'][ind]-df_act['Betyg'][ind]
          grade_D_diff = df_D['Betyg'][ind]-df_act['Betyg'][ind]
          grade_G_E_diff = df_G['Betyg'][ind]-df_act['Betyg'][ind]
          #  A   B   C   D   E   F
          # MVG     VG       G   IG

          #IG = 0, eller F = 0
          if df_grade['Betyg'][ind] == 0:
               course_list.append(df_grade['Kurs'][ind])
               grade_diff_5_step.append(grade_MVG_A_diff)#IG/F till A
               grade_diff_4_step.append(grade_B_diff) #IG/F till B
               grade_diff_3_step.append(grade_VG_C_diff) #IG/F till C
               grade_diff_2_step.append(grade_D_diff) #IG/F till D
               grade_diff_1_step.append(grade_G_E_diff) #IG/F till E
          #Från G/E till A är det "4" steg, G/E = 10
          if df_grade['Betyg'][ind] == 10:
               course_list.append(df_grade['Kurs'][ind])
               grade_diff_5_step.append('-')
               grade_diff_4_step.append(grade_MVG_A_diff)#G/E till A
               grade_diff_3_step.append(grade_B_diff) #G/E till B
               grade_diff_2_step.append(grade_VG_C_diff) #G/E till C
               grade_diff_1_step.append(grade_D_diff) #G/E till D
          
                #  A   B   C   D   E   F
                # MVG     VG       G   IG
                # D=12.5
          if df_grade['Betyg'][ind] == 12.5:
               course_list.append(df_grade['Kurs'][ind])
               grade_diff_5_step.append('-')
               grade_diff_4_step.append('-')
               grade_diff_3_step.append(grade_MVG_A_diff) #D till A
               grade_diff_2_step.append(grade_B_diff) #D till B
               grade_diff_1_step.append(grade_VG_C_diff) #D till C
               #C = 15
          if df_grade['Betyg'][ind] == 15:
               course_list.append(df_grade['Kurs'][ind])
               grade_diff_5_step.append('-')
               grade_diff_4_step.append('-')
               grade_diff_3_step.append('-')
               grade_diff_2_step.append(grade_MVG_A_diff)
               grade_diff_1_step.append(grade_B_diff)
               #B = 17.5
          if df_grade['Betyg'][ind] == 17.5:
               course_list.append(df_grade['Kurs'][ind])
               grade_diff_5_step.append('-')
               grade_diff_4_step.append('-')
               grade_diff_3_step.append('-')
               grade_diff_2_step.append('-')
               grade_diff_1_step.append(grade_MVG_A_diff) #B till A
          #if df_grade['Betyg'][ind] == "20":
          if df_grade['Betyg'][ind] == 20:
               course_list.append(df_grade['Kurs'][ind]) 
               grade_diff_5_step.append('-')
               grade_diff_4_step.append('-')
               grade_diff_3_step.append('-')
               grade_diff_2_step.append('-')
               grade_diff_1_step.append('-') #Kan inte höjas mer
               

     datan = {'Kurs' : course_list, 
             'Betyg diff 1 steg' : grade_diff_1_step,
             'Betyg diff 2 steg' : grade_diff_2_step,
             'Betyg diff 3 steg' : grade_diff_3_step,
             'Betyg diff 4 steg' : grade_diff_4_step,
             'Betyg diff 5 steg' : grade_diff_5_step,
             
           
             }
     df3 = pd.DataFrame(data = datan)
     return df3



#To match interest vector with grade diff vector
#Input: interest vector, contaning all courses
#Output: interest vector, where courses with maximum grades have been omitted
def remove_HighestGrades(d):
     df_interest = pd.DataFrame(data=d)
     interestDf_nonMax_grades = []
     for ind in df_interest.index:
          if df_interest['Betyg'][ind] != 'MVG':
               interestDf_nonMax_grades.append(df_interest['Intresse'][ind])
     df_new = pd.DataFrame(interestDf_nonMax_grades, columns=["Intresse"])
     return df_new


def calc_grade(d):
     df = norm_grade(d) #Calling the norm grade function to normalize your grade
     grade1 = 0
     for ind in df.index:
          grade1 = grade1 + df['Betyg'][ind]
     #print('Ditt betyg (utan meritpoäng) är: ', grade)
     #Meritpoäng is given for 
     return grade1


def what_to_focus_on(d,grade1):
     your_grade = calc_grade(d)
     grade_needed = grade1
     if(your_grade > grade_needed):
          return True
     else:
          return grade_needed-your_grade


#kom med tre föslag på ur du ska göra maximal chans att lyckas.
#1. fokusera på den klassen med flest kurser och högst aver score. 
#2. 
#3. Naive Bais? 
#Iterater över alla kurser

#Slh att höja sig i en viss kurs
def bayes(nbr_grade_in_classes, tot_nbr_of_grades_all_classes):

     #Om det inte finns några B i dina betyg exempelvis
     if nbr_grade_in_classes == 0:
          return 'x'

     #Slh att få MVG givet en viss kurs
     #P(MVG | kurs i) =     (antal VG i alla klasser som kursen tillhör) / (totala antalet kurser i alla klasser som kursen finns i)
     prob_grade_givven_course = nbr_grade_in_classes / tot_nbr_of_grades_all_classes

     if prob_grade_givven_course >= 1:

         
          return round(prob_grade_givven_course,2)
     elif prob_grade_givven_course < 0.05:
          return round(prob_grade_givven_course,2)
     else:
          return round(prob_grade_givven_course,2)


"""
          #För att kunna returnerna string + int måste vi göra om allt
          return "{} %".format(int(round(prob_grade_givven_course * 100,2))) 
     elif prob_grade_givven_course < 0.05:
          return "{} %".format(int(round(prob_grade_givven_course * 100,2)))
     else:
          return "{} %".format(int(round(prob_grade_givven_course * 100,2)))
"""




