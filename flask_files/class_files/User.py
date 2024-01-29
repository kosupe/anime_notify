from class_files.DB_class.user_DB import User_DB
from class_files.scraping_class.Abema       import Abema
from class_files.scraping_class.AmazonPrime import AmazonPrime
from class_files.scraping_class.Danime      import Danime

class User:
    def make_notify_anime_dict_list(userid):
        notify_anime_dict_list = [[],[],[],[],[],[],[]]
        notify_anime_list:list = User_DB.select_tb_WHERE_userid(userid)
        
        for notify_anime in notify_anime_list:
            tmp_dict = {}
            tmp_dict["id"]      = notify_anime[0]
            tmp_dict["service"] = notify_anime[2]
            tmp_dict["url"]     = notify_anime[3]
            tmp_dict["title"]   = notify_anime[6]
            
            if len(notify_anime[4].split(" ")) > 1: 
                tmp_dict["time_hour"]    = notify_anime[4].split(" ")[1]
                tmp_dict["time_minutes"] = notify_anime[4].split(" ")[2]

            notify_anime_dict_list[int(notify_anime[4].split(" ")[0])].append(tmp_dict)

        
        return notify_anime_dict_list
    
    
    def make_anime_info_dict(id):
        anime_info_dict = {}
        anime_info:list = User_DB.select_tb_WHERE_id(id)[0]
        anime_info_dict["id"]      = anime_info[0]
        anime_info_dict["userid"]  = anime_info[1]
        anime_info_dict["service"] = anime_info[2]
        anime_info_dict["url"]     = anime_info[3]
        
        week_num = anime_info[4].split(" ")[0]
        if   week_num == "0":
            anime_info_dict["week"] = "月"
        elif week_num == "1":
            anime_info_dict["week"] = "火"
        elif week_num == "2":
            anime_info_dict["week"] = "水"
        elif week_num == "3":
            anime_info_dict["week"] = "木"
        elif week_num == "4":
            anime_info_dict["week"] = "金"
        elif week_num == "5":
            anime_info_dict["week"] = "土"
        else:
            anime_info_dict["week"] = "日"    
        
        if len(anime_info[4].split(" ")) > 1: 
            anime_info_dict["time_hour"]    = anime_info[4].split(" ")[1]
            if len(anime_info[4].split(" ")[2]) == 2:
                anime_info_dict["time_minutes"] = anime_info[4].split(" ")[2]
            else:
                anime_info_dict["time_minutes"] = "0" + anime_info[4].split(" ")[2]
        else:
            anime_info_dict["time_hour"]    = "--"
            anime_info_dict["time_minutes"] = "--"
        
        aspect_style = "aspect-ratio: %s;"
        if anime_info_dict["service"] == "Danime":
            aspect_style = aspect_style%"16/9"
        else:
            aspect_style = aspect_style%"1/1"
        
        
        anime_info_dict["mainImg_div"] = f"<div style='background-image: url({anime_info[5]}); {aspect_style}' class=mainImg></div>"
        anime_info_dict["title"]       = anime_info[6]
        
        return anime_info_dict
    
if __name__ == "__main__":
    
    print(User.make_notify_anime_dict_list(435764926087299073))