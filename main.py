import requests
from bs4 import BeautifulSoup

URL = 'http://z2.fm/?sort=week'
URL_dload='http://z2.fm'
path = ''#  music/new/

page_num = 3
page_end = 20
j=page_num
while j!=page_end:
    URL = 'http://z2.fm/?sort=week&page='+str(j)

    song_list = BeautifulSoup(requests.get(URL).text, 'html.parser').find(class_='whb_box').find(
        class_='songs-list').findAll(class_='songs-list-item')[1:]
    for i in range(len(song_list)):
        name = song_list[i]('a')[-1]('span')[0].string + ' - ' + song_list[i]('a')[0]('span')[0].string
        url=URL_dload+song_list[i].find(class_='song-download btn4 download')['data-url']
        print(name)
        print(url)
        mp3 = requests.get(url)
        print(mp3.headers) #нет location, который имеет текущую ссылку

        with open(path+name+'.mp3', 'wb') as f:
            f.write(requests.get(url).content) #записывает не те данные
    j+=1
