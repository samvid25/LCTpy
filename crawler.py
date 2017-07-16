################################# IMPORTS #################################
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from selenium import webdriver
import time
from tabulate import tabulate
import sys

############################## HIDE DISPLAY ################################

display = Display(visible=0, size=(800, 600))
display.start()

################################ SELENIUM ##################################
driver = webdriver.Firefox()

print 'Fetching webpage...'
driver.get('https://www.chess24.com/en/watch/live-tournaments')
print 'Loaded webpage.'
print

print 'Waiting for page elements to load...'
#wait till tournamentTitle element is loaded
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "tournamentTitle"))
)
#since the content loads on an infinte scroll, scroll the page down a couple of times; 7 here
for i in range(7):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
print 'Elements loaded.'


tournamentsList = []


#list of the names of the tournaments
tournament_names = []
#get raw html
soup = BeautifulSoup(driver.page_source, "html.parser")
#find all the names of the tournaments
titles = soup.find_all("h1", { "class" : "tournamentTitle" })
print "\nDisplaying " + str(len(titles)) + " tournaments..."
#populate the tournaments list with the names
for title in titles:
    tournament_names.append(title.text)


#create a list of dicts which contain the name and corresponding html div class name for the tournament
tournament_classes = []
i = 0
tournamentsDIV = driver.find_elements_by_class_name("tournament");
for div in tournamentsDIV:
    name = div.get_attribute("class").split()[1]
    tournament_classes.append(name)
    temp = { "name" : tournament_names[i], "className" : name }
    tournamentsList.append(temp)
    i = i+1


#display the list of tournaments
while True:
    print '\nCurrently Live Tournaments'
    print '--------------------------'                                          #Hey there, random-person-reading-the-code! :)
    for i in range(len(tournamentsList)):
        print '[' + str(i) + ']' + ' ' + tournamentsList[i]['name']
    #select tournament
    print
    o = input('Enter the index of the tournament (-1 to exit): ')
    if o >= len(tournamentsList):
        print '\nPlease enter a valid index'
        continue
    elif o == -1:
        sys.exit(0)

    #select the div corresponding to selected tournament
    selected_tournament = soup.find_all('div', attrs = {'class' : tournamentsList[o]['className']})
    #select the standings table from this div
    table = selected_tournament[0].find_all('table', attrs = {'class' : 'items'})[0]

    print
    print '----- ' + tournamentsList[o]['name'] + ' -----'

    #parsing and displaying the selected table
    final = [[]]
    flag = True
    for row in table.find_all('tr'):
        td = row.find_all('td')
        if td[1].find('h6') is None:
            print 'Team-type tournament. Cannot display players\' standings table.'
            flag = False
            break
        temp = []
        temp.append(td[0].text)
        temp.append(td[1].find('h6').find_all('span', attrs = {'class' : 'playerStatistics'})[0].text)
        temp.append(td[2].text)
        temp.append(td[3].text)
        final.append(temp)

    if flag == True:
        print tabulate(final, headers = ['Position', 'Name', 'Score', 'ELO'], tablefmt='grid')
    print


#close
driver.quit()

###############################################################################

display.stop()
#Bye! :)
