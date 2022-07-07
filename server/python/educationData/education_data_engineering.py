

import pandas as pd
import json

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
 

def add_engi(education_name, school_name, class1, class2, class3, class4):

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

def iterate_engi():
  

  #Laterfilter so we only recomend unique educations, the one with the best match
  for ind in range(len(df["Utbildningens namn"])):
    #Add_engi school, then only save the unique schools in the database and all corresponding educations

    school_name = df["Univ/högskola"][ind]
    education_name = df["Utbildningens namn"][ind].lower()
    #print(education_name)


            #IVILINGeNJÖReR            #DATA
    if (("civil" in education_name) and ("data" in education_name or "ai" in education_name or "dator" in education_name or "intelli" in education_name or "robo" in education_name)):  
      
      class1 = ['data','naturvetenskap','mattefysik'] #   3 x 6% = 18%
      class2 = ['elektroteknik',"teknik", "IT"] # 2 x 5% = 10%
      #Currently we are only matching the "word" not the grade
      class3 = ["fysik 2","fysik b","matematik e","matematik 5", "matematik specialisering","programmering", "datavetenskap", "matematik breddning", "datorteknik", "mekatronik", "matematik breddning", 
      "dator nätverksteknik","projektledning","Nätverkssäkerhet"] # 5 x 10 = 50
      class4 = ["robotteknik", "multimediasystem", "ellära","teknik specialisering","gränssnittsdesign", "webbutveckling"] #Courses 4 *
      print(education_name)
      add_engi(education_name, school_name, class1, class2, class3 ,class4)

              #eLeKTRO MeKATRONIK
    if (("civil" in education_name) and ("elektro" in education_name or "meka" in education_name)):  
      class1 = ['data','naturvetenskap','mattefysik', "elektroteknik"] #   3 x 6% = 18%
      class2 = ['styrregleteknik',"teknik","processteknik"] # 2 x 5% = 10%
      class3 = ["fysik b","matematik e","fysik breddning","matematik 5","matematik specialisering","programmering", "datavetenskap", "matematik breddning", "datorteknik", "mekatronik", "matematik breddning", 
      "dator", "nätverksteknik", "elmätteknik", "elkraftteknik", "elektromekanik","högfrekvenskretsar", "elektronik mikrodatorteknik", "projektledning","mikrodatortillämpningar","programmerbara styrsystem",
      "mät och styrteknik","reglerteknik","distribuerande styrsystem"] # 5 x 10 = 50
      class4 = ["robotteknik", "multimediasystem", "ellära","teknik specialisering","högspänningsnät","transformatorstationer"] #Courses 4 *
      add_engi(education_name, school_name, class1, class2, class3, class4)

    #Marin teknik
    if (("civil" in education_name) and ("marin" in education_name)):  
      class1 = ['data','naturvetenskap','mattefysik', "elektroteknik","fordon"] #   3 x 6% = 18%
      class2 = ['styr regleteknik',"teknik","processteknik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","matematik specialisering","programmering", "datavetenskap", "matematik breddning", "datorteknik", "mekatronik", "matematik breddning", "dator", "nätverksteknik", "elmätteknik", "elkraftteknik", "elektromekanik","låg högfrekvenskretsar", "elektronik mikrodatorteknik", "projektledning","mikrodatortillämpningar","programmerbara styrsystem","mät,  reglerteknik","styrteknik","styrsystem"] # 5 x 10 = 50
      class4 = ["robotteknik", "multimediasystem", "ellära","teknik specialisering","högspänningsnät","transformatorstationer"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)
    
                #INFO KOMMUNIKATION IT
    if (("civil" in education_name) and ("info" in education_name or "mjukvaru" in education_name or "spel" in education_name)):  
      class1 = ['data','naturvetenskap', "it"] #   3 x 6% = 18%
      class2 = ['mattefysik',"teknik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","pedagogik", "matematik specialisering","programmering", "datavetenskap", "Informationsteknik", "datorteknik", "gränssnitt", "matematik breddning", 
      "gränssnittsdesign", "webbtjänster", "Webbserverprogrammering","webbutveckling","låg högfrekvenskretsar", "elektronik", "mikrodatorteknik", "Nätverksteknologier","medieteknik"] # 5 x 10 = 50
      class4 = ["robotteknik", "multimediasystem", "projektledning","medieproduktion","teknik specialisering","digitalt skapande","transformatorstationer","medier, samhälle  kommunikation",
      "photoshop","animation specialisering"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)
    
    if (("civil" in education_name) and ("säk" in education_name)):  
      class1 = ['data','naturvetenskap', "it",'mattefysik'] #   3 x 6% = 18%
      class2 = ["teknik", "juridik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","pedagogik", "matematik specialisering","programmering", "datavetenskap", "Informationsteknik", "datorteknik", "gränssnitt", "matematik breddning", 
      "gränssnittsdesign", "webbtjänster", "webbutveckling","elektronik mikrodatorteknik", "Nätverksteknologier", "rättskunskap","rätten samhället"] # 5 x 10 = 50
      class4 = ["multimediasystem", "projektledning","medieproduktion","teknik specialisering","medier"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3,class4)

    if (("civil" in education_name) and ("info" in education_name or "mjukvaru" in education_name)):  
      class1 = ['data','naturvetenskap', "it",'mattefysik'] #   3 x 6% = 18%
      class2 = ['entreprenörskap',"teknik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","pedagogik", "matematik specialisering","programmering", "datavetenskap", "Informationsteknik", "datorteknik", "gränssnitt", "matematik breddning", 
      "gränssnittsdesign", "webbtjänster", "webbutveckling","låg högfrekvenskretsar", "elektronik  mikrodatorteknik", "Nätverksteknologier","Informations medieteknik"] # 5 x 10 = 50
      class4 = ["robotteknik", "multimediasystem", "projektledning","medieproduktion","teknik specialisering","digitalt skapande","transformatorstationer","medier, samhälle  kommunikation",
      "photoshop","animation specialisering"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3,class4)

                  #INFO KOMMUNIKATION IT
    if (("civil" in education_name) and ("medie" in education_name)):  
      class1 = ['media','naturvetenskap', "it"] #   3 x 6% = 18%
      class2 = ['data',"teknik","journalistik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","pedagogik", "matematik specialisering","programmering", "datavetenskap", "Informationsteknik", "datorteknik", "gränssnitt", "matematik breddning" ,
      "projektledning", "dator nätverksteknik", "gränssnittsdesign", "webbtjänster", "webbutveckling","Medier, information  kommunikation", "tv produktion","film produktion", "Nätverksteknologier",
      "Informations medieteknik","ljudproduktion"] # 5 x 10 = 50
      class4 = ["robotteknik", "multimediasystem", "medieproduktion","teknik specialisering","digitalt skapande","kommunikation","administration av nätverks serverutrustning","photoshop",
      "animation specialisering","illustrator","musikproduktion","grafisk illustration","ljud  ljus"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3,class4)

                #DeSIGN / Interaktion
    if (("civil" in education_name) and ("design" in education_name)):  
      class1 = ['processteknik','naturvetenskap', "design"] #   3 x 6% = 18%
      class2 = ["teknik","tillverkning  konstruktion"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","tillverkningsteknik", "matematik specialisering","produktutveckling", "ritteknik", "konstruktion", "konstruktionsteknik", "gränssnitt","projektledning", 
      "matematik breddning 5", "produktionskunskap", "gränssnittsdesign", "Produktionsteknik", "produktionsutrustning","automationsteknik", "cad specialisering", "cad/cam","produktionsflöden", 
      "provning kontrollarbete","Informations medieteknik","ljudproduktion","formgivning","skissteknik","bild  form","bild"] # 5 x 10 = 50
      class4 = ["industritekniska processer", "cad","teknik specialisering","digitalt skapande","kommunikation","photoshop","animation specialisering","illustrator","grafisk illustration","ljud", "ljus",
      "utställningsdesign","visualisering","skissteknik","form","bild och form specialisering"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3,class4)
    
    if (("civil" in education_name) and ("arkitekt" in education_name )):  
      class1 = ['tillverkning  konstruktion',"arkitektur",'teknik', "design","mattefysik"] #   3 x 6% = 18%
      class2 = ["konst"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","matematik 5","tillverkningsteknik", "matematik specialisering","produktutveckling", "ritteknik", "konstruktion", "konstruktionsteknik", "produktion", 
      "matematik breddning 5","cad specialisering", "cad/cam","produktionsflöden", "arkitektur","formgivning","skissteknik","bild  form","bild","underhåll","husbyggnad","husbyggnadsprocessen"] # 5 x 10 = 50
      class4 = ["cad","teknik specialisering","digitalt skapande","kommunikation","photoshop","illustrator","grafisk illustration","utställningsdesign","visualisering","skissteknik","form",
      "bild och form specialisering"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3,class4)
    
                  #maskin/p
    if (("civil" in education_name) and ("produkt" in education_name )):  
      class1 = ['tillverkning konstruktion','teknik', "design","mattefysik"] #   3 x 6% = 18%
      class2 = ["processteknik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","matematik 5","tillverkningsteknik", "matematik specialisering","produktutveckling", "ritteknik", "konstruktion", "konstruktionsteknik", "produktion", "matematik breddning 5", "produktionskunskap", "Produktionsteknik", "produktionsutrustning","automationsteknik", "cad specialisering", "cad/cam","produktionsflöden", "provning kontrollarbete","robotteknik","formgivning","skissteknik","bild  form","bild","Produktionsutrustning","människan i industrin","processmätteknik","underhåll"] # 5 x 10 = 50
      class4 = ["industritekniska processer", "cad","teknik specialisering","digitalt skapande","kommunikation","photoshop","illustrator","grafisk illustration","utställningsdesign","visualisering","skissteknik","form","bild  form specialisering"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3,class4)

                  #maskin/p
    if (("civil" in education_name) and (("maskint" in education_name and "design" in education_name) or "prod" in education_name)):  
      class1 = ['processteknik','naturvetenskap',"styr  regleteknik","design","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","tillverkning  konstruktion"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","matematik","tillverkningsteknik", "matematik specialisering","produktutveckling", "ritteknik", "konstruktion", "konstruktionsteknik", "mät,  styrteknik", "matematik breddning 5", "produktionskunskap", "gränssnittsdesign", "Produktionsteknik", "produktionsutrustning","automationsteknik", "cad specialisering", "cad/cam","produktionsflöden", "provning  kontrollarbete","ljudproduktion","formgivning","skissteknik","bild  form","bild","robotik","mät,  reglerteknik","energiteknik","miljöch energikunskap"] # 5 x 10 = 50
      class4 = ["industritekniska processer", "cad","teknik specialisering","digitalt skapande","kommunikation","photoshop","animation specialisering","illustrator","utställningsdesign","visualisering","skissteknik","form","bild  form specialisering","distribuerande styrsystem"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3,class4)

      #maskin hållbar
    if (("civil" in education_name) and ("maskint" in education_name)):  
      class1 = ['processteknik','naturvetenskap',"styr  regleteknik","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","tillverkning  konstruktion","ekonomi"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","matematik 5","tillverkningsteknik", "matematik specialisering","produktutveckling", "ritteknik", "konstruktion", "konstruktionsteknik", "mät,  styrteknik", "matematik breddning 5", "produktionskunskap", "inköp  logistik", "Produktionsteknik", "produktionsutrustning","automationsteknik", "cad specialisering", "cad/cam","produktionsflöden", "provning  kontrollarbete","ljudproduktion","formgivning","skissteknik","ekonomi","robotik","mät,  reglerteknik"] # 5 x 10 = 50
      class4 = ["industritekniska processer", "cad","teknik specialisering","digitalt skapande","kommunikation","visualisering","skissteknik","form","bild  form specialisering","distribuerande styrsystem"] #Courses 4 *
      add_engi(education_name, school_name, class1, class2, class3,class4)
    
        #maskin fartyg
    if (("civil" in education_name) and ("farkost" in education_name or "rymd" in education_name)):  
      class1 = ['elektroteknik',"fordon",'teknik',"styr  regleteknik","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","tillverkning  konstruktion","data","miljö"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","programmering","matematik 5","tillverkningsteknik", "energiteknik","matematik specialisering","produktutveckling", "ritteknik", "konstruktion", "konstruktionsteknik", "mät,  styrteknik", "matematik breddning 5", "produktionskunskap", "Produktionsteknik", "produktionsutrustning","automationsteknik", "cad specialisering", "cad/cam","produktionsflöden", "provning  kontrollarbete","ljudproduktion","formgivning","skissteknik","ekonomi","robotik","mät,  reglerteknik","robotteknik","skeppsteknik"] # 5 x 10 = 50
      class4 = ["industritekniska processer", "cad","teknik specialisering","distribuerande styrsystem"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)
    
    #maskin samhällsteknik
    if (("civil" in education_name) and ("sam" in education_name)):  
      class1 = ['byggande/samhällsplanering','naturvetenskap',"samhällsteknik","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","miljö","ekonomi","entreprenörskap", "juridik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","matematik 5","tillverkningsteknik", "matematik specialisering","byggprocessen", "ritteknik", "inköp  logistik", "3D","hållbart samhällsbyggande","ekonomi", "matematik breddning 5", "entreprenörskap", "företagsekonomi specialisering", "konstruktionsteknik", "produktionsutrustning","automationsteknik","cad specialisering", "cad/cam", "formgivning","företagande","bild","miljöcertifierade hus","ledarskap  organisation","anläggning","juridik","Affärsjuridik","anläggningsprocessen","husbyggnadsprocessen","geografiska informationssystem"] # 5 x 10 = 50
      class4 = ["industritekniska processer", "cad","teknik specialisering","digitalt skapande","kommunikation","konstruktion","företagsekonomi","ritteknik","konstruktionsteknik","form","bild  form specialisering","politik  hållbar utveckling","husbyggnad","energiteknik","miljöch energikunskap","förnybar energi"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)

    if (("civil" in education_name) and ("lant" in education_name)):  
      class1 = ['byggande/samhällsplanering','juridik',"ekonomi","entreprenörskap","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","miljö","samhällsteknik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","matematik 5", "matematik specialisering","byggprocessen", "ritteknik", "inköp  logistik", "3D","hållbart samhällsbyggande","ekonomi",
       "matematik breddning", "entreprenörskap", "företagsekonomi specialisering","rättskunskap", "konstruktionsteknik","automationsteknik","cad specialisering", "cad/cam","företagande",
       "miljöcertifierade hus","ledarskap  organisation","anläggning","juridik","Affärsjuridik","anläggningsprocessen","husbyggnadsprocessen","geografiska informationssystem"] # 5 x 10 = 50
      class4 = ["cad","teknik specialisering","kommunikation","konstruktion","företagsekonomi","ritteknik","konstruktionsteknik","politik",  "hållbar","energiteknik",
      "miljöch energikunskap","förnybar energi"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)

    #maskin ekosystem
    if (("civil" in education_name) and ("ekos" in education_name or "energ" in education_name or "miljö" in education_name or "global" in education_name or "naturre" in education_name)): 
       
      class1 = ["miljö",'naturvetenskap',"samhällsteknik","ekologi","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","ekonomi","entreprenörskap","juridik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","projektledning","matematik 5","vindkraftnät", "matematik specialisering","byggprocessen", "ritteknik", "vattench processkemi","hållbart samhällsbyggande","förnybar energi",
       "matematik breddning 5","vatten- och miljöteknik","entreprenörskap", "företagsekonomi specialisering", "konstruktionsteknik", "produktionsutrustning","energiteknik","cad specialisering", "energikunskap","miljö", 
       "formgivning","bevarandebiologi","biologi i vattenmiljöer","företagande","dricksvatten","rening av förorenat vatten","miljöcertifierade hus","ledarskap  organisation","anläggning","juridik","affärsjuridik","anläggningsprocessen","husbyggnadsprocessen",
       "geografiska informationssystem","vattenreningens mikrobiologi","politik  hållbar utveckling"] # 5 x 10 = 50
      class4 = ["vattenvård","marken och växternas biologi","cad","teknik specialisering","kommunikation","konstruktion","företagsekonomi","skogsteknik","konstruktionsteknik","form",
      "landskapsvård","rätten"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)

    #maskin medicinteknik
    if (("civil" in education_name) and ("medicin" in education_name or "sjukhus" in education_name)):       
      class1 = ["data",'naturvetenskap',"it","medicinsk teknik","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","elektroteknik","entreprenörskap","styr  regleteknik","medicin"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","matematik specialisering","programmering", "datavetenskap", "matematik breddning", "datorteknik", "mekatronik",
      "dator nätverksteknik", "elmätteknik", "elektromedicinsk teknik", "elektromekanik","låg högfrekvenskretsar", "elektronik  mikrodatorteknik", "projektledning","mikrodatortillämpningar",
      "programmerbara styrsystem","reglerteknik","mät,  styrteknik","distribuerande styrsystem","Radiologiska utrustningar","bioteknik","Gas vätsketeknik","ergonomi","hemsjukvård","akutsjukvård"] # 5 x 10 = 50
      class4 = ["robotteknik","anatomi och fysiologi" ,"multimediasystem", "ellära","teknik specialisering","laboratorieteknik","provning  kontrollarbete","beteendevetenskap",] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)

    #bioteknik
    if (("civil" in education_name) and ("bio" in education_name or "kemi" in education_name)):       
      class1 = ["miljö",'naturvetenskap',"kemiiologi","mattefysik"] #   3 x 6% = 18%
      class2 = ["teknik","entreprenörskap","miljö","ekologi"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","matematik specialisering","programmering", "biologi", "matematik breddning", "matematik breddning", "processmätteknik", "processreglering", 
      "elektromekanik","bevarandebiologi" ,"projektledning","vattench processkemi","mät","reglerteknik","processdatorsystem","distribuerande styrsystem","bioteknik","Gas vätsketeknik","miljö energikunskap",
      "provning  kontrollarbete","kemi","livsmedels näringskunskap","vattenreningens mikrobiologi","kostvetenskap","medicin","vattenreningens mikrobiologi",""] # 5 x 10 = 50
      class4 = ["energiteknik","anatomi och fysiologi","teknik specialisering","biologi i vattenmiljöer","laboratorieteknik","ekonomi"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)
    
    #Nano
    if (("civil" in education_name) and ("nano" in education_name)):      
      class1 = ["mattefysik",'naturvetenskap',"kemiiologi","elektroteknik"] #   3 x 6% = 18%
      class2 = ["teknik","styr  regleteknik","miljö", "medicin"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","matematik specialisering","programmering", "biologi", "matematik breddning", "matematik breddning", "processmätteknik", 
      "processreglering", "elektromekanik", "projektledning","vattench processkemi","mät,  reglerteknik","processdatorsystem","distribuerande styrsystem","bioteknik",
      "Gas vätsketeknik","miljöch energikunskap","provning  kontrollarbete","kemi","livsmedels näringskunskap","kostvetenskap","medicin"] # 5 x 10 = 50
      class4 = ["energiteknik","teknik specialisering","laboratorieteknik","ekonomi"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)
    
    if (("civil" in education_name) and ("fysik" in education_name or "matematik" in education_name)):   
      class1 = ["styr  regleteknik",'naturvetenskap',"mattefysik","elektroteknik","data"] #   3 x 6% = 18%
      class2 = ["teknik","styr  regleteknik"] # 2 x 5% = 10%
      class3 = ["fysik 2","fysik b","matematik e","matematik 5","matematik specialisering","programmering", "fysik 3", "matematik breddning", "datorteknik","processmätteknik", "processreglering", 
      "elektromekanik", "projektledning","robotik","reglerteknik","processdatorsystem","distribuerande styrsystem","trådlösa radiosystem","mikrodatortillämpningar","låg högfrekvenskretsar"] # 5 x 10 = 50
      class4 = ["energiteknik","teknik specialisering","laboratorieteknik","ekonomi","elektronik  mikrodatorteknik","dator nätverksteknik"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)

          #maskin industriell ekommi
    if (("civil" in education_name) and ("ekonomi" in education_name)):  
      class1 = ['ledarskap','naturvetenskap',"ekonomi","mattefysik","entreprenörskap"] #   3 x 6% = 18%
      class2 = ["teknik","juridik", "it","data"] # 2 x 5% = 10%
      class3 = ["pedagogisk ledarskap","fysik b","matematik e","fysik 2","projektledning","matematik 5", "matematik specialisering","produktutveckling", "inköp", "logistik", 
      "administration", "ekonomi", "matematik breddning", "entreprenörskap", "företagsekonomi specialisering", "produktionsteknik", "produktionsutrustning","marknadsföring",
      "produktionsflöden","redovisning","företagande","ledarskap","organisation","försäljning","juridik","affärsjuridik","näthandel"] # 5 x 10 = 50
      class4 = ["teknik specialisering","kommunikation","företagsekonomi","privatjuridik","språk", "etnicitet och kulturmöten"] #Courses 4 *

      add_engi(education_name, school_name, class1, class2, class3, class4)
    
def create_engi():
  iterate_engi()

  return pd.DataFrame(data=education_class_dataFrame)

print(create_engi())



