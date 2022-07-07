

import pandas as pd

  #Class1: 15%
  #Class2: 9%
  #Class3: 12%
  #Class4: 11%


#Autnumn
df = pd.read_excel (r'C:\Users\matti\Desktop\AppDev1\Pluggportalen_kod\Backend\database\statistik_data2.xlsx')

print(df)


#Later- filter so we only recomend unique educations, the one with the best match
for ind in range(len(df["Utbildningens namn"])):
  #Add school, then only save the unique schools in the database and all corresponding educations

  school_name = df["Univ/högskola"][ind]
  education_name = df["Utbildningens namn"][ind].lower()
  #print(education_name)
  
  if ("fastig" in education_name):

    education_class_dataFrame={"Education":[],
                                "Schools":[],
                                "Class1":[],
                                "Class2":[],
                                "Class3":[],
                                "Class4":[]}

    Class1 = ['ekonomi','teknik'] #Classes
    Class2 = ["beteende","juridik","samhällsvetenskap"] #Classes
    Class3 = ["entreprenörskap","samhällskunskap","logistik","internationella relationer","inköp","ledarskap och organisation","branschkunskap inom handel och administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","programhantering","näthandel","projektledning"] #Courses
    Class4 = ["politik och hållbar utveckling","administration","projektledning","redovisning","rättskunskap","företagsekonomi","information och kommunikation","branschkunskap inom handel","försäljning"] #Courses
    interest = []

    education_class_dataFrame["Education"].append(education_name)
    education_class_dataFrame["Schools"].append(school_name)
    education_class_dataFrame["Class1"].append(Class1)
    education_class_dataFrame["Class2"].append(Class2)
    education_class_dataFrame["Class3"].append(Class3)
    education_class_dataFrame["Class4"].append(Class4)

  if ("fastig" in education_name and "rätts" in education_name):

    education_class_dataFrame={"Education":[],
                                "Schools":[],
                                "Class1":[],
                                "Class2":[],
                                "Class3":[],
                                "Class4":[]}

    Class1 = ['ekonomi','juridik'] #Classes
    Class2 = ["beteende","miljö","samhällsvetenskap"] #Classes
    Class3 = ["entreprenörskap","samhällskunskap","logistik","internationella relationer","inköp","ledarskap och organisation","branschkunskap inom handel och administration","privatjuridik","affärsjuridik","affärsutveckling och ledarskap","företagande","programhantering","fastighetsautomation","projektledning","rättskunskap","rätten och samhället"] #Courses
    Class4 = ["politik och hållbar utveckling","administration","projektledning","redovisning","rättskunskap","företagsekonomi","information och kommunikation","branschkunskap inom handel"] #Courses
    interest = []

    education_class_dataFrame["Education"].append(education_name)
    education_class_dataFrame["Schools"].append(school_name)
    education_class_dataFrame["Class1"].append(Class1)
    education_class_dataFrame["Class2"].append(Class2)
    education_class_dataFrame["Class3"].append(Class3)
    education_class_dataFrame["Class4"].append(Class4)
  
  if ("fastig" in education_name and "mäk" in education_name):

    education_class_dataFrame={"Education":[],
                                "Schools":[],
                                "Class1":[],
                                "Class2":[],
                                "Class3":[],
                                "Class4":[]}

    Class1 = ['ekonomi','juridik',"social"] #Classes
    Class2 = ["beteende","turism/service","samhällsvetenskap"] #Classes
    Class3 = ["entreprenörskap","samhällskunskap","ledarskap och organisation","branschkunskap inom handel och administration","affärsjuridik","affärsutveckling och ledarskap","företagande","programhantering","fastighetsautomation","projektledning","kommunikation","retorik","evenemang"] #Courses
    Class4 = ["konferens","administration","projektledning","redovisning","rättskunskap","företagsekonomi","information och kommunikation","branschkunskap inom handel","guide och reseledare","besöksnäring","internationella relationer","etnicitet och kulturmöten","konferens","försäljning"] #Courses
    interest = []

    education_class_dataFrame["Education"].append(education_name)
    education_class_dataFrame["Schools"].append(school_name)
    education_class_dataFrame["Class1"].append(Class1)
    education_class_dataFrame["Class2"].append(Class2)
    education_class_dataFrame["Class3"].append(Class3)
    education_class_dataFrame["Class4"].append(Class4)
  
  if ("mäk" in education_name and "fin" in education_name):

    education_class_dataFrame={"Education":[],
                                "Schools":[],
                                "Class1":[],
                                "Class2":[],
                                "Class3":[],
                                "Class4":[]}

    Class1 = ['ekonomi','juridik',"social"] #Classes
    Class2 = ["beteende","turism/service","samhällsvetenskap"] #Classes
    Class3 = ["entreprenörskap","samhällskunskap","ledarskap och organisation","branschkunskap inom handel och administration","affärsjuridik","affärsutveckling och ledarskap","företagande","programhantering","fastighetsautomation","projektledning","kommunikation","retorik","evenemang","praktisk marknadsföring","marknadsföring","intern och extern kommunikation","försäljning"] #Courses
    Class4 = ["konferens","administration","projektledning","redovisning","rättskunskap","företagsekonomi","information och kommunikation","branschkunskap inom handel","guide och reseledare","besöksnäring","internationella relationer","etnicitet och kulturmöten","konferens"] #Courses
    interest = []

    education_class_dataFrame["Education"].append(education_name)
    education_class_dataFrame["Schools"].append(school_name)
    education_class_dataFrame["Class1"].append(Class1)
    education_class_dataFrame["Class2"].append(Class2)
    education_class_dataFrame["Class3"].append(Class3)
    education_class_dataFrame["Class4"].append(Class4)





#ekonomi + historia
education_class_dataFrame.append({'Education':['Europaprogrammet, Ekonomisk historia GU', 'Samhällsanalysprogram i ekonomisk historia och kulturgeografi GU', 'Kandidatprogram i internationella relationer och ekonomisk historia sthlm'], 'Class1':['ekonomi','humaniora','kultur'], 'Class2':['samhällsvetenskap', 'social'], 'Class3':["ekonomi","historia","psykologi","geografi","sociologi", "fysik 2"], 'Class4':["ekonomi", "historia", "kultur", "genus", "miration"]})

#bank
education_class_dataFrame.append({'Education':['Ekonomprogrammet - Bank och finans kristianstad', 'Mäklarekonomprogrammet, fastighet och finans trollhättan' ], 'Class1':['ekonomi','humaniora','kultur'], 'Class2':['samhällsvetenskap', 'social'], 'Class3':["ekonomi","historia","psykologi","geografi","sociologi", "fysik 2"], 'Class4':["ekonomi", "historia", "kultur", "genus", "miration"]})

#Ekonomi + Fastighet /mäklare
education_class_dataFrame.append({'Education':['Fastighet och finans, kandidatutbildning KTH', 'Mäklarekonomprogrammet, fastighet och finans trollhättan', 'Bygg- och fastighetsekonomprogrammet halmstad', 'Fastighetsmäklarprogrammet gävle', 'Fastighetsekonomi karlstad' , 'Kandidatprogram, Fastighetsutveckling med fastighetsförmedling kth', 'Fastighetsmäklare luleå', 'Fastighetsförmedling malmö', 'Fastighetsföretagande malmö'], 'Class1':['ekonomi','humaniora','kultur'], 'Class2':['samhällsvetenskap', 'social'], 'Class3':["ekonomi","historia","psykologi","geografi","sociologi", "fysik 2"], 'Class4':["ekonomi", "historia", "kultur", "genus", "miration"]})


#ekonomi + mat
education_class_dataFrame.append({'Education':['Kostekonomi med inriktning mot ledarskap, kandidatprogram', ], 'Class1':['ekonomi','ledarskap','kultur'], 'Class2':['samhällsvetenskap', 'social'], 'Class3':["ekonomi","historia","psykologi","geografi","sociologi", "fysik 2"], 'Class4':["ekonomi", "historia", "kultur", "genus", "miration"]})

#logistik Informationslogistik
education_class_dataFrame.append({'Education':['Handelshögskolans logistikprogram gu', 'Industriell ekonomi - logistikingenjör borås', 'Samhällets logistik, kandidatprogram linköping', 'Flygtransport och logistik, kandidatprogram linköäping', 'Logistik och ekonomi södertörn', 'Civilekonomprogrammet med inriktning mot handel och logistik umeå' ], 'Class1':['ekonomi','ledarskap','kultur'], 'Class2':['samhällsvetenskap', 'social'], 'Class3':["ekonomi","historia","psykologi","geografi","sociologi", "fysik 2"], 'Class4':["ekonomi", "historia", "kultur", "genus", "miration"]})


#Nationalekonomi
education_class_dataFrame.append({'Education':['Europaprogrammet, Nationalekonomi GU', 'EKONOMI OCH PRODUKTIONSTEKNIK', 'Ekonomie kandidatprogrammet med inriktning nationalekonomi Södertörn', 'Filosofi, politik och ekonomi, ämnesinriktning nationalekonomi', 'Kandidatprogram i nationalekonomi och statistik STHLm'], 'Class1':['naturvetenskap','teknik','miljö'], 'Class2':['samhälle', 'ekonomi'], 'Class3':["ekonomi","internationella relationer","miljö-och energikunskap","matematik 4","fysik B", "fysik 2"], 'Class4':["miljö", "hållbarhet", "produktutveckling"]})

#Affärsutveckling
education_class_dataFrame.append({'Education':['Industriell ekonomi - arbetsorganisation och ledarskap Borås', 'EKONOMI OCH PRODUKTIONSTEKNIK', 'Civilingenjör i industriell ekonomi'], 'Class1':['naturvetenskap','teknik','miljö'], 'Class2':['samhälle', 'ekonomi'], 'Class3':["ekonomi","kemi","miljö-och energikunskap","matematik 4","redovisning", "fysik 2"], 'Class4':["miljö", "hållbarhet", "produktutveckling"]})

#--JURIDIK-------------------------------------------------------------------------------------------------------------
education_class_dataFrame.append({'Education':['Juristprogrammet', 'Rättsvetenskapligt", "skatterätt" och fastighetsrätt', 'Rättsvetenskap, kandidat, luleå', 'Rättsvetarprogrammet med internationell och digital inriktning örebro', 'Europaprogrammet, ämnesinriktning offentlig rätt'], 'Class1':['juridik','samhällsvetenskap','beteende'], 'Class2':['ekonomi', 'ledarskap'], 'Class3':["juridik","rättskunskap","Affärsjuridik","rätten och samhället","privatjuridik", "internationella relationer"], 'Class4':["juridik", "lagar", "människor"]})


#--JOURNALISTIK-------------------------------------------------------------------------------------------------------------
education_class_dataFrame.append({'Education_name':[], "School_name":[] , 'Class1':['juridik','samhällsvetenskap','mental hälsa'], 'Class2':['social', 'ledarskap'], 'Class3':["juridik","rättskunskap","Affärsjuridik","rätten och samhället","privatjuridik", "internationella relationer"], 'Class4':["juridik", "lagar", "människor"]})

print(education_class_dataFrame)


