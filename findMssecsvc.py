# -*- coding: utf-8 -*-
import os, sys
ipAdr=open("d:\unity1.txt") #путь до файла с ip адресами
fileRes=open("d:\unity2.txt",'w') # файл с результатами
s="//"
s1="/c$/Windows/"
for l in ipAdr: # построчно считываем файл
    ipAdrEdit = l.rstrip('\n')

    s4 = s + ipAdrEdit + s1
    pings = os.system("ping -n 1 "+ ipAdrEdit) #проверяем доступность узла
    if pings==1:
        fileRes.write("нет пинга к  " + ipAdrEdit + '\n')
    if pings==0:
     if (os.path.exists(s4) == True): #проверка существования пути
      #print("проверяем "+ipAdrEdit)
      files = os.listdir(s4) # получаем список файлов в директории
      for i in files:     # проверяем существование файла mssecsvc.exe
          if (i == 'mssecsvc.exe'):
              fileRes.write("mssecsvc найден " + ipAdrEdit + '\n')
              #print("mssecsvc yes " + ipAdrEdit)
fileRes.close()
ipAdr.close()