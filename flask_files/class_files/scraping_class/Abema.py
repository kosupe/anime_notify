from bs4 import BeautifulSoup
import requests
import datetime
import re

class Abema():
    def URL_normalization(URL):
        #https://abema.tv/video/title/ の場合
        if URL[:29] == "https://abema.tv/video/title/":
            return URL
        
        #https://abema.tv/channels/abema-anime/slots/ の場合
        if URL[:44] == "https://abema.tv/channels/abema-anime/slots/":
            html_text = requests.get(URL).text
            soup      = BeautifulSoup(html_text, 'html.parser')
            
            #divを取得
            element_div = soup.find_all(attrs={"class":"com-m-BreadcrumbList"})[0]
            
            element_div_2 = element_div.find_all(attrs={"class":"com-m-BreadcrumbList__item"})[2]
            
            element_a = element_div_2.find_all("a")[0]
            
            href = element_a["href"]
            
            return "https://abema.tv" + href
        
        #https://abema.tv/video/episode/ の場合
        if URL[:31] == "https://abema.tv/video/episode/":
            html_text = requests.get(URL).text
            soup      = BeautifulSoup(html_text, 'html.parser')
            
            #divを取得
            element_div = soup.find_all(attrs={"class":"com-m-BreadcrumbList"})[0]
            
            element_div_2 = element_div.find_all(attrs={"class":"com-m-BreadcrumbList__item"})[2]
            
            element_a = element_div_2.find_all("a")[0]
            
            href = element_a["href"]
            
            return "https://abema.tv" + href
          
    
    def scraping_title(URL):
        URL = Abema.URL_normalization(URL)
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        
        #divを取得
        element_div = soup.find_all(attrs={"class":"com-video-TitleSection__title"})[0]
        
        return element_div.get_text()    
    
    
    def scraping_main_img(URL):
        URL = Abema.URL_normalization(URL)
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        
        #divを取得
        element_div = soup.find_all(attrs={"class":"com-m-PortraitThumbnail com-m-PortraitThumbnail--rounded"})
        
        #imgタグを取得
        element_img = element_div[0].find_all("img")[0]
        
        #srcset属性を取得
        img_url = element_img['srcset'].split()[0]

        # 正規表現パターンを定義 パラメータまだ正規表現
        pattern = r'https://[^?]+'

        # 正規表現でURLからパターンに一致する部分を抽出
        match = re.search(pattern, img_url)

        if match:
            result_url = match.group(0)
            return result_url
        else:
            print("マッチする部分が見つかりませんでした。")


    def scraping_NewEpisode_img(URL):
        URL = Abema.URL_normalization(URL)
        html_text = requests.get(URL).text
        soup      = BeautifulSoup(html_text, 'html.parser')
        
        #divを取得
        element_div = soup.find_all(attrs={"class": "com-m-Thumbnail", "class": "com-m-Thumbnail--loaded", "class": "com-m-Thumbnail--rounded"})
        
        #imgタグを取得
        element_img = element_div[-1].find_all("img")[0]
        
        #srcset属性を取得
        img_url = element_img['srcset'].split()[0]

        # 正規表現パターンを定義 パラメータまで正規表現
        pattern = r'https://[^?]+'

        # 正規表現でURLからパターンに一致する部分を抽出
        match = re.search(pattern, img_url)

        if match:
            result_url = match.group(0)
            return result_url
        else:
            print("マッチする部分が見つかりませんでした。")

    
        
        
    
if __name__ == "__main__":
    URL :str = "https://abema.tv/video/title/25-73"
    ans = Abema.scraping_main_img(URL)
    print(ans)