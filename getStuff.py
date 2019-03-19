import commands
import subprocess
import os

for number in range(100000):
	os.system("curl 'https://galacticpuzzlehunt.com/puzzle/ministry-of-wordsearches/grid' -H 'Cookie: _ga=GA1.2.1005368705.1551899596; __cfduid=d781c5be613ce49f984cad9ba85be0c231551901956; csrftoken=mbGHxmHWilz3q16g3Oo5LJzsxNfkGtKJPtp0gOxXr0auiPfdeygzqUfhXtLNhj9c; sessionid=db804lemp687dnk0gsocm35oog7xfy9e; _gid=GA1.2.1729482871.1552690580' -H 'Origin: https://galacticpuzzlehunt.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: https://galacticpuzzlehunt.com/puzzle/ministry-of-word-searches' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'X-CSRFToken: JAQOBDzLgdeXeoWv4XoufC3MkCVynEEZcSz7k5pMpSPo6c5sfHgYUNJBKir1Yu3s' --data 'id_num=" + str(number) + "&random=false' --compressed > puzzles/" + str(number) + ".txt")
