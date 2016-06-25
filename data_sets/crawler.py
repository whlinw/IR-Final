import httplib2
import datetime
from dateutil import relativedelta

h = httplib2.Http()

link_base = "https://english.wunderground.com/history/airport/RCSS/%Y/%m/1/MonthlyHistory.html?req_city=Taipei&req_statename=Taiwan&reqdb.zip=00000&reqdb.magic=1&reqdb.wmo=58968&format=1"

cur = datetime.datetime(year=2015,month=1,day=1)
while cur < datetime.datetime(year=2016, month=6, day=24):
    link = cur.strftime(link_base)
    resp, content = h.request(link)
    content = content.replace("<br />", "")
    f = open("./weather_data/"+cur.strftime("taipei_%Y_%m"), "w")
    f.write(content)
    cur += relativedelta.relativedelta(months=1)