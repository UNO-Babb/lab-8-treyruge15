#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def makeID(first,last, idNum):
    idlen = len(idNum)

    while len(last) < 5:
      last = last + "X"

    id = first[0] + last +idNum[idlen -3: ]

    return id

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    
    year = {
      "Freshman": "FR",
      "Sophomore": "SO",
      "Junior": "JR",
      "Senior": "SR"
    }

    year1 = year[data[5]]
    major = " ".join(data[6:])
    major3 = major[:3]

    student_id = makeID(data[0], data[1], data[3])
    output = last + "," + first + "," + student_id + "," + major3 + "-" + year1 + "\n"
    outFile.write(output)

  #print(student_id)




  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
