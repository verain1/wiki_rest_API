import json
from django.shortcuts import render

from django.http import HttpResponse
import json
import requests
from bs4 import BeautifulSoup
# Create your views here.




def ansPageView(request, id):
    url = "https://en.wikipedia.org/wiki/" + id

    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")

    ans = soup.find('table', attrs={'class': 'infobox ib-country vcard'})

    trs = ans.find_all('tr')
    resp_dict = dict()

    flag = soup.find_all('img', attrs={'class': 'thumbborder'})[0]
    resp_dict['flag_link'] = flag['src']

    for tr in trs:
        key = tr.find('th',attrs={'class':'infobox-label'})
        val = tr.find(attrs={'class':'infobox-data'})
        if key != None and val != None:
            if 'Capital' in key.text:
                if val.find('ul') != None:
                    resp_dict['capital'] = [i.find('a')['title'] for i in val.find_all('li')]
                else:
                    resp_dict['capital'] = val.find('a')['title'] 

            if 'languages' and 'Official' in key.text:
                if val.find('ul') != None:
                    resp_dict['official_languages'] = [i.find('a')['title'] for i in val.find_all('li')]
                else:
                    resp_dict['official_languages'] = val.text
            if 'Largest city' in key.text:
                if val.find('ul') != None:
                    resp_dict['largest_city'] = [i.find('a')['title'] for i in val.find_all('li')]
                else:
                    resp_dict['largest_city'] = val.find('a')['title']

            if 'Total' in key.text and 'km' in val.text:
                string = val.text
                string = string.replace(u'\xa0', u' ')
                sp = string.split('(')
                resp_dict['area'] = sp[0]
            
            if 'Total' in key.text and '$' in val.text:
                string = val.text
                sp = string.split('[')
                resp_dict['GDP_nominal'] = sp[0]
            
            
            if 'estimate' in key.text or 'census' in key.text:
                string = val.text
                sp = string.split('[')
                resp_dict['population'] = sp[0]
    return HttpResponse(json.dumps(resp_dict))