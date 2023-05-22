import requests
from bs4 import BeautifulSoup

def get_id(username):

        url = f'https://www.facebook.com/{username}'
        url = url

        payload = {}
        headers = {
        'authority': 'www.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'datr=dE1SZDlHC8pPBaEFsWq8AW1f; wd=839x952',
        'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        response = requests.request("GET", url, headers=headers, data=payload).text
        fid =''
        if '/profile/' in response:
            fid =  response.split("/profile/")[1].split('\"')[0]
        elif 'entity_id' in response:
            fid =  response.split("entity_id")[1].split('"')[2]
        else:
            print ("Not Found")
            fid = 'Not Found'


        return {'fid':fid, 'username':url}


def get_id_with_proxy(username):
  
        usernamee = 'sprf1lyzgh'
        password = 'Y0xnnKy6ete47AxmnG'

        proxy = f'http://{usernamee}:{password}@gate.smartproxy.com:7000'

        url = f'https://www.facebook.com/{username}'
        url = url


        payload = {}
        headers = {
        'authority': 'www.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'datr=dE1SZDlHC8pPBaEFsWq8AW1f; wd=839x952',
        'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }    

        print("Not Found Without Proxy")
        response = requests.request("GET", url, headers=headers, data=payload, proxies={'http': proxy, 'https': proxy}).text
        fid =''
        if '/profile/' in response:
            fid =  response.split("/profile/")[1].split('\"')[0]
        elif 'entity_id' in response:
            fid =  response.split("entity_id")[1].split('"')[2]
        else:
            print ("Not Found With Proxy")
            fid = 'Not Found'
      

        return {'fid':fid, 'username':url}
