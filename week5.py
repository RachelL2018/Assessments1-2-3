with open("data\iris.csv") as f: #open function to open a csv file by passing the path name to it
   for line in f:# loops through each line in file
    
    print(line.split(',')[0:4])# print each line in file as it loops through & uses split method to return an array of strings in the file and 
                               # returns the items in the array ranging from indexes specified.
