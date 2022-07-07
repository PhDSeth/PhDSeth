

import pandas as pd
import json

  #class1: 15%
  #class2: 9%
  #class3: 12%
  #class4: 11%


#Autnumn
df = pd.read_excel (r'C:\Users\matti\Desktop\AppDev1\Pluggportalen_kod\Backend\database\statistik_data2.xlsx')



education_class_dataFrame={"Education":[],
                              "Schools":[],
                              "class1":[],
                              "class2":[],
                              "class3":[],
                              "class4":[]}
 

def add_social(education_name, school_name, class1, class2, class3, class4):

  education_class_dataFrame["Education"].append(education_name)
  education_class_dataFrame["Schools"].append(school_name)
  education_class_dataFrame["class1"].append(class1)
  education_class_dataFrame["class2"].append(class2)
  education_class_dataFrame["class3"].append(class3)
  education_class_dataFrame["class4"].append(class4)

  return education_class_dataFrame

# 'def return_df():
#   data = add_social()
#   return data'

def iterate_social():
  

  #Later- filter so we only recomend unique educations, the one with the best match
  for ind in range(len(df["Utbildningens namn"])):
    #add_social school, then only save the unique schools in the database and all corresponding educations

    school_name = df["Univ/högskola"][ind]
    education_name = df["Utbildningens namn"][ind].lower()
    #print(education_name)

    #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("socio" in education_name):
      class1 = ['social',"omvårdnad", "barn/fritid"] #Classes
      class2 = ['pedagogik','samhällsvetenskap',"beteende","juridik"] #Classes
      class3 = ["vård- och omsorgsarbete","socialt arbete","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer", "lärande och utveckling","sociologi","etnicitet och kulturmöten","social omsorg","pedagogiskt ledarskap","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","aktivitetsledarskap","pedagogiska teorier och praktiker","friskvård och hälsa","hemsjukvård","rätts","psykiatri","människors miljöer","rättspsykiatri", "barnhälsovård", "vårdpedagogik och handledning","vård och omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("soci" in education_name and "psy" in education_name):
      class1 = ['social',"omvårdnad", "barn/fritid"] #Classes
      class2 = ['pedagogik','samhällsvetenskap',"beteende","juridik"] #Classes
      class3 = ["vård- och omsorgsarbete","socialt arbete","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer", "lärande och utveckling","sociologi","etnicitet och kulturmöten","social omsorg","pedagogiskt ledarskap","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","aktivitetsledarskap","pedagogiska teorier och praktiker","friskvård och hälsa","hemsjukvård","rätts","psykiatri","människors miljöer","rättspsykiatri", "barnhälsovård", "vårdpedagogik och handledning","vård och omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("soci" in education_name and "hållb" in education_name):
      class1 = ['social',"omvårdnad", "barn/fritid"] #Classes
      class2 = ['pedagogik','samhällsvetenskap',"beteende","juridik"] #Classes
      class3 = ["vård- och omsorgsarbete","socialt arbete","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer", "lärande och utveckling","sociologi","etnicitet och kulturmöten","social omsorg","pedagogiskt ledarskap","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","aktivitetsledarskap","pedagogiska teorier och praktiker","friskvård och hälsa","hemsjukvård","rätts","psykiatri","människors miljöer","rättspsykiatri", "barnhälsovård", "vårdpedagogik och handledning","vård och omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)

          #FIXA
    if ("soci" in education_name and "internatione" in education_name):
      class1 = ['social',"omvårdnad", "barn/fritid"] #Classes
      class2 = ['pedagogik','samhällsvetenskap',"beteende","juridik"] #Classes
      class3 = ["vård- och omsorgsarbete","socialt arbete","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer", "lärande och utveckling","sociologi","etnicitet och kulturmöten","social omsorg","pedagogiskt ledarskap","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","aktivitetsledarskap","pedagogiska teorier och praktiker","friskvård och hälsa","hemsjukvård","rätts","psykiatri","människors miljöer","rättspsykiatri", "barnhälsovård", "vårdpedagogik och handledning","vård och omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)
    
             #FIXA
    if ("omsorgsped" in education_name):
      class1 = ['social',"omvårdnad", "barn/fritid"] #Classes
      class2 = ['pedagogik','samhällsvetenskap',"beteende","juridik"] #Classes
      class3 = ["vård- och omsorgsarbete","socialt arbete","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer", "lärande och utveckling","sociologi","etnicitet och kulturmöten","social omsorg","pedagogiskt ledarskap","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","aktivitetsledarskap","pedagogiska teorier och praktiker","friskvård och hälsa","hemsjukvård","rätts","psykiatri","människors miljöer","rättspsykiatri", "barnhälsovård", "vårdpedagogik och handledning","vård och omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)

    #FIXA
    if ("arbetstera" in education_name):
      class1 = ['social',"omvårdnad", "barn/fritid"] #Classes
      class2 = ['pedagogik','samhällsvetenskap',"beteende","juridik"] #Classes
      class3 = ["vård- och omsorgsarbete","socialt arbete","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer", "lärande och utveckling","sociologi","etnicitet och kulturmöten","social omsorg","pedagogiskt ledarskap","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","aktivitetsledarskap","pedagogiska teorier och praktiker","friskvård och hälsa","hemsjukvård","rätts","psykiatri","människors miljöer","rättspsykiatri", "barnhälsovård", "vårdpedagogik och handledning","vård och omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)
    
    #FIXA
    if ("samhäll" in education_name and "kultur" in education_name):
      class1 = ['social',"omvårdnad", "barn/fritid"] #Classes
      class2 = ['pedagogik','samhällsvetenskap',"beteende","juridik"] #Classes
      class3 = ["vård- och omsorgsarbete","socialt arbete","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer", "lärande och utveckling","sociologi","etnicitet och kulturmöten","social omsorg","pedagogiskt ledarskap","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","aktivitetsledarskap","pedagogiska teorier och praktiker","friskvård och hälsa","hemsjukvård","rätts","psykiatri","människors miljöer","rättspsykiatri", "barnhälsovård", "vårdpedagogik och handledning","vård och omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)

       #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("samhällsanaly" in education_name or "Samhällsförändring" in education_name and "entreprenör" not in education_name):
      class1 = ['social',"genus", "samhällsvetenskap","kultur", "språk"] #Classes
      class2 = ['ekonomi',"beteende", "juridik"] #Classes
      class3 = ["etnicitet och kulturmöten","kultur- och idéhistoria","konstarterna och samhället","historia","socialt arbete","människors miljöer","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer","samtida kulturuttryck","religionskunskap","internationella relationer","lärande och utveckling","sociologi","social omsorg","kultur"] #Courses
      class4 = ["hälsopedagogik","barns lärande och växande","pedagogiska teorier och praktiker","geografi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)

      
       #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if (("samhällsanaly" in education_name or "Samhällsförändring" in education_name or "förändring" in education_name) and ("entreprenör" in education_name)):
      class1 = ['social',"ekonomi", "samhällsvetenskap","kultur", "språk","entreprenörskap"] #Classes
      class2 = ['genus',"beteende", "juridik"] #Classes
      class3 = ["etnicitet och kulturmöten","entreprenörskap","kultur- och idéhistoria","företagsekonomi","konstarterna och samhället","historia","socialt arbete","människors miljöer","barn- och ungdomshälsa","socialpedagogik"
      ,"ungdomskulturer","samtida kulturuttryck","religionskunskap","internationella relationer","lärande och utveckling","sociologi","social omsorg","kultur"] #Courses
      class4 = ["hälsopedagogik","entreprenörskap och företagande","barns lärande och växande","pedagogiska teorier och praktiker","geografi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)

      
    #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("personal" in education_name and "ledarskap" not in education_name):
      class1 = ['HR',"social", "samhällsvetenskap","beteende"] #Classes
      class2 = ["ekonomi","juridik", "språk"] #Classes
      class3 = ["administration","ledarskap", "administration – specialisering","personaladministration","textproduktion","affärskommunikation"] #Courses
      class4 = ["receptions- och konferensservice","ergonomi","friskvård och hälsa","marknadsföring","företagsekonomi","intern och extern kommunikation","entreprenörskap och företagande",
      "medier, samhälle och kommunikation","psykologi","svensk","engelska","information och kommunikation","människors miljöer", "visuell kommunikation"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)

          #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("personal" in education_name and "psyko" in education_name):
      class1 = ['HR',"social", "mental hälsa","beteende"] #Classes
      class2 = ["ekonomi","juridik", "omvårdnand"] #Classes
      class3 = ["administration", "psykologi","administration – specialisering","personaladministration","textproduktion","människors miljöer","affärskommunikation"] #Courses
      class4 = ["receptions- och konferensservice","ergonomi","friskvård och hälsa","marknadsföring","företagsekonomi","intern och extern kommunikation",
      "medier, samhälle och kommunikation","svensk","engelska","information och kommunikation", "visuell kommunikation","ledarskap"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)

      
    #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("kura" in education_name):
      class1 = ['medicin','naturvetenskap','kemibiologi',"omvårdnad", "mattefysik"] #Classes
      class2 = ['mental hälsa','medicinsk teknik',"fysisk hälsa","beteende"] #Classes
      class3 = ["vård- och omsorgsarbete","medicin","naturkunskap","Biologi Breddning","kemi 2","kemi 2","räddningsmedicin",
      "akutsjukvård","bioteknik","biologi b","biologi 2","barn- och ungdomssjukvård","barn- och ungdomshälsa"
      , "akut omhändertagande", "anatomi och fysiologi","naturvetenskaplig specialisering","hälsopedagogik","omvårdnad"] #Courses
      class4 = ["hälsopedagogik","friskvård och hälsa","hemsjukvård","radiologiska utrustningar","palliativ vård","psykiatri","rättspsykiatri", "barnhälsovård", "vård omsorg","filosofi"] #Courses
      interest = []

      add_social(education_name, school_name, class1, class2, class3, class4)


    

def create_social():
  iterate_social()

  return pd.DataFrame(data=education_class_dataFrame)



