import urllib.request
response = urllib.request.urlopen("http://placekitten.com/g/500/600")
cat_img = response.read()

with open('cat_500.jpg', 'wb') as img:
        img.write(cat_img)
