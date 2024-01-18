#The below code is used to convert C# to json
''''import json
with open('sample_app.cs', 'r', encoding ='utf-8') as file:
       csharp_code = file.read()
class_info={
       "class name" : "sample_app",
       "code_snippet": csharp_code
}
json_data=json.dumps(class_info, indent =2)
with open('results.json', 'w', encoding='utf-8')as json_file:
       json_file.write(json_data)
print("Conversion complete")'''

#The below code is used to convert html to json
from bs4 import BeautifulSoup
import json

with open('index.html', 'r',encoding='utf-8')as file:
    html_content = file.read()
soup= BeautifulSoup(html_content,'html.parser')
class_info={
       "class name" : "index",
}
json_data={
    "html-content":str(soup)
}
with open('results1.json', 'w',encoding='utf-8')as json_file:
    json.dump(json_data, json_file, ensure_ascii= False, indent=2)
print("Conversion complete")