from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import time


#nasa website crawler to get the POD
class Nasa(commands.Cog):
    
    url = ""
    
    def __init__(self, bot):
        url = self.getUrl()
        self.bot = bot

    def getIndex(self, explanation) -> int: 
        
        endings = ["Notable APOD Image", "Share the Sky", "Tomorrow's picture:"]
       
        for end in endings:
            if not(explanation.text.find(end) == -1):
                return explanation.text.find(end)
        
        return -1
    
    def getUrl(self) -> str:
        
        current = time.localtime(time.time())
            
        day = "0" + str(current.tm_mday) if current.tm_mday <= 9 else current.tm_mday
        month = "0" + str(current.tm_mon) if current.tm_mon <= 9 else current.tm_mday
            
        #url = "https://apod.nasa.gov/apod/ap210725.html"
        url = "https://apod.nasa.gov/apod/ap{}{}{}.html".format(str(current.tm_year)[2:], month, day)
        
        if(requests.get(url).status_code == 200):
            return url
        else:
            print("Error as occured getting url")   
            return     

    def getPicture(self): # works
        
        base = "https://apod.nasa.gov/apod/"
        link = ""
        
        #annotated_picture = https://apod.nasa.gov/apod/image/2108/PerseidRain2021_Luo_960_annotated.jpg
        
        r = requests.get(self.getUrl())
        
        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("img") # only one in page
        
        for p in paragraphs:
            link = base + p["src"]
        
        return link

    def AstronomyPictureOfTheDayText(self) -> str: # works
        
        r = requests.get(self.getUrl())
        
        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find("center").find("h1")
        
        content = str(paragraphs)[5:-5]
        
        return content

    def getName(self): # works
        
        r = requests.get(self.getUrl())
        
        soup = BeautifulSoup(r.text, "html.parser")

        b = soup.find_all("center")[1].find_next("b")
        
        return str(b)[3:-4].strip()

    def getCredit(self) -> str: # works
        
        r = requests.get(self.getUrl())
        
        soup = BeautifulSoup(r.text, "html.parser")
        
        credit = soup.find_all("center")[1].find_all_next("b")[1].text.strip()
        
        author = soup.find_all("center")[1].text[soup.find_all("center")[1].text.find("Copyright:") + len("Copyright:"):]
        
        arr = author.strip().split(" ")
        
        author = ""
        for i in range(len(arr)):
            if "\n" in arr[i]:
                arr[i] = arr[i].replace("\n", "")
            
            author += arr[i] + " "
        
        return credit + " " + author.strip()

        
    def getNextPOD(self) -> str:
        
        r = requests.get(self.getUrl())
        
        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("p")
        
        explanation = paragraphs[2]
        
        index = explanation.text.find("Tomorrow's picture:")
        index_text = explanation.text[index:]
        end = index_text.find("<")
        
        return index_text[:end].strip()
    
    #gets the explanation and makes it more readable 
    def getExplanation(self):
        
        s = []
        
        r = requests.get(self.getUrl())
        
        
        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("p")
        
        explanation = paragraphs[2]
        
        index = self.getIndex(explanation)
      
        if(index == -1):
            print("Check site")
            return
        
        s = explanation.text[:index].split(sep=".")
        
        t = []
        for line in s:
            t.append(line.split(" "))#splitting each word in each sentence by a space
        
        paragraph = ""
        for row in t: #sentence
            
            
            if len(row) <= 3:
                continue
            
            sentence = ""
            for word in range(len(row)): # word
                w = ""
                for char in row[word]:
                    if char == "\n":
                        w += " "
                    else:
                        w += char
                
                sentence += w
                sentence += " "
            
            print(len(sentence))
            
            print("\nSentence: {}".format(sentence))
            if(len(sentence) < 1):
                continue
            else:
                sentence = sentence.strip()
                sentence += "."
                sentence += "\n\n"
            
            paragraph += sentence
           
        
        return paragraph
    
    def getUrlByDate(date: str) -> str:
        pass
        
    
'''
TO DO: 
using the list of archives in https://apod.nasa.gov/apod/archivepix.html, make it where i can access any date i want from 2015 to current day
'''

def setup(bot):
    bot.add_cog(Nasa(bot))