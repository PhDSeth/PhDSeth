
import pandas as pd

  #class1: 15%
  #class2: 9%
  #class3: 12%
  #class4: 11%




df = pd.read_excel (r'C:\Users\matti\Desktop\AppDev1\Pluggportalen_kod\Backend\database\statistik_data2.xlsx')

  

education_class_dataFrame={"Education":[],
                              "Schools":[],
                              "class1":[],
                              "class2":[],
                              "class3":[],
                              "class4":[]}
 

def add_economy(education_name, school_name, class1, class2, class3, class4):

  education_class_dataFrame["Education"].append(education_name)
  education_class_dataFrame["Schools"].append(school_name)
  education_class_dataFrame["class1"].append(class1)
  education_class_dataFrame["class2"].append(class2)
  education_class_dataFrame["class3"].append(class3)
  education_class_dataFrame["class4"].append(class4)

  return education_class_dataFrame

# 'def return_df():
#   data = add_health()
#   return data'

def iterate_economy():

  # print(df)
  #Later- filter so we only recomend unique educations, the one with the best match
  for ind in range(len(df["Utbildningens namn"])):
    #Add school, then only save the unique schools in the database and all corresponding educations

    school_name = df["Univ/högskola"][ind]
    education_name = df["Utbildningens namn"][ind].lower()
    #print(education_name)
    
    #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("finans" in education_name):
      class1 = ['ekonomi','samhällsvetenskap','entreprenörskap'] #Classes
      class2 = ['juridik',"beteende"] #Classes
      class3 = ["sociologi","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","rätten samhället"] #Courses
      class4 = ["geografi", "entreprenörskap", "ledarskap och organisation","juridik","företagsekonomi"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)


    if ("nationalek" in education_name):
      class1 = ['ekonomi','samhällsvetenskap','språk',"social"] #Classes
      class2 = ['humanioria',"beteende"] #Classes
      class3 = ["sociologi","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","rätten samhället"] #Courses
      class4 = ["geografi", "entreprenörskap", "ledarskap och organisation","juridik","företagsekonomi"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

        #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("europa" in education_name and "före"):
      class1 = ['ekonomi','samhällsvetenskap','språk',"social"] #Classes
      class2 = ['humanioria',"beteende"] #Classes
      class3 = ["sociologi","företagsekonomi - specialisering","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","psykologi","rätten och samhället"] #Courses
      class4 = ["entreprenörskap", "ledarskap och organisation","juridik","företagsekonomi","branschkunskap inom handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

    
            #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("europa" in education_name and "nat"):
      class1 = ['ekonomi','samhällsvetenskap','språk',"social"] #Classes
      class2 = ['humanioria',"beteende"] #Classes
      class3 = ["sociologi","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","rätten och samhället","politik och hållbar utveckling","branschkunskap inom handel och administration"] #Courses
      class4 = ["geografi", "entreprenörskap", "ledarskap och organisation","branschkunskap inom handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
              #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("ekonomie" in education_name or "civilekonom" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap'] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","branschkunskap handel administration","privatjuridik","affärsjuridik","affärsutveckling ledarskap","företagande","affärskommunikation","programhantering"] #Courses
      class4 = ["kommunikation","politik hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","handel"]#Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

                #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("civilekonom" in education_name and "internationell" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("ekonom" in education_name and "ledarskap" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)

       #FIXA
    if ("ekonom" in education_name and "redovi" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("ekonom" in education_name and "hållbar" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("agrar" in education_name and "ekon" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("ekonom" in education_name and ("företag" in education_name and "etik" not in education_name and "kult" not in education_name)):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
  
    #FIXA
    if ("ekonom" in education_name and ("företag" in education_name and "etik" in education_name)):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("ekonom" in education_name and ("kultu" in education_name and "föret" in education_name)):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("ekonom" in education_name and ("kultu" in education_name and "konst" in education_name)):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("entrepre" in education_name and "medie" in education_name or "text" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
     #FIXA
    if ("entrepre" in education_name and "markn" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("filos" in education_name and "poli" in education_name and "ekon" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("filos" in education_name and "poli" in education_name and "nation" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)

      #FIXA
    if ("filos" in education_name and "poli" in education_name and "statsv" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
     #FIXA
    if ("interna" in education_name and "politik" in education_name and "ekonom" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
        #FIXA
    if ("econ" in education_name and "soc" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
         #FIXA
    if ("event" in education_name and "manag" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
            #FIXA
    if ("data" in education_name and "ekonom" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("politic" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("ekonom" in education_name and ("kultu" in education_name and "relig" in education_name)):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("textil" in education_name and "handel" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
        #FIXA
    if "affärssystem" in education_name:
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
    
   
    if ("skogsek" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("inter" in education_name and "affär" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
        #FIXA
    if ("handels" in education_name and "ekono" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("retail" in education_name and "manag" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
      #FIXA
    if ("digital" in education_name and ("verksam" in education_name or "affär" in education_name)):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
          #FIXA
    if ("medie" in education_name and "entre" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("marknadsfö" in education_name and "interna" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("logis" in education_name and "ekon" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("ekonomi" in education_name and "desi" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
      #FIXA
    if ("offent" in education_name and "förva" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
     
     #FIXA
    if ("industriell" in education_name and "organisa" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("sport" in education_name and "manag" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("market" in education_name and "manage" in education_name):
      class1 = ['ekonomi','entreprenörskap','ledarskap',"språk"] #Classes
      class2 = ['humanioria',"beteende","juridik","samhällsvetenskap"] #Classes
      class3 = ["entreprenörskap","samhällskunskap","humanistisk och samhällsvetenskaplig specialisering","internationella relationer","psykologi","ledarskap och organisation","administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","kinesiska","franska","tyska","spanska","moderna språk","italienska","ryska","japanska","mandarin","programhantering","affärskommunikation"] #Courses
      class4 = ["politik och hållbar utveckling","inköp","projektledning","redovisning","rättskunskap","kommunikation","information och kommunikation","handel"] #Courses
      interest = []
      add_economy(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("personal" in education_name and "ledarskap" in education_name):
      class1 = ['HR',"social", "samhällsvetenskap","beteende","ledarskap"] #Classes
      class2 = ["ekonomi","juridik", "språk"] #Classes
      class3 = ["administration","ledarskap", "administration – specialisering","personaladministration","textproduktion","affärskommunikation"] #Courses
      class4 = ["konferensservice","ergonomi","friskvård","marknadsföring","företagsekonomi","intern och extern kommunikation","entreprenörskap",
      "medier, samhälle och kommunikation","psykologi","svensk","engelska","pedagogisk ledarskap","information","människors", "kommunikation"] #Courses
      interest = []

      add_economy(education_name, school_name, class1, class2, class3, class4)
  
  return education_class_dataFrame


    

def create_economyl():
  iterate_economy()

  return pd.DataFrame(data=education_class_dataFrame)
