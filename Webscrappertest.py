from selenium import webdriver
from reportlab.pdfgen.canvas import Canvas
from fpdf import FPDF
from selenium.common.exceptions import NoSuchElementException
import time

# To change target or website to scrap
# change url to the website u wanna scrap
# get the header and text
# need to implement while loop

nextbut= True

file1 = open("LTBE.txt", "w", encoding='utf8')

#url = 'https://ranobes.net/up/dragon-chain-ori/899985-1.html'
url = 'https://hostednovel.com/11635/novel/little-tyrant-doesnt-want-to-meet-with-a-bad-end/ltbe-chapter-1'
browser = webdriver.Chrome()
#browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.get(url)
browser.delete_all_cookies()

#title = browser.find_element_by_class_name('h4').text
# title = browser.find_element_by_class_name('text-center').text
#content = browser.find_element_by_class_name('text').text
# content = browser.find_element_by_id('chapter').text

# file1.write(title)
# file1.write('\n')
# file1.write(content)

while(nextbut):
        time.sleep(1)
        #title = browser.find_element_by_class_name('h4').text
        title = browser.find_element_by_class_name('text-center').text
        
        #content = browser.find_element_by_class_name('text').text
        content = browser.find_element_by_id('chapter').text
        browser.delete_all_cookies()

        try:
                #browser.find_element_by_id('next').click()
                browser.find_element_by_xpath('//*[@id="app"]/main/div[3]/div/div/div/div/div/div[3]/a').click()
                
        except NoSuchElementException:
                nextbut = False
        
        time.sleep(2)
        #try:
        #        time.sleep(2)
        #        browser.find_element_by_xpath('//*[@id="dismiss-button"]').click()
        #except NoSuchElementException:
        #        pass
        file1.write(title)
        file1.write('\n')
        file1.write(content)
        file1.write('\n')
        file1.write('\n')
        file1.write('\n')

file1.close()

#need to ask for url and title/content class name. and the txt file name.
#we can possible make a list of urls to scrap everything.?
#we need to add the button that goes next chapter so we can automate the scrap.

#title = browser.find_element_by_class_name('post-title').text
#this finds the body paragraph of the light novel in this website.
#content = browser.find_element_by_class_name('post-body').text


#The utf8 encoding is all characters possible this lets us by pass the error earlier where uff0c is similar to a comma but is not.      
#obviously writes to a text file.


#list2 = list(content)
#list = list(content)
#print(list.index("\uff0c"))
#print(''.join(list))
#com = list[281]
#comma = ","
#print(com == comma)
#for i in range(len(list)):
#    if list[i] == "\uff0c":
        #print("testing")
#        list[i] = ","

#filtercontent = ''.join(list)

#pdf = FPDF()
#pdf.add_page()
#pdf.set_font("Arial", size = 15)
#f = open("MyFile.txt","r")

#for x in f:
#    pdf.cell(200,10,txt = x, ln = 1, align = 'C')

#pdf.output("txttopdf.pdf")

#job_list = []
#file1 = open("MyFile.txt","a")
#file1.write(title.text)
#file1.close()
#canvas = Canvas("test.pdf")
#canvas.drawString(0, 0, "Hello, World")
#canvas.save()