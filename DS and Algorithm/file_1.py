import csv
file = open('example.csv','a',newline='')
file_writer = csv.writer(file,delimiter = ',')
file_writer.writerow([1,2,3,4])
file_writer.writerow([15,26,36,46])
file.close()
