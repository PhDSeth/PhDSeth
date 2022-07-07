

import pandas as pd

  #class1: 15%
  #class2: 9%
  #class3: 12%
  #class4: 11%


#Autnumn
df = pd.read_excel (r'C:\Users\matti\Desktop\AppDev1\Pluggportalen_kod\backend\database\statistik_data2.xlsx')


education_class_dataFrame={"Education":[],
                              "Schools":[],
                              "class1":[],
                              "class2":[],
                              "class3":[],
                              "class4":[]}
 

def add_geology(education_name, school_name, class1, class2, class3, class4):

  education_class_dataFrame["Education"].append(education_name)
  education_class_dataFrame["Schools"].append(school_name)
  education_class_dataFrame["class1"].append(class1)
  education_class_dataFrame["class2"].append(class2)
  education_class_dataFrame["class3"].append(class3)
  education_class_dataFrame["class4"].append(class4)

  return education_class_dataFrame

# 'def return_df():
#   data = add_engi()
#   return data'


def iterate_geology():

  #Later- filter so we only recomend unique educations, the one with the best match
  for ind in range(len(df["Utbildningens namn"])):
    #Add school, then only save the unique schools in the database and all corresponding educations

    school_name = df["Univ/högskola"][ind]
    education_name = df["Utbildningens namn"][ind].lower()
    #print(education_name)
    
    if ("geov" in education_name or "geol" in education_name):

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}

      class1 = ['miljö',"ekologi",'kemi-biologi'] #Classes
      class2 = ["naturbruk","naturvetenskap"] #Classes
      class3 = ["naturvetenskap","växtodling","växtkunskap","vattenvård","bevarandebiologi","marken och växternas biologi","vatten-och processkemi","miljö-och energikunskap","geografi","kemi","biologi"] #Courses
      class4 = ["politik och hållbar utveckling","bioteknik","geografiska informationssystem","geografi","fysik"] #Courses
      interest = []

      add_geology(education_name, school_name, class1, class2, class3, class4)

    if ("arkeo" in education_name):

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}

      class1 = ['naturvetenskap',"kemi-biologi",'miljö', "humanioria"] #Classes
      class2 = ["byggande/samhällsplanering"] #Classes
      class3 = ["naturvetenskap","historia","religion","vattenvård","bevarandebiologi","geografi","vatten-och processkemi","miljö-och energikunskap","geografi","kemi","biologi"] #Courses
      class4 = ["politik","miljö","geografiska informationssystem","geografi"] #Courses
      interest = []

      education_class_dataFrame["Education"].append(education_name)
      education_class_dataFrame["Schools"].append(school_name)
      education_class_dataFrame["class1"].append(class1)
      education_class_dataFrame["class2"].append(class2)
      education_class_dataFrame["class3"].append(class3)
      education_class_dataFrame["class4"].append(class4)

  

def create_geology():
  iterate_geology()

  return pd.DataFrame(data=education_class_dataFrame)

print(create_geology())
