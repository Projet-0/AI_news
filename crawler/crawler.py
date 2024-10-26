import json
import requests
from bs4 import BeautifulSoup


class Crawler():
    """ Function that analyse the content of a website using its url
    
    """
    def __init__(self):
        self.url = 'https://www.artificialintelligence-news.com/'
        self.content = []
        self.links = []
        self.request_content = ''
        self.headers = {'Server': 'nginx', 'Date': 'Sat, 26 Oct 2024 23:16:59 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Access-Control-Allow-Origin': '*', 'X-Cache-Enabled': 'True', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Link': '<https://www.artificialintelligence-news.com/wp-json/>; rel="https://api.w.org/", <https://www.artificialintelligence-news.com/wp-json/wp/v2/pages/1835>; rel="alternate"; title="JSON"; type="application/json", <https://www.artificialintelligence-news.com/>; rel=shortlink', 'X-Httpd-Modphp': '1', 'Host-Header': '8441280b0c35cbc1147f8ba998a563a7', 'X-Proxy-Cache': 'HIT', 'Content-Encoding': 'gzip'}
        self.request_header = ""
        pass
    
    def request(self):
        if not self.url:
            raise ValueError
        else:
            print("URL valid. Attempting to request...")
            self.request_content = requests.get(f'{self.url}')
            self.request_header = requests.get(f'{self.url}',headers=self.headers)
            
                
        if self.request_content.status_code != 200:
            raise ConnectionError
        else:
            print("Succeed to request the website")
            # for element in self.request_content:
            #     print(element,"\n")
    
    def get_url(self):
        return self.url

    def get_request_content(self):
        return self.request_content
    
    def parse(self):
        soup = BeautifulSoup(f"{self.request_content.text}","lxml")
        return soup

if __name__ == "__main__":
    cr = Crawler()
    cr.request()
    resultat = cr.get_request_content()
    # soup = cr.parse()
    # print(soup)
    
    
    # for element in resultat:
    #     print(element,'\n')
    
    
    
    