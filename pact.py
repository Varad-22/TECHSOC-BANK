import csv
# # with open("rand.txt","w")  as fin:
# #     fin.writelines(["Helllo\n","How are you\n","I am fine thank you\n"])

# with open ("rand.txt") as fin:
#     lst = fin.readlines()
#     # print(lst)
#     fin.seek(8)
#     s="I am fine thank you so much"
#     # l=fin.readline()
#     # l=s
# with open("rand.txt","r+",newline="") as fin:
#     # fin.seek(8)
#     # print(fin.tell())
#     fin.seek(len(fin.read()))
#     fin.write(s)
#     fin.seek(8)
#     fin.write("")


def acc_read(fin,anum):
    with open(fin) as file:
        cur=csv.DictReader(file)
        for row in cur:
            if (row["acc_number"] == str(anum)):
                return (row)  #row will be dictionary
            
def edit_data(fin,field,anum,replace):
    heading=["full_name","login","pswd","acc_number","balance"]
    lstr = []
    with open (fin) as file:
        data = file.readlines() #list of strings
        # print(data)
        if field in heading:
            for i in data:
                lst=i.split(",") #i is a list
                # print(lst)
                if (lst[3] == str(anum)):
                    lst[heading.index(field)] = str(replace) + "\n"
                    s=",".join(lst)
                    lstr.append(s)
                else:
                    lstr.append(",".join(lst))
            print(s)

        else:
            print("Error")
            return

        # print(lstr)

    with open (fin,"w",newline="") as file:
        file.writelines(lstr)

# edit_data("bank.txt","balance",1234567890,70000)

def withdraw(fin,anum,amt):  #can be used for deposit as well
    data_dict = acc_read(fin,anum)
    n_amt=int(data_dict["balance"]) - amt
    edit_data(fin,"balance",anum,n_amt)
a=1000
withdraw("bank.txt",1234567890,0-a)