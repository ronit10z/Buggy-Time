import csv
data = ["value %d" % i for i in range(1,4)]

out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow(data)