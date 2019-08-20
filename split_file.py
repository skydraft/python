#открываем файл для записи
#output_file = open('C:\\Users\\zankovich\\Documents\\8152\\p16in\\p16in1','w')
output_file = open('C:\\jira_logs\\1\\log\\authmgr1','w')

#a="C:\\Users\\zankovich\\Documents\\8152\\p16in\\p16in"
a="C:\\jira_logs\\1\\log\\authmgr"
s=1 # счетчик колличества файлов
p=0 # счетчик строк
#запускаем цикл и записываем в новый файл 1000000 строк
with open("C:\\jira_logs\\1\\log\\authmgr","r",errors='ignore') as r:

    for line in r:
        if p==500000:
            p=0
            s=s+1
            fil=a+str(s) #формируем новои имя файла

            output_file = open(fil,'w')

        p=p+1
        output_file.write(line)
#
