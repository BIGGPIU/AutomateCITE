from datetime import datetime,timedelta



if __name__ == "__main__":
    print (timedelta(hours=13,minutes=45))
    x = datetime.now()
    hours = x.hour
    minutes = x.minute
    print(timedelta(hours=9,minutes=45) - timedelta(hours=hours,minutes=minutes))