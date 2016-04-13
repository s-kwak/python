import requests
import bs4
import os

url = 'http://danbooru.donmai.us/explore/posts/popular?date=2016-04-12+03%3A32%3A26+-0400&scale=month'
os.makedirs('danb', exist_ok=True)

# find url of comic
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

# download image
pageCode = soup.select('.post-preview')

for i in range(0, len(pageCode)):
    imgUrl = 'http://danbooru.donmai.us' + pageCode[i].get('data-file-url')
    print('Downloading image number %s' %i)
    res = requests.get(imgUrl)
    res.raise_for_status()
    imageFile = open(os.path.join('danb', os.path.basename(imgUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

