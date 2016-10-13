import datetime, pytz
import csv
import thread

# simple logic to update with a single timezone. Static to read CSV file, no update received to program if CSV file changed in running instance code.
msg = " : Hi you are at : "
tz = pytz.all_timezones
with open('in.csv') as inObj:
    inCSV = csv.reader(inObj)
    inCSV = list(inCSV)
    open('out.txt', 'w')
    while(len(inCSV)>0):
        for i in inCSV:
            date_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            d = date_time.date().strftime('%m/%d/%Y')
            t = date_time.time().strftime('%H:%M:%S')
            if t in i and d in i:
                with open('out.txt', 'a') as outObj:
                    outObj.write(i[0] + msg + i[1] + " messaged at:" + t + d +  "\n")
                    print "done"
                inCSV.remove(i)