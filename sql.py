import pymysql

def insert_to_sql(rssi, sensor, beamer, time,uuid,major,minor):
    try:
        db = pymysql.connect(host="localhost", port=3306,
                             user="psigel", passwd="beaconsbeacons", db="beacons")
    except Exception as e:
        print("error tratando de conectar a DB")
        print(e)
    curs = db.cursor()
    query = "INSERT INTO fast_data_pulpa (sensor,beamer,rssi,time,ibeaconUuid,ibeaconMajor,ibeaconMinor) VALUES('" + sensor + "','" + beamer + "'," + str(rssi) + ",'" + str(time) + "','" + uuid + "'," + str(major) + "," + str(minor) + ")"
    try:
        curs.execute(query)
    except Exception as e:
        print("exception:", e)

    db.commit()
    db.close()

def get_data(limit):
    try:
        db = pymysql.connect(host="localhost", port=3306,
                             user="psigel", passwd="beaconsbeacons", db="beacons")
    except Exception as e:
        print("error tratando de conectar a DB")
        print(e)
    curs = db.cursor()
    query = "SELECT * FROM fast_data_pulpa where time > date_sub(now(), interval 3 second) ORDER BY ID DESC LIMIT " + str(limit)
    try:
        curs.execute(query)
        data = curs.fetchall()
        db.close()
        return data
    except Exception as e:
        print("exception:", e)
        db.close()

