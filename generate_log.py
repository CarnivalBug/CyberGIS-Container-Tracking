f = open("tracking.log", "r")
x = f.read()
ay = x.split("\n")
rt = ""
i = 1
while(ay[len(ay)-1]!='Finish One'):
    ay.pop()
ay.pop(0)
rt = []
i = 0
while (i<len(ay)):
    curr_time = ay[i]
    i+=1
    while (i<len(ay) and ay[i]!='Finish One'):
        data = ""
        diff_str = ay[i]
        if (diff_str[0]=='<' and diff_str!='< '):
            ## Delete
            data = data+curr_time+". Remove Container id: " + diff_str.split()[1]+" by user: "+diff_str.split()[2]
        elif (diff_str[0]=='>'and diff_str!='> '):
            ## Add
            data = data+curr_time+". Add Container id: " + diff_str.split()[1]+" by user: "+diff_str.split()[2]
        rt.append(data)
        i+=1
with open("log", "w") as file:
    for i in range(0, len(rt)):
        if (rt[i]!=''):
            file.write(rt[i])
            file.write("\n")
print("Done")


