""" Get the most common 10000 words """

from bs4 import BeautifulSoup
import requests
from string import ascii_uppercase

url="https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016)"

##########
# Functions
##########


def pulltext(instring) -> str :
    # take the element and extract just the element(word) from it
    outstring:str=instring.text
    # strip non-ascii
    outstring=outstring.encode(encoding="ascii",errors="ignore")
    outstring=outstring.decode("ascii")
    return(outstring)


def clean(instring:str)->str :
    outstring:str=instring.strip().upper()
    return(outstring)

def badword(word:str)->bool:
    # The logic might seem backward because we
    # want to say True if the word does not qualify
    out=False
    condition1=(' ' in word) #cannot have multi-word string
    condition2=(word[0] in ascii_uppercase) #Cannot be proper name
    condition3=(word in wordlist)#Can not be a repeat
    if any([condition1,
            condition2,
            condition3
          ]):
        out=True
    return(out)


################
# Main program
################


print("Attempting to get the most common 10 thousand words from Wikitionary")

wordlist: list[str] =[]

response = requests.get(url)
if response.status_code!=200:
    print('Could not find the page')
else:
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all 10 sections
    for kiloword in range(10):
        parsestring ='div.mw-content-ltr.mw-parser-output p:nth-child('
        parsestring+=str(7+ (2*kiloword) )
        parsestring+=') a'
        words=soup.select(parsestring)

        for item in range(len(words)):
            word=pulltext(words[item])
            # This list also contains phrases. They will contain a space Do not include those
            # This list contains proper names. They will start with a capital letter
            # Do not include these
            if not badword(word):
                wordlist.append(clean(word))
        print('Getting '+str(1+(kiloword)*1000)+'-'+str((kiloword+1)*1000)+' most common words')
        # 'most common' in this case is most common used in Wikipedia

    print(f"\nRetrieved {int(len(wordlist))} total words:")
    print (wordlist)
    # This page has repeats, phrases, and proper names
    # So we dont have exactly 10000
    #print(len(wordlist))
    # from here, we can copy wordlist into a file or whatever we need it for
