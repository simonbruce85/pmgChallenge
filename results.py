import csv
import os.path as path
import os
import sys

DIR = path.abspath(path.dirname(__file__))

def write_file(writer, csv_reader,filename):
    #ignoring the first row of the document, which is the header
    next(csv_reader)
    #now iterates trough the document, line by line, printing the line in the destination document
    for line in csv_reader:
            writer.writerow([
                line[0],
                line[1],
                filename
            ])

def main():
    if path.exists(path.join(DIR, 'fixtures', sys.argv[len(sys.argv)-1])):
    # delete the file
        os.remove(path.join(DIR, 'fixtures', sys.argv[len(sys.argv)-1]))

    #opening the destination document, letting the script know that the name of the document will be the last argument
    #newline='' argument is used in windows to avoid the writer printing a new line
    with open(path.join(DIR, 'fixtures', sys.argv[len(sys.argv)-1]), 'a',newline='') as fh:
        #declaring the writer
        writer = csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
        #writing the first row, the header of the document with the new category
        writer.writerow(['email_hash', 'category','filename'])
        #go over all the documents provided by input, from arg 1 to n-1
        for i in range(1,len(sys.argv)-1,1):
            #open the document one by one
            with open(path.join(DIR, 'fixtures', sys.argv[i]), 'r',) as csv_file:
                #declare the reader
                csv_reader = csv.reader(csv_file)
                #call the function to write in the the new document the document just read, providing the writer, the content, and the name of the current document where it is located
                write_file(
                    writer,
                    csv_reader,
                    sys.argv[i]
            )

if __name__ == '__main__':
    main()
