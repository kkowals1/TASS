from bs4 import BeautifulSoup
import requests
import re
import openpyxl

wb = openpyxl.load_workbook(r'C:\Users\Karol\Desktop\airlines.xlsx')
sheet = wb.active

temp=1
for i in range (1, 236):
    temp += 1
    cell_read = "B"+str(temp)
    cell_write = "G" + str(temp)
    url_param = sheet[cell_read].value

    url = "https://www.airlinequality.com/airline-reviews/" + url_param
    #print(url)
    cookies = {"CONSENT":"YES+shp.gws-20210330-0-RC1.de+FX+412"}

    result = requests.get(url, cookies=cookies)
    doc = BeautifulSoup(result.text, "html.parser")
    tag_list = doc.find_all(["div"], class_="rating-10 rating-large")
    # REMARK - "span itemprop"ratingValue" wyrzuca również oceny z bieżących opinii

    if tag_list == []:
       rating = 0
    else:
       b4s_tag = tag_list[0]
       string = str(b4s_tag)
       pure_string = re.sub(r"[\n\t\s]*", "", string)
       a, b = pure_string.split('>', 1)
       x = re.findall("(?<=\>)(.*?)(?=\<)", b)
       rating = x[0]

    destination = sheet[cell_write]
    destination.value=rating

wb.save(r'C:\Users\Karol\Desktop\airlines1.xlsx')