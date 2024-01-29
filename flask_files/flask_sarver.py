from flask import Flask, render_template, request, Markup
from class_files.User import User

#435764926087299073
app = Flask(__name__, static_folder="./static")

@app.route("/<userid>", methods=["GET", "POST"])
def index(userid):
    print(userid)
    notify_anime_dict_list = User.make_notify_anime_dict_list(userid)
    print(notify_anime_dict_list)
    return render_template('index.html', notify_anime_dict_list=notify_anime_dict_list)

@app.route("/kspNotify", methods=["GET"])
def home():
    try:
        req = request.args
        userid = req.get("userid")
    except:
        print("ユーザーidがget出来ませんでした。")
    print(userid)
    notify_anime_dict_list = User.make_notify_anime_dict_list(userid)
    print(notify_anime_dict_list)
    return render_template('index.html', notify_anime_dict_list=notify_anime_dict_list)

@app.route("/animeInfo", methods=["GET","POST"])
def animeInfo():
    id = request.form.get("id")
    anime_info_dict = User.make_anime_info_dict(id)
    anime_info_dict["mainImg_div"] = Markup(anime_info_dict["mainImg_div"])
    return render_template('animeInfo.html', anime_info_dict=anime_info_dict)



if __name__=="__main__":
    app.run(port=8000, debug=True)

