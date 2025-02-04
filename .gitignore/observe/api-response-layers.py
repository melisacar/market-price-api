import requests

url = "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c"
response = requests.get(url)
data = response.json()

print(data.keys())  
# OUTPUT: dict_keys(['endUserMessage', 'page', 'meta', 'paging', 'redirectTo'])
print(type(data["page"])) 
# <class 'list'>
print(len(data["page"]))
# 2
print(type(data["page"][0]))
# <class 'dict'>
print(type(data["page"][1]))
# <class 'dict'>
print(data["page"][0].keys())
# dict_keys(['$type', 'component', 'align', 'justify', 'hideOnBasketPage', 'backgroundColor', 'columns', 'screenMode', 'marginTop', 'marginBottom'])

print(type(data["page"][0]["columns"]))
# <class 'list'>
print(len(data["page"][0]["columns"]))
# 1
print(type(data["page"][0]["columns"][0]))
# <class 'dict'>
print(data["page"][0]["columns"][0].keys())
# dict_keys(['$type', 'content', 'mobileContent', 'span', 'mobileSpan', 'offset'])

print(type(data["page"][0]["columns"][0]["content"]))
# <class 'dict'>
print(len(data["page"][0]["columns"][0]["content"]))
# 6
print(data["page"][0]["columns"][0]["content"].keys())
# dict_keys(['$type', 'component', 'title', 'subTitle', 'breadcrumb', 'carousel'])

print(data["page"][0]["columns"][0]["content"]["component"])
# category-banner
print(type(data["page"][0]["columns"][0]["content"]))  
# <class 'dict'>
print(data["page"][0]["columns"][0]["content"].keys())  
# 
print(data["page"][0]["columns"][0]["content"].get("carousel"))  
# {'component': 'carousel', 'height': 180, 'borderRadius': None, 'autoPlay': True, 'campaigns': []}


print(data["page"][1].keys())
# dict_keys(['$type', 'component', 'justify', 'align', 'screenMode', 'columns'])dict_keys(['$type', 'component', 'justify', 'align', 'screenMode', 'columns'])
print(type(data["page"][1]["columns"]))
# <class 'list'>
print(type(data["page"][1]["component"]))
# <class 'str'>
