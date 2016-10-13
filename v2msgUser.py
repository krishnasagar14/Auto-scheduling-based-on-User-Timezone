import datetime, pytz
import csv
import thread

msg = " : Message sent : "

# updated program : dict of country codes from CSV to actual time zones. Also, after message sent user item is removed.

tz_dict = {'IND':'Asia/Kolkata', 'WIN' : 'Jamaica', 'USA' : 'US/Pacific', 'ENG' : 'Europe/London', 'JAP' : 'Japan'}
with open('in.csv') as inObj:
    inCSV = csv.reader(inObj)
    inCSV = list(inCSV) # user items list.
    open('out.txt', 'w')
    tz1 = {}
    while(len(inCSV)>0):
        for i in inCSV:
            date_time = datetime.datetime.now(pytz.timezone(tz_dict[i[1]]))
            d = date_time.date().strftime('%m/%d/%Y')
            t = date_time.time().strftime('%H:%M:%S')
            if t in i and d in i:
                with open('out.txt', 'a') as outObj:
                    outObj.write(i[0] + msg + i[1] + " messaged at:" + t + " " + d +  "\n")
                    print "done"
                inCSV.remove(i)