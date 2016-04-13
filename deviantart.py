import requests, os, bs4, re

os.makedirs('deviantart', exist_ok=True)

# download gallery page and parse
galleryUrl = 'http://andyfairhurst.deviantart.com/gallery/'
res = requests.get(galleryUrl)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
galleryElem = soup.select('.tt-fh')

# pull image links from each and download
for i in range(0, len(galleryElem)):
    pictureUrl = str(galleryElem[i]).split('data-super-img="')[1].split('" ')[0]
    print('Downloading image %s of %s' % (i+1, len(galleryElem)))
    res_pic = requests.get(pictureUrl)
    res_pic.raise_for_status()
    pictureFile = open(os.path.join('deviantart', os.path.basename(pictureUrl)), 'wb')
    for chunk in res_pic.iter_content(100000):
        pictureFile.write(chunk)
    pictureFile.close()


'''
# download single page image and loop
url = 'http://wiwionart.deviantart.com/art/Let-us-move-closer-595704589'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

pageElem = soup.select('.dev-content-normal')
imageUrl = pageElem[0].get('src')
res_img = requests.get(imageUrl)
res_img.raise_for_status()

print('Downloading image')
imageFile = open(os.path.join('deviantart', os.path.basename(imageUrl)), 'wb')
for chunk in res_img.iter_content(10000):
    imageFile.write(chunk)
imageFile.close()

help(open)
'''