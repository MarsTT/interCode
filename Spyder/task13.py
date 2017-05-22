#coding=utf-8

import requests

params = {'firstname':'marxia','lastname':'tianci'}
r_1 = requests.post("http://pythonscraping.com/files/processing.php",data=params)
print r_1.text


files = {'uploadFile':open('../re.png','rb')}
r_2 = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)
print r_2.text