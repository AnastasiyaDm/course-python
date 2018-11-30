from django.core.management.base import BaseCommand, CommandError
from main.models import Art
import requests
from bs4 import BeautifulSoup
url='http://art-news.com.ua/'
r=requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
class Command(BaseCommand):


    def handle(self,*arguments,**options):
        print 'START'
        i=1
        Art.objects.all().delete()
        block=soup.find_all('div',{'column half'})
        
        for l in block:
            item=Art()
            head=l.find('h2').find('a')
            item.title=head.text
            item.link=head.get('http')
            item.content=l.find('div',{'excerpt text-font'}).get('p')
            item.save()
            print 'Saving %s' % i
            i+=1
        
