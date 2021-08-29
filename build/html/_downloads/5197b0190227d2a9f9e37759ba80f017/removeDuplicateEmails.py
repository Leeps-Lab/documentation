import csv
import os

# This script filters out emails who have previously been emailed or are already enrolled

# This file are the emails you just grabbed
newEmails = 'Emails.csv'

# This file contains emails that already have been contacted and emails that are already in the database
oldEmails = 'Spring.csv'

with open (newEmails) as csvfile:
    newEmailsCSV = csv.reader(csvfile)
    
    newEmailList = []
    for i in newEmailsCSV:
        newEmailList.append(i[0])

    with open (oldEmails) as csvfilez:
        oldEmailsCSV = csv.reader(csvfilez)

        oldEmailList = []
        for i in oldEmailsCSV:
            if len(i[0]) > 0:
                oldEmailList.append(i[0])
            if len(i[1]) > 0:
                oldEmailList.append(i[1])

        emailList = list(set(newEmailList) - set(oldEmailList))
        print(len(emailList))

        with open('PeopleToEmail.csv', 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(zip(emailList))