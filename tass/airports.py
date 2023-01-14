from bs4 import BeautifulSoup
import requests
import re
import openpyxl

wb = openpyxl.load_workbook(r'flight_data\airports.xlsx')
sheet = wb.active

temp=1
for i in range (1, 1124):
    temp += 1
    print(temp)
    cell_read = "F"+str(temp)
    cell_write = "J" + str(temp)
    url_param = sheet[cell_read].value

    url = "https://www.google.com/search?q=" + url_param
    cookies = {"CONSENT":"YES+shp.gws-20210330-0-RC1.de+FX+412"}

    result = requests.get(url, cookies=cookies)
    doc = BeautifulSoup(result.text, "html.parser")
    tag_list = doc.find_all(["span"], class_="oqSTJd")

    if tag_list == []:
        rating = 0
    else:
        b4s_tag = tag_list[0]
        string = str(b4s_tag)
        x = re.findall("(?<=\>)(.*?)(?=\<)", string)
        new_string = x[0]
        #if new_string.find("/") != -1:
        #    final_rating = 0
        #else:
        #    rating = new_string.replace(",", ".")
        #    final_rating = float(rating)
        rating = new_string.replace(",", ".")
        #final_rating = float(rating)
    destination = sheet[cell_write]
    destination.value=rating

wb.save(r'scrapping\airports1.xlsx')

#"https://tickets.pl/avia/rating?search_str=" + adria
