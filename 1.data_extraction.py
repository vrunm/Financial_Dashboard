from sec_api import ExtractorApi # https://sec-api.io/
import pandas as pd              # for handling data
import re                        # cleaning data
   

# This will return Company's Name from URL string.

def return_company_name(url):
  company_name = []

  for i in url[::-1]:
    if i == '/':
      break
    
    company_name.append(i)

  return ''.join(company_name[-4:])[::-1]
  
# Function to  extract required sections from 10-K file and returns a Dataframe

def extractor_filing(extractorApi, filing_url, section):

  rows = []

  for url in filing_url:

    dict_ = {}

    columns = ["Company", "Reporting_Date"]

    elements = [return_company_name(url), url[-12:-4]]

    for sec in section:

      extracted_section = extractorApi.get_section(url, sec, "text")
      cleaned_section = re.sub(r"\n|[0-9]+;", "", extracted_section)

      columns.append(sec)
      elements.append(cleaned_section)
      
    rows.append(elements)

  return pd.DataFrame(rows, columns=columns)
 
#Set the SEC Api key

extractorApi = ExtractorApi("fcb2dcbdd4fead6b697c30ec7f025e0a00cb65eb25318217be3396d0950e49e3")
       
#Selecting the sections to extract 

section = ["1", "1A", "1B", "2", "3", "5", "7", "7A", "8", "9A"]

# Function call

results = extractor_filing(extractorApi, filing_url, section)

results




  
  
