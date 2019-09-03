# module that requests info from a web page
import requests
# module that allows user to go through a website and sort through data you want
from bs4 import BeautifulSoup


# create a function to crawl the Find Jobs site on Indeed
def find_jobs_page_crawler(max_start_value):
    start = 0
    while start <= max_start_value:
        url_to_scrape = "https://www.indeed.com/jobs?q=Summer+Data+Science+Internship&start=" + str(start)
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
            # to get the name of the job
            job_title = job_link.string
            print(href)
            print(job_title)
        start += 10


# get employer data for single job posting
def employer_info(employer_url):
    source_code = requests.get(employer_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for employer in soup.findAll("a", {"class": "turnstileLink"}):
        href = employer.get("href")
        print(href)


find_jobs_page_crawler(70)
employer_info(href)
