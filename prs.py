import json
from bs4 import BeautifulSoup
import requests

url = "https://habr.com/ru/all/"

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'
}

req = requests.get(url, headers=headers)
src = req.text
# # print(src)   #for_testing
#
# with open("index.html", "w") as file:      #saving_code_to_file
#     file.write(src)


# with open("index.html") as file:            #using_saved_file
#     src = file.read()
#
soup = BeautifulSoup(src, 'lxml')
all_products_href = soup.find_all(class_="tm-articles-list__item")

all_categories_dict = {}
for item in all_products_href:
    item_text = item.text
    item_href = "https://habr.com/ru/all/"

    all_categories_dict[item_text] = item_href

with open("news/habr/all_categories_dict.json", "w")as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


