

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
 

def add_health(education_name, school_name, class1, class2, class3, class4):

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

def iterate_health():
  

  #Later- filter so we only recomend unique educations, the one with the best match
  for ind in range(len(df["Utbildningens namn"])):
    #Add_health school, then only save the unique schools in the database and all corresponding educations

    school_name = df["Univ/högskola"][ind]
    education_name = df["Utbildningens namn"][ind].lower()
    #print(education_name)

    #if ("Rätts" in education_name) or ("Jurist" in education_name) or ("Europaprogrammet" in education_name):
    if ("läkar" in education_name):
      class1 = ['medicin','naturvetenskap','kemibiologi',"omvårdnad","fysisk hälsa","mental hälsa"] #Classes 4 total
      class2 = ['medicinsk teknik',"beteende","mattefysik"] #Classes
      class3 = ["vård- och omsorgsarbete","medicin","naturkunskap","Biologi Breddning","kemi 2","kemi 2","räddningsmedicin","matematik",
      "akutsjukvård","bioteknik","biologi b","biologi 2","barn- och ungdomssjukvård","barn- och ungdomshälsa","hälso- och sjukvård", "akut omhändertagande", "anatomi och fysiologi","naturvetenskaplig specialisering","hälsopedagogik "] #Courses
      class4 = ["hälsopedagogik","människors miljöer","vård och omsorg – specialisering","grundläggande vård och omsorg","vårdpedagogik och handledning","friskvård och hälsa","hemsjukvård","radiologiska utrustningar","palliativ","psykiatri","rättspsykiatri", "barnhälsovård", "social omsorg","filosofi"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)

      
    if ("audionom" in education_name or "optiker" in education_name):
      class1 = ['medicin','naturvetenskap','social',"omvårdnad"] #Classes 4 total
      class2 = ['medicinsk teknik',"fysisk hälsa","beteende", "teknik","mattefysik"] #Classes
      class3 = ["social omsorg","vård- och omsorgsarbete","medicin","naturkunskap","Biologi Breddning","kemi 2","kemi 2","psykologi","matematik",
      "akutsjukvård","ergonomi","biologi b","biologi 2","barn- och ungdomssjukvård","barn- och ungdomshälsa","hälso- och sjukvård", "sociologi", "anatomi och fysiologi","naturvetenskaplig specialisering","hälsopedagogik"] #Courses
      class4 = ["samhällskunskap","hälsopedagogik","människors miljöer","vård och omsorg – specialisering","grundläggande vård och omsorg","vårdpedagogik och handledning","friskvård och hälsa","hemsjukvård","radiologiska utrustningar", "barnhälsovård","filosofi"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)


    if ("sjuksköt" in education_name and ('röntg' not in education_name and "djur" not in education_name)):
      class1 = ['medicin','naturvetenskap','teknik',"omvårdnad", "djur", "medicinsk teknik"] #Classes
      class2 = ["fysisk hälsa","ekologi", "naturbruk"] #Classes
      class3 = ["Radiologiska utrustningar","sällskapsdjur","hästkunskap","grundläggande vård och omsorg","medicin","naturkunskap","kemi 2","räddningsmedicin","lantbruksdjur",
      "akutsjukvård","anatomi och fysiologi","hundkunskap","biologi b","biologi 2","hälso- och sjukvård"
      ,"friskvård och hälsa","vård och omsorg – specialisering","akut omhändertagande", "naturvetenskaplig specialisering","vårdpedagogik och handledning"], #Courses
      class4 = ["biologi breddning","omsorg","filosofi","hemsjukvård"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("sjuksköt" in education_name and 'röntg' in education_name):
      class1 = ['medicin','naturvetenskap','teknik',"omvårdnad", "medicinsk teknik"] #Classes
      class2 = ["fysisk hälsa","mattefysik"] #Classes
      class3 = ["Radiologiska utrustningar","sällskapsdjur","hästkunskap","grundläggande vård och omsorg","medicin","naturkunskap","kemi 2","räddningsmedicin","lantbruksdjur",
      "akutsjukvård","anatomi och fysiologi","hundkunskap","biologi b","biologi 2","hälso- och sjukvård"
      ,"friskvård och hälsa","vård och omsorg – specialisering","akut omhändertagande", "naturvetenskaplig specialisering","vårdpedagogik och handledning"], #Courses
      class4 = ["biologi breddning","omsorg","filosofi","hemsjukvård"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)

            
    if ("sjuksköt" in education_name and 'djur' in education_name):
      class1 = ['medicin','naturvetenskap',"omvårdnad", "djur"] #Classes
      class2 = ["fysisk hälsa","ekologi", "naturbruk"] #Classes
      class3 = ["sällskapsdjur","hästkunskap","grundläggande vård och omsorg","medicin","naturkunskap","kemi 2","räddningsmedicin","lantbruksdjur",
      "akutsjukvård","anatomi och fysiologi","hundkunskap","biologi b","biologi 2","hälso- och sjukvård"
      ,"friskvård och hälsa","vård och omsorg – specialisering","akut omhändertagande", "naturvetenskaplig specialisering","vårdpedagogik och handledning"], #Courses
      class4 = ["biologi breddning","omsorg","filosofi","hemsjukvård"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("tand" in education_name and "läk" in education_name):
      class1 = ['medicin','fysisk hälsa','naturvetenskap','kemibiologi', "träning"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["laboratorieteknik","medicin","naturkunskap","biologi Breddning","kemi 2","kemi 2",
      "kemi specialisering","biologi b","biologi 2","kost, måltid och munhälsa","friskvård och hälsa"
       "idrott", "naturvetenskaplig specialisering","barn- och ungdomshälsa", "anatomi och fysiologi"] #Courses
      class4 = ["hälsopedagogik", "barnhälsovård", "vård omsorg","bioteknik","komplementärmedicin","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
      #FIXA
    if ("tand" in education_name and "hyg" in education_name):
      class1 = ['medicin','fysisk hälsa','naturvetenskap','kemibiologi', "träning"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["laboratorieteknik","medicin","naturkunskap","biologi Breddning","kemi 2","kemi 2",
      "kemi specialisering","biologi b","biologi 2","kost, måltid och munhälsa","friskvård och hälsa"
       "idrott", "naturvetenskaplig specialisering","barn- och ungdomshälsa", "anatomi och fysiologi"] #Courses
      class4 = ["hälsopedagogik", "barnhälsovård", "vård omsorg","bioteknik","komplementärmedicin","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("tand" in education_name and "tek" in education_name):
      class1 = ['medicin','fysisk hälsa','naturvetenskap','kemibiologi', "träning"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["laboratorieteknik","medicin","naturkunskap","biologi Breddning","kemi 2","kemi 2",
      "kemi specialisering","biologi b","biologi 2","kost, måltid och munhälsa","friskvård och hälsa"
       "idrott", "naturvetenskaplig specialisering","barn- och ungdomshälsa", "anatomi och fysiologi"] #Courses
      class4 = ["hälsopedagogik", "barnhälsovård", "vård omsorg","bioteknik","komplementärmedicin","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
      
    if ("logoped" in education_name):
      class1 = ['medicin','naturvetenskap','social',"beteende","mental hälsa"] #Classes
      class2 = ['pedagogik',"teknik","språk","Beteendevetenskap"] #Classes
      class3 = ["kommunikation","medicin","naturkunskap","biologi Breddning","pedagogisk",
      "omsorg","biologi b","biologi 2","kost, måltid och munhälsa","psykologi","kemi"
       "naturvetenskaplig specialisering","barn- och ungdomshälsa", "anatomi och fysiologi"] #Courses
      class4 = ["hälsopedagogik", "barnhälsovård", "vård omsorg","bioteknik","komplementärmedicin","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("biomedicin" in education_name):
      class1 = ['medicin','fysisk hälsa','naturvetenskap','kemibiologi', "träning"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["laboratorieteknik","naturkunskap","biologi Breddning","kemi 2","kemi 2","bioteknik",
      "kemi specialisering","biologi b","biologi 2","idrottsspecialisering","idrottsledarskap"
       "idrott", "idrottsledarskap", "naturvetenskaplig specialisering","barn- och ungdomshälsa"] #Courses
      class4 = ["hälsopedagogik","medicin", "barnhälsovård", "vård omsorg","vatten- och miljöteknik","anatomi och fysiologi"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("biomedicin" in education_name) and ("träning" in education_name):
      class1 = ['medicin','fysisk hälsa','naturvetenskap','kemibiologi', "träning"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["laboratorieteknik","naturkunskap","biologi Breddning","kemi 2","kemi 2","bioteknik",
      "kemi specialisering","biologi b","biologi 2","idrottsspecialisering","idrottsledarskap"
       "idrott", "idrottsledarskap", "naturvetenskaplig specialisering","barn- och ungdomshälsa"] #Courses
      class4 = ["hälsopedagogik","medicin", "barnhälsovård", "vård omsorg","vatten- och miljöteknik","anatomi och fysiologi"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("biomedicin" in education_name) and ("klinisk" in education_name):
      class1 = ['medicin','fysisk hälsa','naturvetenskap','kemibiologi', "träning"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["laboratorieteknik","naturkunskap","biologi Breddning","kemi 2","kemi 2",
      "kemi specialisering","bioteknik","biologi b","biologi 2","idrottsspecialisering","idrottsledarskap"
       "idrott", "idrottsledarskap", "naturvetenskaplig specialisering","barn- och ungdomshälsa"] #Courses
      class4 = ["hälsopedagogik","medicin", "barnhälsovård", "vård omsorg","vatten- och miljöteknik","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("biomedicin" in education_name) and ("laborat" in education_name):
      class1 = ['medicin','fysisk hälsa','naturvetenskap','kemibiologi', "träning"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["laboratorieteknik","naturkunskap","biologi Breddning","kemi 2","kemi 2",
      "kemi specialisering","bioteknik","biologi b","biologi 2","idrottsspecialisering","idrottsledarskap"
       "idrott", "idrottsledarskap", "naturvetenskaplig specialisering","barn- och ungdomshälsa"] #Courses
      class4 = ["hälsopedagogik","medicin", "barnhälsovård", "vård omsorg","vatten- och miljöteknik","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("apotek" in education_name):
      class1 = ['medicin','naturvetenskap','kemibiologi',"mattefysik"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["vård- och omsorgsarbete","naturkunskap","Biologi Breddning","kemi 2","kemi 2","laboratorieteknik",
      "akutsjukvård","bioteknik","biologi b","biologi 2", "naturvetenskaplig specialisering",
      "komplementärmedicin","medicin"] #Courses
      class4 = ["hälsopedagogik", " friskvård och hälsa", "barnhälsovård", "vård omsorg","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("recept" in education_name):
      class1 = ['medicin','naturvetenskap','kemibiologi',"mattefysik"] #Classes
      class2 = ['medicinsk teknik'] #Classes
      class3 = ["vård- och omsorgsarbete","naturkunskap","Biologi Breddning","kemi 2","kemi 2","laboratorieteknik",
      "akutsjukvård","bioteknik","biologi b","biologi 2", "naturvetenskaplig specialisering",
      "komplementärmedicin","medicin"] #Courses
      class4 = ["hälsopedagogik", " friskvård och hälsa", "barnhälsovård", "vård omsorg","grundläggande vård och omsorg"] #Courses
      interest = []
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("kost" in education_name or "livsmedel" in education_name):  
      class1 = ['mat och hälsa','beteende','mat och nutrion'] 
      class2 = ['fysisk hälsa',"pedagogik","social"] 
      class3 = ["rätten samhället","hälsopedagogik","kemi","kemi 2","biologi 2","biologi", "kostvetenskap"] 
      class4 = ["psykologi", "barnhälsovård", "Livsmedels- och näringskunskap", "träningslära", "kost och hälsa",
       "idrott och hälsa"] 
      add_health(education_name, school_name, class1, class2, class3, class4)
      
    if ("kost" in education_name and "leda" in education_name):  
      class1 = ['mat och hälsa','beteende','mat och nutrion'] 
      class2 = ['fysisk hälsa',"pedagogik","social"] 
      class3 = ["rätten samhället","hälsopedagogik","kemi","kemi 2","biologi 2","biologi", "kostvetenskap"] 
      class4 = ["psykologi", "barnhälsovård", "Livsmedels- och näringskunskap", "träningslära", "kost och hälsa",
       "idrott och hälsa"] 
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("häls" in education_name and "samh" in education_name):  
      class1 = ['mat och hälsa','beteende','mat och nutrion'] 
      class2 = ['fysisk hälsa',"pedagogik","social"] 
      class3 = ["rätten samhället","hälsopedagogik","kemi","kemi 2","biologi 2","biologi", "kostvetenskap"] 
      class4 = ["psykologi", "barnhälsovård", "Livsmedels- och näringskunskap", "träningslära", "kost och hälsa",
       "idrott och hälsa"] 
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("häls" in education_name and "psy" in education_name):  
      class1 = ['mat och hälsa','beteende','mat och nutrion'] 
      class2 = ['fysisk hälsa',"pedagogik","social"] 
      class3 = ["rätten samhället","hälsopedagogik","kemi","kemi 2","biologi 2","biologi", "kostvetenskap"] 
      class4 = ["psykologi", "barnhälsovård", "Livsmedels- och näringskunskap", "träningslära", "kost och hälsa",
       "idrott och hälsa"] 
      add_health(education_name, school_name, class1, class2, class3, class4)

    #fixa
    if ("häls" in education_name and "medi" in education_name):  
      class1 = ['mat och hälsa','beteende','mat och nutrion'] 
      class2 = ['fysisk hälsa',"pedagogik","social"] 
      class3 = ["rätten samhället","hälsopedagogik","kemi","kemi 2","biologi 2","biologi", "kostvetenskap"] 
      class4 = ["psykologi", "barnhälsovård", "Livsmedels- och näringskunskap", "träningslära", "kost och hälsa",
       "idrott och hälsa"] 
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("häls" in education_name and "folk" in education_name):  
      class1 = ['beteende',"samhällsvetenskap", "social", "kultur"] 
      class2 = ['fysisk hälsa',"medicin",'mat och hälsa',"mental hälsa","juridik"] 
      class3 = ["historia","sociologi","rätten samhället","hälsopedagogik","kommunikation","hälsopedagogik", "kostvetenskap","samhällskunskap"] 
      class4 = ["psykologi", "barnhälsovård", "Livsmedels- och näringskunskap", "träningslära", "kost och hälsa",
       "idrott och hälsa","politik hållbar utveckling","geografi","människan","pedagogik"] 
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("häls" in education_name and ("folk" in education_name and "peda" in education_name)):  
      class1 = ['beteende',"samhällsvetenskap", "social", "pedagogik", "kultur"] 
      class2 = ['fysisk hälsa',"medicin",'mat och hälsa',"mental hälsa","juridik"] 
      class3 = ["historia","sociologi","rätten samhället","hälsopedagogik","kommunikation","pedagogik","hälsopedagogik", "kostvetenskap","samhällskunskap"] 
      class4 = ["psykologi", "barnhälsovård", "Livsmedels- och näringskunskap", "träningslära", "kost och hälsa",
       "idrott och hälsa","politik hållbar utveckling","geografi","människan"] 
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("häls" in education_name and "coa" in education_name):  
      class1 = ["träning",'barn/fritid','fysisk hälsa',"ledarskap"] 
      class2 = ['mental hälsa',"pedagogik","social",'mat och nutrion',"entreprenörskap"] 
      class3 = ["projektledning","hälsopedagogik","ergonomi","träningslära","idrott","tävlingslära","idrottsledarskap","pedagogiskt ledarskap","friskvård och hälsa","aktivitetsledarskap","fritids idrottskunskap","fritids och friskvårdsverksamheter",
       "kostvetenskap", "matlagning – specialisering","biologi", "kemi", "anatomi och fysiologi","naturkunskap","kost och hälsa","specialkoster","matlagning"] #Courses
      class4 = ["idrottsspecialisering","psykologi", "kost, måltid och munhälsa","barnhälsovård","sociologi","Livsmedels näringskunskap", "träningslära", "biologi"] #Courses  
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("hälso" in education_name and "kost") or ("idrott" in education_name) or ("nutrition" in education_name):  
      class1 = ['barn/fritid','fysisk hälsa','mat och nutrion',"mat hälsa"] 
      class2 = ["idrottsspecialisering",'mental hälsa',"pedagogik","social"] 
      class3 = ["näringskunskap","livsmedel","kost","hälsopedagogik","kostvetenskap","ergonomi","träningslära","idrott","tävlingslära","idrottsledarskap","pedagogiskt ledarskap","friskvård och hälsa","aktivitetsledarskap","fritids idrottskunskap","fritids och friskvårdsverksamheter",
       "kostvetenskap", "matlagning – specialisering","biologi", "kemi", "anatomi och fysiologi","naturkunskap","kost och hälsa","specialkoster","matlagning"] #Courses
      class4 = ["psykologi", "kost, måltid och munhälsa","barnhälsovård","sociologi","Livsmedels näringskunskap", "träningslära", "biologi"] #Courses  
      add_health(education_name, school_name, class1, class2, class3, class4)
  
    if ("hälsopr" in education_name):  
      class1 = ["träning",'barn/fritid','fysisk hälsa'] 
      class2 = ['mental hälsa',"pedagogik","social",'mat och nutrion'] 
      class3 = ["hälsopedagogik","ergonomi","träningslära","idrott","tävlingslära","idrottsledarskap","pedagogiskt ledarskap","friskvård och hälsa","aktivitetsledarskap","fritids idrottskunskap","fritids och friskvårdsverksamheter",
       "kostvetenskap", "matlagning – specialisering","biologi", "kemi", "anatomi och fysiologi","naturkunskap","kost och hälsa","specialkoster","matlagning"] #Courses
      class4 = ["idrottsspecialisering","psykologi", "kost, måltid och munhälsa","barnhälsovård","sociologi","Livsmedels näringskunskap", "träningslära", "biologi"] #Courses  
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("hälsoped" in education_name):  
      class1 = ["träning",'barn/fritid','fysisk hälsa',"pedagogik"] 
      class2 = ['mental hälsa',"beteende","social","'mat och nutrion'"] 
      class3 = ["hälsopedagogik","ergonomi","träningslära","idrott","tävlingslära","idrottsledarskap","pedagogiskt ledarskap","friskvård och hälsa","aktivitetsledarskap","fritids idrottskunskap","fritids och friskvårdsverksamheter",
       "kostvetenskap", "matlagning – specialisering","biologi", "kemi", "anatomi och fysiologi","naturkunskap","kost och hälsa","specialkoster","matlagning"] #Courses
      class4 = ["idrottsspecialisering","psykologi", "kost, måltid och munhälsa","barnhälsovård","sociologi","Livsmedels näringskunskap", "träningslära", "biologi"] #Courses  
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("psykolog" in education_name or "beteende" in education_name or "kognitions" in education_name):  
      class1 = ['beteende','mental hälsa','social'] #   3 x 6% = 18%
      class2 = ['pedagogik',"medicin", "språk", "omvårdnad"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","psykologi","Beteendevetenskap", "mental träning","socialpedagogik"] # 5 x 10
      class4 = ["biologi", "människors miljöer","rättspsykiatri","kommunikation","ungdomskulturer","social omsorg","hälso- och sjukvård","medicin","pedagogik","hälsopedagogik","friskvård och hälsa"] #Courses 4 *
      add_health(education_name, school_name, class1, class2, class3, class4)

      
    if ("psykolog" in education_name and "idrott" in education_name):  
      class1 = ['beteende','mental hälsa','social',"fysisk hälsa", "träning"] #   3 x 6% = 18%
      class2 = ['pedagogik',"medicin", "språk", "omvårdnad"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","träningslära","idrott","barn- och ungdomshälsa","fritids","psykologi","Beteendevetenskap", "mental träning","socialpedagogik"] # 5 x 10
      class4 = ["biologi", "människors miljöer","rättspsykiatri","kommunikation","lärande och utveckling","ungdomskulturer","social omsorg","hälso- och sjukvård","medicin","pedagogik","hälsopedagogik","friskvård och hälsa"] #Courses 4 *
      add_health(education_name, school_name, class1, class2, class3, class4)
          
    if ("psykolog" in education_name and "djur" in education_name):  
      class1 = ['beteende','mental hälsa','ekologi',"djur"] #   3 x 6% = 18%
      class2 = ['naturbruk',"medicin", "social"] # 2 x 5% = 10%
      class3 = ["djurhållning","psykologi","Beteendevetenskap", "mental träning","sällskapsdjur","djurvård","hundkunskap"] # 5 x 10
      class4 = ["biologi","kommunikation","ungdomskulturer","djurens biologi","medicin"] #Courses 4 *
      add_health(education_name, school_name, class1, class2, class3, class4)
    
    if ("fysiotera" in education_name):  
      class1 = ["fysisk hälsa","träning"] #   3 x 6% = 18%
      class2 = ["mental hälsa","naturvetenskap","mat hälsa","omvårdnad","medicin","mat nutrion"] # 2 x 5% = 10%
      class3 = ["idrottsspecialisering","vårdpedagogik","tävlingslära","ungdomshälsa","träningslära","ergonomi","idrott","aktivitetsledarskap","pedagogik","kommunikation","psykologi","anatomi fysiologi","Beteendevetenskap","hälsopedagogik"] # 5 x 10 = 50
      class4 = ["mental träning","massage","idrottsledarskap","kostvetenskap","biologi","hälso- och sjukvård","social omsorg","socialpedagogik","sjukvård","hälsopedagogik","friskvård"] #Courses 4 *
      add_health(education_name, school_name, class1, class2, class3, class4)

    if ("dietis" in education_name):  
      class1 = ['beteende',"omvårdnad","medicin","mental hälsa","mat hälsa",'social',"mat nutrion"] #   3 x 6% = 18%
      class2 = ["fysisk hälsa","naturvetenskap"] # 2 x 5% = 10%
      class3 = ["specialkoster","kostvetenskap","Livsmedels","anatomi fysiologi","Beteendevetenskap","munhälsa","hälsopedagogik","sociologi"] # 5 x 10 = 50
      class4 = ["psykologi","psykiatri","biologi","hälso- och sjukvård","social omsorg","socialpedagogik","sjukvård","hälsopedagogik","friskvård"] #Courses 4 *
      add_health(education_name, school_name, class1, class2, class3, class4)



    

def create_health():
  iterate_health()

  return pd.DataFrame(data=education_class_dataFrame)



