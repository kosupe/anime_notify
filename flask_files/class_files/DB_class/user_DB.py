import sqlite3

class User_DB():
    """
    -------+--------+---------+-----+------+---------+-------
    id(PK) | userid | service | url | date | mainimg | title
    -------+--------+---------+-----+------+---------+-------
    """
    _con = None
    _cur = None
    
    def _start_db():
        User_DB._con = sqlite3.connect("../flask_files/class_files/DB_class/user.db")
        User_DB._cur = User_DB._con.cursor()
    
    def _fin_db():
        User_DB._cur.close()
    

    def drop_tb():
        User_DB._start_db()
        User_DB._cur.execute("""
        DROP TABLE usertable;
        """)
        User_DB._con.commit()
        User_DB._fin_db()
    
    
    def create_tb():
        User_DB._start_db()
        User_DB._cur.execute("""
        CREATE TABLE usertable(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INT,
            service TEXT NOT NULL,
            url TEXT NOT NULL,
            date TEXT,
            mainimg TEXT,
            title TEXT
        );
        """)
        User_DB._con.commit()
        User_DB._fin_db()
        
    def insert_tb(userid, service, url, date, main_img, title):
        User_DB._start_db()
        User_DB._cur.execute(f"""
        INSERT INTO usertable (userid,service,url,date,mainimg,title) VALUES({userid},'{service}','{url}','{date}','{main_img}','{title}')
        """)
        User_DB._con.commit()
        User_DB._fin_db()
    
    def update_tb():
        User_DB._start_db()
        User_DB._cur.execute(f"""
        UPDATE  usertable set mainimg='https://image.p-c2-x.abema-tv.com/image/series/25-73/portrait.png' WHERE id = 3
        """)
        User_DB._con.commit()
        User_DB._fin_db()
        
    def select_tb_ALL():
        User_DB._start_db()
        res = User_DB._cur.execute(f"""
        SELECT * FROM usertable;
        """)
        result = res.fetchall()
        User_DB._con.commit()
        User_DB._fin_db()
        return result
    
    
    def select_tb_WHERE_userid(userid):
        User_DB._start_db()
        res = User_DB._cur.execute(f"""
        SELECT * FROM usertable WHERE userid={userid};
        """)
        result = res.fetchall()
        User_DB._con.commit()
        User_DB._fin_db()
        return result
    
    def select_tb_WHERE_id(id):
        User_DB._start_db()
        res = User_DB._cur.execute(f"""
        SELECT * FROM usertable WHERE id={id};
        """)
        result = res.fetchall()
        User_DB._con.commit()
        User_DB._fin_db()
        return result


if __name__ == "__main__":
    """
    User_DB.insert_tb(
        userid=435764926087299073,
        service="Danime",
        url="https://animestore.docomo.ne.jp/animestore/ci_pc?workId=26610",
        date="6 1 30",
        main_img="https://cs1.animestore.docomo.ne.jp/anime_kv/img/26/61/0/26610_1_1.png?1699498832881",
        title="薬屋のひとりごと"
    )
    """
    User_DB.update_tb()
    ans = User_DB.select_tb_WHERE_userid(435764926087299073)
    print(ans)