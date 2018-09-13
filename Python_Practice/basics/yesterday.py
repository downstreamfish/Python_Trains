import datetime
def getyesterday():
    ttoday = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = ttoday - oneday
    return yesterday

print(getyesterday())
