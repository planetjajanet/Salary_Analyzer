# -*- coding: utf-8 -*-
import csv

class Employee:
    Gender = ""
    AnnualSalary = 0
    Position = ""

employees = []

file = open("/Users/Janet/Documents/Python/Employee_Salaries_-_2014.csv")
data = csv.reader(file)
next(data)

for row in data:
    e = Employee()
    e.Gender = row[1] #reads each row at index 1
    e.AnnualSalary = float(row[2].replace("$", ""))
    e.Position = row[9]
    employees.append(e)    

def OverallSalary(employees):
    
    salarylist = []
    
    for e in employees:
        salarylist.append(e.AnnualSalary)        

    MaxSalary = 0

    for i in salarylist:
        if i > MaxSalary:
            MaxSalary = i
            MinSalary = MaxSalary
        if i < MinSalary:
            MinSalary = i
        
    avg = sum(salarylist)/len(salarylist)
    print "The maximum salary is: $" + str(MaxSalary)
    print "The minimum salary is: $" + str(MinSalary)   
    print "The average salary is: $" + str(avg)    
    
def SalaryByGender(employees):
    FemaleSalary = []
    MaleSalary = []
    for e in employees:    
        if e.Gender == "F":
            FemaleSalary.append(e.AnnualSalary)
        if e.Gender == "M":
            MaleSalary.append(e.AnnualSalary)

    FemaleAvg = sum(FemaleSalary)/len(FemaleSalary)
    MaleAvg = sum(MaleSalary)/len(MaleSalary)

    print "The average salary for females is: $" + str(FemaleAvg)
    print "The average salary for males is: $" + str(MaleAvg)
    
    

#========Appearance==========
while (True): 
    print "Salary Analyzer"
    print "==============="
    print "1- Overall Max/Min/Average Salary"
    print "2- Average Salary by Gender"
    print "3- Highest Paid Position"
    print "0- Exit"
       
    choice = input("What do you want to do? ")
    if choice == 1:
        OverallSalary(employees)
        print "\n"
    elif choice == 2:
        SalaryByGender(employees)
        print "\n"
    elif choice == 0:
        print "Thank you for using Salary Analyzer (: "        
        break;    

file.close()    