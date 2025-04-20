# Web scraper to pull the most common 10 thousand words

### Part of a portfolio of Python projects developed by Brian Spangler

Demonstration of understanding Python, webscraping (BeautifulSoup) and text filtering

- Scrape Wikitionary  
- Eliminate words that dont fit
- Count total valid words 

A lot of people have this list including:  
- https://github.com/tgmgroup/Word-List-from-Google-10000  
- https://github.com/first20hours/google-10000-english  
-  https://www.mit.edu/~ecprice/wordlist.10000 

I chose https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016) 

The purpose of this code is not to reinvent the wheel but to show that I can webscarpaing tools.  

I chose this page to scrape because of the complicated nature.
Words are listed in 1000-word sections so I had to repeat the process 10 times.
It's also complicated to find the tags to scrape while inspecting the code.  

To find the tags to scrape, right-click on the webpage and click Inspect to expose the HTML.
In the console, find the element you want and Copy CSS Selector.
Then, search to find the exact nesting of tags in each section.

This list also included proper names and multi-word phrases. There is a section that eliminates them.

Requirements:  
Python 3.7+

> Sample output:  
> Getting the most common 10 thousand words from Wikitionary  
> Getting 1-1000 most common words  
> Getting 1001-2000 most common words  
> Getting 2001-3000 most common words  
> Getting 3001-4000 most common words  
> Getting 4001-5000 most common words  
> Getting 5001-6000 most common words  
> Getting 6001-7000 most common words  
> Getting 7001-8000 most common words  
> Getting 8001-9000 most common words  
> Getting 9001-10000 most common words  
> Retrieved 8068 total words  
>
> ['THE', 'OF', 'AND', 'TO', ...  

Future improvement:  
Currently, the word list is displayed in terminal. It can be saved into a file  
Statistics can be run on the words for length, common letters, patterns, etc   
