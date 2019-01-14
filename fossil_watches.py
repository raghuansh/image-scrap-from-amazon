##requirements##
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from resumable import urlretrieve
import csv



##selenium driver object##
driver = webdriver.Chrome('/home/bhavesh/Documents/Data_Science/watch_scrap/chromedriver')
driver.get('https://www.amazon.in/s/ref=sr_in_-2_p_89_14?fst=as%3Aoff&rh=k%3Awatches%2Cn%3A1350387031%2Cp_89%3AFossil&bbn=1350387031&keywords=watches&ie=UTF8&qid=1517909003&rnid=3837712031')


html = driver.page_source #html page source

##beautiful soup##
soup = BeautifulSoup(html)

avon_list = []
tag_list = []

for tag in soup.find_all("a", {"class":"a-link-normal a-text-normal"}):
    img = tag.find_all('img')
    for i in img:
        link = i['src']
        avon_list.append(link)


for lo in soup.find_all("h2", {"class":"a-size-base s-inline s-access-title a-text-normal"}):
    tag_list.append(lo.text)

driver.close()



###################################
avon_id = list(range(1969, 2017))  ## generating random ids
brand = ['fossil']
avon_brand = brand * 48

final_df = pd.DataFrame()
final_df['Image_Id'] = avon_id
final_df['Image_URL'] = avon_list
final_df['Brand'] = avon_brand
final_df['Model_Tag'] = tag_list

final_df.to_csv("fossil_with_tags.csv", sep=',', encoding='utf-8', index=False) ##writing a csv of image links & its tags




##downloading images from links stored in csv
with open('fossil_with_tags.csv') as images:
    images = csv.reader(images)
    img_count = 1  # start at 1
    for i in images:
        urlretrieve(i[1], '/home/bhavesh/Documents/Data_Science/watch_scrap/data/fossil_watches/{0}.jpg'.format(img_count)) # string formatting inserting count
        img_count += 1 # increase count for each image.
print("All imgs downloaded !!!!")
