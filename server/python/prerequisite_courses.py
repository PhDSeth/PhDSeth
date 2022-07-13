import pandas as pd
prerequisite_data = []
prerequisite_education = []

#Data för att kunna se vilken behörighet som krävs för en viss utbildning. 


# OBS Meritpoäng för områdeskurser tas bort 2022

 #   kurser som liger i samma []: å krävs det at båda kurserna uppnås

#--------------Här får vi reda på vilken omrdesbehörighet du har!--------------------------------------------
 #HUMANIORA, JURIDIK, TEOLOGI

points_for_basis = 2250

 #Används dels för att du ska kunna få fram din behörighet 
 #Ex: [["Engelska A"], ["Engelska 5"]] här måste antingen engelska A eller Engleksa 5 vara uppfyllda
 #Alt. 
prerequisite_data.append({"Områdesbehörighet" : "Grundläggande behörighet", "Kurser" : [["Engelska A"], ["Matematik A"], ['Svenska A'], ['Svenska B']],"Education":['Offentlig förvaltning och ledning', 'samhällsvetarprogrammet, Umeå universitet', 
'Teologiskt program', "Arkeologprogrammet", "Historikerprogrammet - kandidatexamen, Södertörns högskola (180 hp, 3 år)", "Globala studier - kandidatexamen, Linköpings universitet (180 hp, 3 år)", "Kommunikatörsprogrammet - kandidatexamen, Södertörns högskola (180 hp, 3 år)", "Programmet för kulturentreprenörskap - kandidatexamen, Umeå universitet (180 hp, 3 år)", 
"Europaprogrammet, Statsvetenskap - kandidatexamen, Göteborgs universitet (180 hp, 3 år)", "Europaprogrammet, Ekonomisk historia - kandidatexamen, Göteborgs universitet (180 hp, 3 år)","Europaprogrammet, Sociologi - kandidatexamen, Göteborgs universitet (180 hp, 3 år)", "Ekonomisk historia - kulturgeografi, Göteborgs universitet (180 hp, 3 år)", 
"Kandidatprogrammet i internationella relationer - kandidatexamen, Göteborgs universitet (180 hp, 3 år)", "Antropologprogrammet - kandidatexamen, Göteborgs universitet (180 hp, 3 år)", "Europaprogrammet, Idé- och lärdomshistoria - kandidatexamen, Göteborgs universitet (180 hp, 3 år)", "Kulturanalysprogrammet - kandidatexamen, Umeå universitet (180 hp, 3 år)", 
"Kulturanalys, inriktning hållbar utveckling - kandidatexamen, Södertörns högskola (180 hp, 3 år)", "Biblioteks- och informationsvetenskap - kandidatexamen, Linnéuniversitetet (180 hp, 3år)"]})


# courses in separate [] within a list ( [ ["Engelska 6"], ['Engelska B'] ]  ) means OR for example enegslak & OR engelska B
#cours in one [] ["samhällskunskap 1a1", "samhällskunskap 1a2"] means that both needs to be fullfilled

#Humaniora, Juridik och Teologi
#Use education list to sort out schools and educations from our database
# prerequisite_data.append({"Områdesbehörighet" : "A1", "Kurser" : [[["Historia 1b"], ["Historia 1a1", "Historia 1a2"], ["historia A"]], [['Samhällskunskap 1b'], ['Samhällskunskap 1a1', "Samhällskunskap 1a2"], ["Samhällskunskap A"]]], 
# 'Education':["juristprogrammet", "Rättsvetenskap", "Teologi", "Bebyggelseantikvariskt program", "kultur- och samhällsanalys", "Historia", "Arkeologi och antik historia", "Arkeologi", "Religionsvetenskap och teologi", "kultur", "samhälle och etnografi"]})

prerequisite_data.append({"Områdesbehörighet" : "1", "Kurser" : [ ["Historia A"], ["Samhällskunskap A"]], "Education":[]})

#Humaniora, Juridik och Teologi
#prerequisite_data.append({"Områdesbehörighet" : "A2 a", "Kurser" : [["Moderna språk"], [["Engelska 6"], ['Engelska B']]], 'Education':["Kulturvetarprogrammet - kandidatexamen, Stockholms universitet (180 hp, 3 år)", "Språk och politik - Inriktning engelska - kandidatexamen, Linnéuniversitetet (180 hp, 3 år)"]})

prerequisite_data.append({"Områdesbehörighet" : "2", "Kurser" : [["Engelska B"], ["Franska 3"]], 'Education':["Språk och politik - Inriktning franska"]})
prerequisite_data.append({"Områdesbehörighet" : "2", "Kurser" : [["Engelska B"], ["Tyska 3"]], 'Education':["Språk och politik - Inriktning franska"]})
prerequisite_data.append({"Områdesbehörighet" : "2", "Kurser" : [["Engelska B"], ["Spanska 3"]], 'Education':["Språk och politik - Inriktning franska"]})
prerequisite_data.append({"Områdesbehörighet" : "2", "Kurser" : [["Engelska B"], ["moderna språk 3"]], 'Education':["Språk och politik - Inriktning franska"]})


# prerequisite_data.append({"Områdesbehörighet" : "A2", "Kurser" : [[["Moderna språk"], ["tyska 3"]]], 'Education':["Språk och politik - Inriktning tyska - kandidatexamen, Linnéuniversitetet (180 hp, 3 år)"]})

# prerequisite_data.append({"Områdesbehörighet" : "A2", "Kurser" : [[["Moderna språk"], ["spanska 3"]]], 'Education':["Språk och politik - Inriktning spanska - kandidatexamen, Linnéuniversitetet (180 hp, 3 år)"]})

#Arkitektur och Naturresurser
# prerequisite_data.append({"Områdesbehörighet" : "A3", "Kurser" : [[["Matematik 3b"], ["matematik 3c"], ["matematik C"]], [["Naturkunskap B"],['Naturkunskap 2'], ['Biologi 1', 'Fysik 1a' ,'Kemi 1'], ['Biologi 1', 'Fysik 1b1', 'Fysik 1b2' ,'Kemi 1']], [["Samhällskunskap 1b"],["Samhällskunskap 1a1","Samhällskunskap 1a2"],["Samhällskunskap A"]]], 'Education':['Landskapsarkitekt', 'arkitekt', 'agronom']})
prerequisite_data.append({"Områdesbehörighet" : "3", "Kurser" : [ ["Naturkunskap B"], ["Samhällskunskap A"], ["Matematik C"]], "Education":[]})
prerequisite_data.append({"Områdesbehörighet" : "3", "Kurser" : [ ["Biologi A", "Kemi A", "Fysik A"], ["Samhällskunskap A"], ["Matematik C"]], "Education":[]})

#Beteendevetenskap, Ekonomi och Samhällsvetenskap
# prerequisite_data.append({"Områdesbehörighet" : "A4", "Kurser" : [[["Matematik 3b"], ["matematik 3c"], ["matematik C"]],[["Samhällskunskap 1b"],["Samhällskunskap 1a1","Samhällskunskap 1a2"],["Samhällskunskap A"]]],'Education':['psykolog', 'socionom', 'agronom']})
prerequisite_data.append({"Områdesbehörighet" : "4", "Kurser" : [ ["Engelska B"], ["Samhällskunskap A"], ["Matematik C"]], "Education":[]})

#Beteendevetenskap, Ekonomi och Samhällsvetenskap
# prerequisite_data.append({"Områdesbehörighet" : "A5", "Kurser" : [[["Matematik 2a"], ["Matematik 2b"], ["matematik 2c"], ["Matematik B"]], [["samhällskunskap 1b"], ["samhällskunskap A"], ["samhällskunskap 1a1", "samhällskunskap 1a2"]]],'Education':['psykolog', 'socionom', 'agronom', ]})
# prerequisite_data.append({"Områdesbehörighet" : "A5", "Kurser" : [[["Matematik 2a"], ["Matematik 2b"], ["matematik 2c"], ["Matematik B"]], [["samhällskunskap 1b"], ["samhällskunskap A"], ["samhällskunskap 1a1", "samhällskunskap 1a2"]]],'Education':['psykolog', 'socionom', 'agronom', ]})
prerequisite_data.append({"Områdesbehörighet" : "5", "Kurser" : [ ["Matematik B"], ["Samhällskunskap A"]], "Education":[]})


# prerequisite_data.append({"Områdesbehörighet" : "A6", "Kurser" : [[["samhällskunskap 1b"], ["samhällskunskap 1a1", "samhällskunskap 1a2"]], ["samhällskunskap A"]]})
prerequisite_data.append({"Områdesbehörighet" : "6", "Kurser" : [ ["Engelska B"], ["Samhällskunskap A"]], "Education":[]})

#Områdesbehörighet A6 b
# prerequisite_data.append({"Områdesbehörighet" : "A6 a", "Kurser" : [[["Naturkunskap 1b"], ["Naturkunskap 1a1", "Naturkunskap 1a2"],["Biologi 1", "Fysik 1a"], ["Fysik 1b1", "Fysik 1b2", "kemi 1"]], [["Samhällskunskap 1b"], ["Samhällskunskap 1a1", "Samhällskunskap 1a2"]]], "Education":[["Grundlärarprogrammet", "dalarna"]]})

#Områdesbehörighet Ac
# prerequisite_data.append({"Områdesbehörighet" : "A6 a", "Kurser" : [[["Naturkunskap 1b"], ["Naturkunskap 1a1", "Naturkunskap 1a2"],["Biologi 1", "Fysik 1a"], ["Fysik 1b1", "Fysik 1b2", "kemi 1"]], [["Samhällskunskap 1b"], ["Samhällskunskap 1a1", "Samhällskunskap 1a2"]]], "Education":["Förskollärare", "fritidshem", ["Grundlärarprogrammet", ]]})


#Områdesbehörighet A7
prerequisite_data.append({"Områdesbehörighet" : "7", "Kurser" : [ ["Matematik B"]], "Education":[]})



#Områdesbehörighet A8
prerequisite_data.append({"Områdesbehörighet" : "8", "Kurser" : [["Fysik B"], ["kemi A"], ["Matematik D"]], 'Education':["Högskoleingenjör", "Ortopedingenjör"]})

#Områdesbehörighet A9
prerequisite_data.append({"Områdesbehörighet" : "9", "Kurser" : [["Fysik B"], ["Kemi A"], ["Matematik E"]], 'Education':["Civilingenjör", "Brandingenjör"]})

#Områdesbehörighet A10
prerequisite_data.append({"Områdesbehörighet" : "10", "Kurser" : [["Biologi A"],["Fysik B"], ["kemi B"], ["Matematik E"]], 'Education':["Sjukhusfysikerprogrammet"]})
 
#Områdesbehörighet A11
prerequisite_data.append({"Områdesbehörighet" : "11", "Kurser" : [["Biologi B"], ["Fysik A"],["Kemi B"],["Matematik D"]], 'Education':["Jägmästarprogrammet", "Etologi och djurskydd", "Agronomprogrammet ", "Receptarieprogrammet"]})

#Områdesbehörighet A12
prerequisite_data.append({"Områdesbehörighet" : "12", "Kurser" : [["Biologi B"],["Fysik A"], ["Kemi B"], 
["Matematik C"]], 'Education':["Biomedicinsk analytiker", "Djurpsykologi"]})

#Områdesbehörighet A13
prerequisite_data.append({"Områdesbehörighet" : "13", "Kurser" : [ ["Biologi B"], ["Fysik B"], ["Kemi B"], ["Matematik D"]], 'Education':["Apotekarprogrammet", "Läkarprogrammet", "Optikerprogrammet", "tandläkarprogrammet", "Veterinärprogrammet"]})

#Områdesbehörighet A14
prerequisite_data.append({"Områdesbehörighet" : "14", "Kurser" : [["Biologi B"], ["Fysik A"], ["Kemi B"], ["Matematik D"]], "Education":["Arbetsterapeut", "audionom", "dietist", "Djursjukskötarprogrammet"]})

#Områdesbehörighet A15
prerequisite_data.append({"Områdesbehörighet" : "14", "Kurser" : [["Naturkunskap B"], ["Samhällskunskap A"],["Matematik B"]], "Education":["Arbetsterapeut", "audionom", "dietist", "Djursjukskötarprogrammet"]})
prerequisite_data.append({"Områdesbehörighet" : "14", "Kurser" : [["fysik A", "Kemi A", "Biologi A"], ["Samhällskunskap A"],["Matematik B"]], "Education":["Arbetsterapeut", "audionom", "dietist", "Djursjukskötarprogrammet"]})


def pre_edu(df1):
  pd.set_option('display.max_colwidth', None)

  df = pd.DataFrame(data = df1)
  
  return df

pre_edu(prerequisite_data)["Kurser"]
