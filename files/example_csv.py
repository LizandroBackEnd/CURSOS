#import csv  
#import os
 
""" Write 
with open("files/file.csv", "w") as file: 
    writer = csv.writer(file) 
    writer.writerow(["twit_id", "user_id", "text"]) 
    writer.writerow([41, 7, "User 7 twit 41"])
    writer.writerow([12, 15, "User 15 twit 12"]) """ 
 
""" Read 
with open("files/file.csv") as file: 
    reader = csv.reader(file) 
    for line in reader: 
        print(line)"""
     
""" Update CSV   
with open("files/file.csv") as r, open("files/files_temp.csv", "w") as w: 
    reader = csv.reader(r) 
    writer = csv.writer(w)  
    for line in reader:  
        if line[1] == "41":   
            writer.writerow([41, 7, "User 7 twit 41 updated"]) 
        else: 
            writer.writerow(line) 
    os.remove("files/file.csv") 
    os.rename("files/files_temp.csv", "files/file.csv")"""