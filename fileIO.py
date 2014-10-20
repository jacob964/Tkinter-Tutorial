
import os

# def retrieveFile():
#     try:
#         bestStudent = {}
#         bestStudentStr = "The Best Students Ranked\n\n"
#         
#         f = open('studentgrades.txt') #default to 'r' or read-only; also 'w' for write or 'a' for append
#     
#     except(IOError), e:
#         print "File not found", e
#     
#     else:
#         for line in f:
#             name, grade = line.split()
#             bestStudent[grade] = name
#         f.close()
#         
#         for i in sorted(bestStudent.keys(), reverse=True):
#             print (bestStudent[i] + ' scored a ' + i)
#             bestStudentStr += bestStudent[i] + ' scored a ' + i + "\n"
#         print "\n"
#         
#         print bestStudentStr
#         
#         outToFile = open("studentrank.txt", "w")
#         outToFile.write(bestStudentStr)
#         outToFile.close()
#         
#         print "Finished Output"

def directoryPlay():
#     print os.listdir(".")
#     print os.path.isdir("C:/Python27")
#     print os.path.isfile("C:/Python27/python.exe")
    
    dirList = os.listdir("C:/Users/Jacob/Desktop")
    
    for file in dirList:
        if os.path.isdir("C:/Users/Jacob/Desktop/" + file):
            print os.listdir("C:/Users/Jacob/Desktop/" + file)
        else:
            continue
    
    # os.mkdir("./Testing")
    
    
def main():
    directoryPlay()
    
if __name__ == '__main__': main()