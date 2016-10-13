import datetime, pytz
import csv

def CSVupdates(inCSV): # function to check any new updated schedule from CSV file.
    with open('in.csv') as inObj:
        upCSV = csv.reader(inObj)
        upCSV = list(upCSV)
        for i in upCSV:
            if i not in inCSV:
                inCSV.append(i.append('0'))
    return inCSV

msg = " : Message sent : "
tz_dict = {'IND':'Asia/Kolkata', 'WIN' : 'Jamaica', 'USA' : 'US/Pacific', 'ENG' : 'Europe/London', 'JAP' : 'Japan'} # dict gluing CSV country codes with actual time zones.

#updated program : below logic works upto all CSV contents are updated with respective timezone. This is done with setting processed attribute.
with open('in.csv') as inObj:
    inCSV = csv.reader(inObj)
    inCSV = list(inCSV)
    # attribute proceessed :  0 stands : not sent message, 1 stands : message sent.
    incSV = [i.append('0') for i in inCSV]
    open('out.txt', 'w')
    tz1 = {}
    while(all(x[-1]=='1' for x in inCSV) == False):
        inCSV = CSVupdates(inCSV)
        for j,i in enumerate(inCSV):
            if i != None:
                date_time = datetime.datetime.now(pytz.timezone(tz_dict[i[1]])) # getting time respective to country.
                d = date_time.date().strftime('%m/%d/%Y')
                t = date_time.time().strftime('%H:%M:%S')
                if t in i and d in i and i[-1] == '0':
                    with open('out.txt', 'a') as outObj:
                        outObj.write(i[0] + msg + i[1] + " messaged at:" + t + " " + d +  "\n")
                        print "done"
                    inCSV[j][-1] = '1'