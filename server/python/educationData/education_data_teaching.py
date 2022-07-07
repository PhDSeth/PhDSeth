

import pandas as pd

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
 

def add_teach(education_name, school_name, class1, class2, class3, class4):

  education_class_dataFrame["Education"].append(education_name)
  education_class_dataFrame["Schools"].append(school_name)
  education_class_dataFrame["class1"].append(class1)
  education_class_dataFrame["class2"].append(class2)
  education_class_dataFrame["class3"].append(class3)
  education_class_dataFrame["class4"].append(class4)

  return education_class_dataFrame


def iterate_teach():
  #Later- filter so we only recomend unique educations, the one with the best match
  for ind in range(len(df["Utbildningens namn"])):
    #Add school, then only save the unique schools in the database and all corresponding educations

    school_name = df["Univ/högskola"][ind]
    education_name = df["Utbildningens namn"][ind].lower()
    #print(education_name)


            #--------------------PEDAGOGIK------------------------------------------------------

    if (("häls" in education_name or "idrott" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  
    
      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','fysisk hälsa','social'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","aktivitetsledarskap","pedagogik", "beteendevetenskap", "fritids- och friskvårdsverksamheter","barns lärande och växande", "pedagogiska teorier och praktiker", "fritids- och idrottskunskap", "lärande och utveckling", "idrott och hälsa", "träningslära"] # 5 x 10 = 50
      class4 = ["fritids- och idrottskunskap", "människors miljöer", "kommunikation", "psykologi","hälsopedagogik", "ergonomi" ] #Courses 4 *


      add_teach(education_name, school_name, class1, class2, class3, class4)
  
    if (("mat" in education_name or "fysik" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *


      add_teach(education_name, school_name, class1, class2, class3, class4)
    
    if (("slöjd" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *


      add_teach(education_name, school_name, class1, class2, class3, class4)
    
    if (("idrott" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *


      add_teach(education_name, school_name, class1, class2, class3, class4)

    if (("idrott" in education_name and "biolog" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *

      add_teach(education_name, school_name, class1, class2, class3, class4)
    
    if (("idrott" in education_name and "histor" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *

      add_teach(education_name, school_name, class1, class2, class3, class4)
    
    if (("idrott" in education_name and "mate" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *

      add_teach(education_name, school_name, class1, class2, class3, class4)
    
    if ("idrott" in education_name and ("enge" in education_name or "svensk" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *

      add_teach(education_name, school_name, class1, class2, class3, class4)
    
        
    if ("samhäll" in education_name) and ("lära" in education_name or "pedagog" in education_name)):  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *

      add_teach(education_name, school_name, class1, class2, class3, class4)
  

    if "pedagogi" in education_name:  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *


      add_teach(education_name, school_name, class1, class2, class3, class4)
    
    if "förskol" in education_name:  

      education_class_dataFrame={"Education":[],
                                  "Schools":[],
                                  "class1":[],
                                  "class2":[],
                                  "class3":[],
                                  "class4":[]}
      
      class1 = ['pedagogik','naturvetenskap','matte-fysik'] #   3 x 6% = 18%
      class2 = ['samhällsvetenskap',"barn/fritid"] # 2 x 5% = 10%
      class3 = ["pedagogiskt ledarskap","matematik","pedagogik","projektledning", "matematik - specialisering","barns lärande och växande", "pedagogiska teorier och praktiker", "matematik breddning", "lärande och utveckling"] # 5 x 10 = 50
      class4 = ["människors miljöer", "kommunikation", "psykologi", "beteendevetenskap"] #Courses 4 *


      add_teach(education_name, school_name, class1, class2, class3, class4)


      


      

def create_social():
  iterate_social()

  return pd.DataFrame(data=education_class_dataFrame)


