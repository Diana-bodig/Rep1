# xnj 
import BeautifulSoup
import requests as req

resp = req.get('http://www.columbia.edu/~fdc/sample.html')

soup = BeautifulSoup(resp.text, 'lxml')
print(soup.h3)
