from bs4 import BeautifulSoup
import requests

post = "https://www.instagram.com/p/CS07JDVrRt4/"

postToJson = "?__a=1"

#add PostToJson to the end of post to get the post details in json

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

with open("test.txt", "w") as f:
    f.write(r.text)
