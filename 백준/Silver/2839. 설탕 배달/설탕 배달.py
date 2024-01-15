DPlist = []
DPlist.append(-1) #0
DPlist.append(-1) #1
DPlist.append(-1) #2
DPlist.append(1) #3
DPlist.append(-1) #4
DPlist.append(1) #5
DPlist.append(2) #6
DPlist.append(-1) #7
DPlist.append(2) #8
DPlist.append(3) #9
DPlist.append(2) #10
DPlist.append(3) #11
DPlist.append(4) #12
DPlist.append(3) #13
DPlist.append(4) #14
DPlist.append(3) #15
DPlist.append(4) #16
DPlist.append(5) #17
DPlist.append(4) #18
DPlist.append(5) #19

for i in range(20, 5001):
    new_data = DPlist[i-10] + 2
    DPlist.append(new_data)

#for i in range(1,100) :
    #print(i, ':', DPlist[i])

a = int(input())
print(DPlist[a])