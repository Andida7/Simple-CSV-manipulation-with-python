import csv

def main():
    """This function will read some csv file"""

    #open the file
    with open('csvfile1.csv', 'r') as csvfile1:
        #read the file
        csv_reader = csv.reader(csvfile1)
        #jummp the first line
        next(csv_reader)
        #loop through the file
        for line in csv_reader:
            print(line)
#call main function
#main()
def mani2():
    """This will write csv file to the original csv file with aother delimeter"""
    #open the original file
    with open('csvfile1.csv', 'r') as csvfile1:
        #read the csv file
        csv_reader = csv.reader(csvfile1)

        #open the new csv file 
        with open('csvfile2.csv', 'w') as csvfile2:
            #write to it with another delimeter
            csv_writer = csv.writer(csvfile2, delimiter='-')
            #loop through the line
            for line in csv_reader:
                csv_writer.writerow(line)        
#call main2
#mani2()
def main3():
    """This will use dictionary reader for the same csv file reading perpose"""
    #open the file
    with open('csvfile1.csv', 'r') as csvfile1:
        #use DictReader method from csv module
        csv_reader = csv.DictReader(csvfile1)
        #read the lines
        for line in csv_reader:
            print(line['email'])

#call main3
#main3()
def main4():
    """This will use DictWriter for writing purpose"""
    #open the file
    with open('csvfile1.csv', 'r') as csvfile1:
        #use DictReader method from csv module
        csv_reader = csv.DictReader(csvfile1)
        #open the new csv file
        #newline='' will remove the new line that will be printed to the new file
        with open('csvfile4.csv', 'w', newline='') as csvfile4:
            #create a list of fieldnames
            field_names = ['first_name', 'last_name', 'email']
            #write to it with another delimeter
            csv_writer = csv.DictWriter(csvfile4, fieldnames = field_names, delimiter='\t')
            #write the field names as a header
            csv_writer.writeheader()
            #loop through the line
            for line in csv_reader:
                #if we dont want some info to be shown we can delete it , 
                # first delet the 'email' from the field_names and
                # we can pass delete statment here
                # del line['email']

                #write the line to the new file 
                csv_writer.writerow(line)


#call main4
main4()

