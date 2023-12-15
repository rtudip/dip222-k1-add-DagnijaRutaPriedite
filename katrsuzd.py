#1.uzd
fails='data.txt'
Country=input()
latvija=[]
with open(fails) as f:
    regi=[]
    next(f)
    for line in f:
            row=line.rstrip().split(",")
            if(row[4]==Country):
                regi.append(int(row[6]))
print(regi)

#2.uzd
fails='data.txt'
Country=input()
job=input()
with open(fails) as f:
    darbinieki=[]
    next(f)
    for line in f:
            row=line.rstrip().split(",")
            if(row[4]==Country and row[7]==job):
                  darbinieki.append(int(row[8]))
print(sum(darbinieki))

#3.uzd
fails='data.txt'
Industry=input()
country=[]
with open(fails) as f:
    darbinieki=[]
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        if(row[7]== Industry and row[4]=="Latvia"):
            country.append(int(row[8]))
print(sum(country))
         

#4.uzdevums
fails='data.txt'
Country=input()
with open(fails) as f:
    next(f)
    count=0
    for line in f:
            row=line.rstrip().split(",")
            if row[4]==Country:
                if "https://" in line:
                    count+=1
print(sum)

#5.uzdevums
fails='data.txt'
Country=input()
with open(fails) as f:
    next(f)
    count=0
    for line in f:
            row=line.rstrip().split(",")
            if row[4]==Country:
                if ".org" in line:
                    count+=1
print(sum)