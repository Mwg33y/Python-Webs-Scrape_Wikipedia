# Python-Webs-Scrape_Wikipedia

Web Scraping with Python 

We can use Python code to extract information from the front end of a website. Python allows us to look at the HTML, CSS, and Javascript that are
used to construct the front end of web pages on the internet. Extracting data in this manner from some webpages may require permission from the 
owner. Web page owners who do not want their information accessed this way may set up anti-web-scraping software to prevent this. In some instances,
web scraping can be illegal due to personal, propietary, or sensitive information on a webpage.

A piece of web scraping code has limitations, and can not be generalized to all webpages. Web pages are structured differently according to their 
purporse (e.g. banking, youtube, newspaper, etc. ), so the web scraping code must be suited to each individual website. Some webpages are not static and
undergoes changes that can mean a complete alteration of the internal structure of the code used to build it. This can render our web scraping code 
useless. Web scraping code should be adjusted accordingly in such cases.

I used Python to extract paragraphs of information, tables, and images from a Wikipedia article about the annual Temperature data in Canada. I used the
'Beautifulsoup-4' and 'requests' packages in python to facilitate this. I chose to use Wikipedia because it is a high traffic public web site. 
