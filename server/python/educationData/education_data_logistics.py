

import pandas as pd

  #class1: 15%
  #class2: 9%
  #class3: 12%
  #class4: 11%


#Autnumn
df = pd.read_excel (r'C:\Users\matti\Desktop\AppDev1\Pluggportalen_kod\Backend\database\statistik_data2.xlsx')

print(df)


#Later- filter so we only recomend unique educations, the one with the best match
for ind in range(len(df["Utbildningens namn"])):
  #Add school, then only save the unique schools in the database and all corresponding educations

  school_name = df["Univ/högskola"][ind]
  education_name = df["Utbildningens namn"][ind].lower()
  #print(education_name)
  
  if ("logistik" in education_name and "ekono" not in education_name ):

    education_class_dataFrame={"Education":[],
                                "Schools":[],
                                "class1":[],
                                "class2":[],
                                "class3":[],
                                "class4":[]}

    class1 = ['ekonomi','teknik'] #Classes
    class2 = ["beteende","juridik","samhällsvetenskap"] #Classes
    class3 = ["entreprenörskap","samhällskunskap","logistik","internationella relationer","inköp","ledarskap och organisation","branschkunskap inom handel och administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","programhantering","näthandel","projektledning"] #Courses
    class4 = ["politik och hållbar utveckling","administration","projektledning","redovisning","rättskunskap","företagsekonomi","information och kommunikation","branschkunskap inom handel"] #Courses
    interest = []



