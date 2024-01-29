from bs4 import BeautifulSoup
import requests
import datetime
import re

class Danime():
    def URL_normalization(URL):
        
        pattern = r'https://[^&]+'
        
        match = re.search(pattern, URL)

        if match:
            result_url = match.group(0)
            return result_url
        else:
            print("マッチする部分が見つかりませんでした。")
        
    
    def scraping_title(URL):
        URL = Danime.URL_normalization(URL)
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        
        #divを取得
        element_div = soup.find_all(attrs={"class":"titleWrap"})[0]
        
        element_h1 = element_div.find_all("h1")[0]
        
        return element_h1.get_text()    
    
    
    def scraping_main_img(URL):
        URL = Danime.URL_normalization(URL)
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        
        #divタグを取得
        element_div = soup.find_all(attrs={"class":"isMultipleImg keyVisual"})[0]
        
        #divタグを取得
        element_div_2 = element_div.find_all(attrs={"class":"thumbnailLeft"})[0]
        
        #imgタグを取得
        element_img = element_div_2.find_all("img")[0]
        return element_img["data-src"]


if __name__ =="__main__":
    URL = "https://animestore.docomo.ne.jp/animestore/ci_pc?workId=26610"
    URL = Danime.scraping_main_img(URL)
    
    print(URL)