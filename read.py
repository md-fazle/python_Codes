import csv
 
with open('Book1.csv','r') as csvfile:
     csv_reader=csv.reader(csvfile)
 
with open('N_Book1.csv','w') as new_file:
     csv_writer=csv.writer(new_file, delimiter='\t')
    
     for line in csv_reader:
      csv_writer.writerow(line)