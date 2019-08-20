import os
## TODO: поиск по всем файлам и запись найденого в один файл
# TODO:
m=[]
#получить список 'элементов' в каталоге
#записываем в массив m полный путь до файла
try:
    filedir=os.listdir("C:\log_err")
    for i in filedir:
        myPatch="C:\log_err\\"+i
        m.append(myPatch)
    #################################################
    #записываем все найденное в "C:\log_err\FileErr.txt"
    fErr = open("C:\log_err\FileErr.txt", "a")
    for i in m:
        try:
            fileOpen=open(i,"r",errors='ignore')
            print("File: "+i+" is being analyzed" )
            fErr.write("######################"+i+"######################"+"\n")
            for f in fileOpen:
                #условие поиска значения в файле
                if  "5BA65C38D9B34DBDB" in f:
                    fErr.write(f)
            fileOpen.close()
        except:
            continue

    fErr.close()
except:
    print("Patch C:\log_err not foud")
