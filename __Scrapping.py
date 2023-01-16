# pip install requests/beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
import time

class Scrapper():

    def __init__(self,url):
        #GET Request
       self.r = url 
       self.r2 = requests.get(self.r)
       print()
        #parsing HTML
       self.parsing = BeautifulSoup(self.r2.content, 'html.parser')


    def html_text(self):

        self.html = self.parsing.prettify() #print the html in more readable view

        return self.html


    def paragraph_find(self):#Extracting text from the tags

        self.lines = self.parsing.find_all('p')
        self.par = [ line.text for line in self.lines ]
        self.par_fixed = [ i for i in self.par if i != '' ]
        self.par_find = [ [item] for item in self.par_fixed ]

        return self.par_find


    def links_find(self): #Extracting links

        self.links = [ link.get('href') for link in self.parsing.find_all('a') ]
        self.links_fixed_1 = [ i for i in self.links if i != None]
        self.links_fixed_2 = filter(lambda x: not x.startswith('#'), self.links_fixed_1)
        self.links_fixed_3 = filter(lambda x: not x.startswith('/'), self.links_fixed_2)
        self.lnk = [ [item] for item in self.links_fixed_3 ]

        return self.lnk


    def images_find(self): #Extracting the images' link

        self.images = [ image.get('src') for image in self.parsing.find_all('img') ]
        self.img_fixed = [ i for i in self.images if i != '' ]
        self.img_lnk = [ [item] for item in self.img_fixed ]

        return self.img_lnk


    def Save_2_CSV(self, data): #Saving data to CSV format
        self.data = data
        self.file_name = input("Your CSV file's name \n>>> ") + '.csv'
        with open (f'{self.file_name}', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(self.data)):
                writer.writerow(self.data[i])
        time.sleep(2)
        print(f'Your data is saved in ', self.file_name)

print("Welcome to Web Scrapper!\nYou can scrap text, link, or image's link here.\nONLY FOR NEWS SITE.\n")

while True:
    
    link_site = input('Input your URL : ')
    scrapper = Scrapper(link_site)

    to_do = int(input("\nWhat would you like to do?\n[1] Scrap Text\n[2] Scrap Link\n[3] Scrap Image Link\n[4] Exit\n>>> "))

    if to_do == 1:
        paragrapgh = scrapper.paragraph_find()
        scrapper.Save_2_CSV(paragrapgh)
    elif to_do == 2:
        paragrapgh = scrapper.links_find()
        scrapper.Save_2_CSV(paragrapgh)
    elif to_do == 3:
        paragrapgh = scrapper.images_find()
        scrapper.Save_2_CSV(paragrapgh)
    elif to_do == 4:
        break
    else:
        print("Invalid input")

    to_do_2 = input("Would you like to continue? [Y/N]")

    if to_do_2 == 'N' or to_do_2 == 'n':
        break
    else:
        pass