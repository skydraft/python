import vk_api
from  vk_api.audio import VkAudio
import collections
def main():

 vk_session=vk_api.VkApi("login","pass")
 try:
    vk_session.auth()
 except vk_api.AuthError as err:
    print(err)
    return

#vk=vk_session.get_api()
 vkaudio=VkAudio(vk_session)
 a={}
 a=vkaudio.get()
 output_file = open('D:\\vk.txt', 'w')
 s=0
 st=""
 for i in a:
     for k,v in i.items():
         #print(k)
         if k=='url':
             output_file.write(str(v)+' ')
         if k=='title':
             output_file.write(str(v) + '\n')


         #c=str(k)+str(v)

     print(i)




 print(a)
if __name__ == '__main__':
    main()