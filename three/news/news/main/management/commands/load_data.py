from django.core.management.base import BaseCommand, CommandError
from main.models import News
import requests
from bs4 import BeautifulSoup
url='https://pythondigest.ru/'
r=requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
class Command(BaseCommand):
    

    def handle(self,*arguments,**options):
        print 'START'
        i=1
        News.objects.all().delete()
        block=soup.find_all('div',{'class':'item-container'})
        for l in block:
            record=News()
            findText=l.findNext('div',{'class':'issue-item'}).find_all('p')
            a=''
            for m in findText:
                a=a+m.text
            record.content=a    
            record.title=l.find('a',{'class':'issue-item-title'}).text
            record.urls=l.find('a',{'class':'issue-item-title'}).get('href','http')
            record.save()
            print 'Saving %s' % i
            i+=1
        

