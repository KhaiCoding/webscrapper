import requests
from bs4 import BeautifulSoup

LIMIT = 50
PYTHON_URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"


def extract_indeed_pages():
    python_result = requests.get(PYTHON_URL)
    python_soup = BeautifulSoup(python_result.text, 'html.parser')
    pagination = python_soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')

    pages = []
    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


# jobs1 'html' = jobs2 'result'
def extract_indeed_jobs1(html):
    title = (html.find("div", {"class": "title"})).find("a")["title"]
    # Indeed not always provide Company name link - issue
    company = html.find("span", {"class": "company"})
    company_link = company.find("a")
    if company_link is not None:
        # make string : To remove blank in company name
        company = str(company_link.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    print(location)
    return {'title': title, 'company': company, 'location': location}


def extract_indeed_jobs2(last_page):
    jobs = []
    # for page in range(last_page):
    python_result = requests.get(f"{PYTHON_URL}&start={0*LIMIT}")
    python_soup = BeautifulSoup(python_result.text, 'html.parser')
    python_results = python_soup.find_all(
        "div", {"class": "jobsearch-SerpJobCard"})
    for result in python_results:
        job = extract_indeed_jobs1(result)
        jobs.append(job)
    return jobs
