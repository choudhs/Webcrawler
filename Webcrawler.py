# module that requests info from a web page
import requests
# module that allows user to go through a website and sort through data you want
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# create a function to crawl the Find Jobs site on Indeed
def find_jobs_site_crawler(max_start_value):
    start = 0
    while start <= max_start_value:
        url_to_scrape = "https://www.indeed.com/jobs?q=Data+Science+Summer+Intern&start=" + str(start)
        # request data from the url loaded above and store the results
        source_code = requests.get(url_to_scrape, allow_redirects=False)
        # take the text from the above requests and store it
        plain_text = source_code.text
        # create BS object
        soup = BeautifulSoup(plain_text, features="html.parser")
        # tell BS to pull out all the title names of the jobs
        for job_link in soup.findAll("a", {"class": "jobtitle turnstileLink visited"}):
            # get the urls of the job titles
            href = job_link.get("href")
            job_title = job_link.string
            print(href)
            print(job_title)
            single_job_data(href)
        start += 10


# get info on one single job posting
def single_job_data(job_title_url):
    source_code = requests.get(job_title_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for job_title in soup.findAll("div", {"class": "title"}):
        print(job_title.string)


find_jobs_site_crawler(70)
