# import 'beautifulsoup4' and 'requests' for web scraping

import bs4
import requests



basic_url = 'https://en.wikipedia.org/wiki/Temperature_in_Canada'



result = requests.get(basic_url.format())

#print(result)

soup = bs4.BeautifulSoup(result.text, 'html.parser')

#print(soup)


#Save the first two introductory paragraphs of this article

first_paragraph = soup.select('p')[0].text
second_paragraph = soup.select('p')[1].text





#save the Average temperatures table (table 1), and the high temperatures table (table 3)

table_details = soup.select('table') #save the source code for all tables on this page

highs_table = table_details[2].select('tr') #save the row entries in the third table in a list

averages_table = table_details[0].select('tr') #saves each row of the first table in a list



# some row entries in table 1

print(averages_table[7].text) #seventh row of table 1
print(averages_table[14].text) #fourteenth row of table 1
print(averages_table[22].text) #twent-second row of table 1




# some entries in table 3

print(highs_table[2].text) #second row of table 3
print(highs_table[9].text) #ninth row of table 3
print(highs_table[16].text) #sixteenth row of table 3




#get images in wikipedia article

result_2 = requests.get('https://en.wikipedia.org/wiki/Temperature_in_Canada')

image_soup = bs4.BeautifulSoup(result_2.text, 'html.parser')

image_1 = image_soup.select('img')[0]['src']

image_2 = image_soup.select('img')[1]['src']


pic_1 = requests.get(image_1)
pic_2 = requests.get(image_2)




# save first image
f =open('abdul_temperature.png', 'wb')
f.write(pic_1.content)
f.close()


# save second image
f = open('abdul_temperature_2.png', 'wb')
f.write(pic_2.content)
f.close()