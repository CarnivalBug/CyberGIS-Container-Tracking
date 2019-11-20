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

curr_time = ""

while (i<len(ay)):
    if ('CST 20' in ay[i]):
        curr_time=ay[i]
        i=i+1
    if (ay[i][0]>='0' and ay[i][0]<='9'):
        if ('c' in ay[i] and ay[i].split("c")[0]==ay[i].split("c")[1]):
            i = i+1
        elif ('c' in ay[i]):
            temp = []
            while(ay[i]!='Finish One'):
                #print(ay[i])
                temp.append(ay[i])
                i=i+1
            for j in range(0,len(temp)):
                if (temp[j][0]=='>'):
                    data = curr_time+". Add Container id: " + temp[j].split()[1]+" by user: "+temp[j].split()[2]
                    rt.append(data)
        elif ('a' in ay[i]):
            temp = []
            while(ay[i]!='Finish One'):
                #print(ay[i])
                temp.append(ay[i])
                i=i+1
            for j in range(0,len(temp)):
                if (temp[j][0]=='>'):
                    data = curr_time+". Add Container id: " + temp[j].split()[1]+" by user: "+temp[j].split()[2]
                    rt.append(data)
        elif ('d' in ay[i]):
            while(ay[i]!='Finish One'):
                #print(ay[i])
                temp.append(ay[i])
                i=i+1
            for j in range(0,len(temp)):
                if (temp[j][0]=='<'):
                    data = curr_time+". Remove Container id: " + temp[j].split()[1]+" by user: "+temp[j].split()[2]
                    rt.append(data)        
    
        else:
            i=i+1
    else:
        i=i+1
with open("log", "w") as file:
    for i in range(0, len(rt)):
        if (rt[i]!=''):
            file.write(rt[i])
            file.write("\n")
print("Done")  
