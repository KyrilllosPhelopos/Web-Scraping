import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

jop_title = []
address = []
job_skill = []
company_name = []



result = requests.get("https://wuzzuf.net/search/jobs/?q=embedded&a=hpb")
src = result.content
soup = BeautifulSoup(src , "lxml")

jop_titles = soup.find_all("h2", {"class": "css-m604qf"})

company_names = soup.find_all("a" , {"class":"css-17s97q8"})

addresses = soup.find_all("span" , {"class":"css-5wys0k"})

job_skills = soup.find_all("div", {"class":"css-y4udm8"})

for i in range(len(jop_titles)):
    jop_title.append(jop_titles[i].text)
    address.append(addresses[i].text)
    job_skill.append(job_skills[i].text)
    company_name.append(company_names[i].text)

file_list = [jop_title , company_name , address , job_skill]
exported = zip_longest(*file_list)

with open(r"C:\Users\phelp\OneDrive\Desktop\web scraping\WUZZUF\jobsInfo.csv", "w") as out_file:
    wr = csv.writer(out_file)
    wr.writerow(["Job title" , "Company name", "Location", "Skills"])
    wr.writerows(exported)
