"""
Web Scrapper made by : Naman Garg
Section : CS A 04
Roll Number : 12112061
Contact: <12112061@nitkkr.ac.in>

NIT Scrapped in this project are:

1. NIT Uttarakhand
2. NIT Puducherry
3. NIT Arunachal Pradesh
4. NIT Sikkim
5. NIT Delhi
6.NIT Mizoram
7. NIT Nagaland
8. NIT Andhra Pradesh
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

import docx

doc = docx.Document()

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

#============================================================================================= 1. NIT Uttarakhand =============================================================================================

doc.add_heading("1. NIT Uttarakhand", 0)
doc.add_paragraph("Full Name \n Designation \n Email ID \n Contact Number \n Research area")

url_list = ['https://nituk.ac.in/computer-science-engineering/peoples', 'https://nituk.ac.in/civil-engineering/peoples',
            'https://nituk.ac.in/electrical-engineering/peoples', 'https://nituk.ac.in/electronics-engineering/peoples',
            'https://nituk.ac.in/mechanical-engineering/peoples'
            ]
for page in url_list:
    driver.get(page)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    s = soup.find_all("td")

    for faculty in s:
        facultyData = faculty.text

        # Skip, because not all td are faculty
        if facultyData.find("Designation") == -1:
            continue

        facultyData = facultyData.strip().split("\n")
        # Faculty Name
        fac_name = facultyData[0].strip()

        # Designation
        fac_designation = facultyData[2].split(":")[1]

        # Email ID
        if len(facultyData) >= 5:
            fac_email = facultyData[4].split(":")[1].strip()
        else:
            fac_email = "-"

        fac_phone = "-"
        # Phone Number
        if len(facultyData) >= 4:
            for string in facultyData[3].split():
                if string.isnumeric():
                    fac_phone = string
                    break

        fac_research = "-"

        if len(facultyData) >= 6:
            fac_research = facultyData[5].split(":")[1].strip()

        doc.add_paragraph("\n==============================================================\n" +
                          fac_name + " \n" + fac_designation + " \n " + fac_email + " \n " +
                          fac_phone + " \n " + fac_research)

doc.add_page_break()
doc.save('output.docx')
print("Done NIT Uttarakhand")

