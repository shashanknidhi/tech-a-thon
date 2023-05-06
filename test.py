# import datetime
# date = datetime.datetime.now()
# file = str(date.strftime("%B"))  + "/" + str(date.year) + "-" + str(date.month) + "-" + str(date.day) + ".pcapng"
# print(file)
# file = "captures/a1.pcapng"
# output = open(file,"x")
# print(output)
for i in range(1,5):
    file = "captures/"+str(i)+".pcapng"
    output = open(file, "x")
