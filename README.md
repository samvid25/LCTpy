# LCTpy

## Description
LCTpy is a web crawler written in python 2 to fetch and parse players' standings and scores in top tournaments from https://chess24.com/en/watch/live-tournaments and display it in the terminal without having to open the page in a browser.

## Dependencies
This script uses:
* Selenium: To fetch the dynamic webpage (install using `pip install selenium`)
* BeautifulSoup: To parse the HTML (install using `sudo apt-get install python-bs4`)
* Tabulate: To display a formatted standings table (install using `pip install tabulate`)
* Pyvirtualdisplay: To hide the browser window while the script is running (install using `pip install pyvirtualdisplay`)

The script requires Firefox and geckodriver for Firefox added to PATH ([Download link](https://github.com/mozilla/geckodriver/releases))

## Usage
```
$ python crawler.py
```

## Disclaimer
The script does not display all the tournaments listed in the webpage. Only a few from the top are shown.  
The code does not follow the best coding practices. It is just a simple script to extract required data.  
Contact me if there are any bugs or compatibility issues.

## To Do
Test the infinite scroll load on a slow internet connection

