#Python Automation Demo Example
from Header import *

i = 0

def DisplayProcess(FolderName="MarvellousLog"):
    global i
    today = date.today()
    Data = []

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    File_Path = os.path.join(FolderName,"Marvellous%s_%d.log"%(today,i))
    i = i + 1
    fd = open(File_Path,"w")

    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)

    for element in Data:
        fd.write("%s\n"%element)

    mail(File_Path)

def main():
    print("-----------------Marvellous Infosystems------------------")
    print("Script Title : "+argv[0])

    if(argv[1] == "-u" or argv[1]=="-U"):#custom flags
        print("Usage : Use the script as Name.py Schedule_Time Folder_name")
        exit()

    if(argv[1] == "-h" or argv[1]=="-H"):
        print("Help : It is udsed to create log file")
        exit()

    schedule.every(int(argv[1])).minutes.do(DisplayProcess)
    while  True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
