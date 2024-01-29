from bs4 import BeautifulSoup
import requests
import datetime
import re

class AmazonPrime():
    
    def scraping_title(URL):
        html_text = requests.get(URL)
        print(html_text)
        
        soup      = BeautifulSoup(html_text, 'html.parser')
        soup_jis = soup.prettify('Shift_JIS')
        soup      = BeautifulSoup(soup_jis, 'html.parser')
        
        #divを取得
        element_div = soup.find_all(attrs={"class":"p-jAFk", "class":"Qo+b2C"})[0]
        return element_div.get_text()
        
    
    def scraping_main_img(URL):
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        soup.prettify('Shift_JIS')
        
        #divを取得
        element_div = soup.find_all(attrs={"class":"DVWebNode-detail-atf-wrapper DVWebNode"})[0]
        
        #sourceタグを取得
        source_picture = element_div.find_all("source")[0]
        
        return source_picture["srcset"].split()[0]
    
    def scraping_main_img2(title):
        URL = f"https://www.amazon.co.jp/s?k={title}"
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        soup.prettify('Shift_JIS')
        
        #divを取得
        element_divs = soup.find_all(attrs={"class":"sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"})
        print(soup)
        for element_div in element_divs:
            title_div = element_div.find_all(attrs={"class":"a-size-base-plus a-color-base a-text-normal"})[0]
            print(title.get_text())
            if title.get_text() == title:
                element_img_div = element_div.find_all(attrs={"a-section aok-relative s-image-square-aspect"})[0]
                element_img = element_img_div.find_all("img")[0]
                return element_img["src"]
        
    
    
    #最新の話のサムネ
    def scraping_NewEpisode_img(URL):
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        soup.prettify('Shift_JIS')
        
        #divを取得
        element_div = soup.find_all(attrs={"class":"c5qQpO"})[-1]
        
        element_div_2 = element_div.find_all(attrs={"class":"om7nme"})[0]
        
        #sourceタグを取得
        element_source = element_div_2.find_all("source")[0]
        
        return element_source["srcset"].split()[0] 
    
    
if __name__ == "__main__":
    URL :str = "https://www.amazon.co.jp/gp/video/detail/B0CPPKSBYS/ref=atv_hm_hom_c_iWh0hk_brws_2_2?jic=8%7CEgRzdm9k"
    title = "僕の心のヤバイやつ"
    ans = AmazonPrime.scraping_title(URL)
    print(ans)
    