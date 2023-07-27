import os
import csv
import shutil
import math
import logging
import time

logging.basicConfig(level=logging.DEBUG,filename='File.log',filemode='a',format="%(asctime)s - %(levelname)s - %(message)s")


def move(source,destination):
    dest=shutil.move(source,destination)
    return dest                  # dest will give address of file

#for size of file
def getsize(file):
    size = os.path.getsize(file)
    size = size / 1024  # for kb
    size = math.ceil(size * 1000) / 1000  # for rounding of
    return size

def getformat(file):
    filename,fileextension=os.path.splitext(file)
    filename=os.path.basename(file)
    return filename,fileextension

while 1:
    print("Enter 1 for moving file \n"
          "Enter 2 to exit")
    x=input()
    if x==str(1):
        start_time = time.time()
        source=input("enter source Folder \n")

        k1=os.path.isdir(source)
        if k1==False:
            while k1!= True:
                print("Enter valid source folder")
                source = input()
                k1 = os.path.isdir(source)
        destination = input("enter destination Folder \n")
        k2=os.path.isdir(destination)
        if k2==False:
            while k2!=True:
                print("Enter valid Destination Folder")
                destination=input()
                k2=os.path.isdir(destination)
        folderlist = os.listdir(source)
        if len(folderlist) != 0:
            logging.debug("File Moving Started...")
            counter = 1
            # /home/diwakarkothari/
            for i in folderlist:
                destdirlist = os.listdir(destination)
                j=os.path.join(source,i)
                filelist=os.listdir(j)
                if len(filelist)!=0:
                    for k in filelist:
                        if k in destdirlist:

                            k1 = os.path.join(j, k)
                            name, ext = getformat(k1)

                            newname = ''
                            for z in name:
                                if z == '.':
                                    break
                                newname = newname + z
                            newname = newname + '(' + str(counter) + ')'
                            counter = counter + 1
                            newname = newname + ext

                            k2 = os.path.join(j, newname)
                            os.rename(k, k2)
                            size = getsize(k)
                            name, ext = getformat(k)
                            dest = move(k, destination)
                            data_to_append = [name, ext, size, dest]
                            file = open('mycsv.csv', 'a', newline='')
                            writer = csv.writer(file)
                            writer.writerow(data_to_append)
                            file.close()


                        else:
                            q = os.path.join(j, k)
                            size = getsize(q)
                            name, ext = getformat(q)
                            dest = move(q, destination)
                            data_to_append = [name, ext, size, dest]
                            file = open('mycsv.csv', 'a', newline='')
                            writer = csv.writer(file)
                            writer.writerow(data_to_append)
                            file.close()
            end_time = time.time()
            TotalTime = end_time - start_time
            TotalTime = math.ceil(TotalTime * 10000) / 10000
            Time_to_Append = [TotalTime]
            ff = open('time.csv', 'a', newline='')
            wr = csv.writer(ff)
            wr.writerow(Time_to_Append)
            ff.close()
            print("All Files Moved Successfully")
            logging.debug("File Moving Completed")

        else:
            print("No Folder Exists to Move")
    elif x==str(2):
        print("Exiting...")
        exit(1)
    else:
        print("Invalid Choice")

