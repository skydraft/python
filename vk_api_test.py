import vk_api
from  vk_api.audio import VkAudio
import collections
import requests
import os,shutil

def auth_handler():
    """ При двухфакторной аутентификации вызывается этот метод.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device
def main():

 vk_session=vk_api.VkApi("login","pass",auth_handler=auth_handler)
 print(vk_session)
 try:
    vk_session.auth()
 except vk_api.AuthError as err:
    print(err)
    return


 vkaudio=VkAudio(vk_session)
 a=vkaudio.get()
 output_file = open('D:\\vk.txt', 'w')

 #st=""
 #des=""
 #n=""


 dirname='D:\\vk_music\\'
 filename=n
 for i in a:


     des=""
     n=""
     st=""

     for k,v in i.items():

         if k=='url':
             for j in v:

                 if j=="?":
                     break
                 st+=j
             des=k
             #output_file.write(str(v)+' ')
         if k=='title':

             v=v.replace("\"","'")
             v+=".mp3"

             r = requests.get(st, stream=True)
             if r.status_code == 200:

                 with open(dirname+v, 'wb') as f:
                     r.raw.decode_content = True
                     shutil.copyfileobj(r.raw, f)
                 print(v)

             n=k
             output_file.write(str(v) + '\n')


     filename = n





if __name__ == '__main__':
    main()