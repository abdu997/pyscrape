import csv
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def find_element(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)

def find_elements(driver, selector):
    return driver.find_elements(By.CSS_SELECTOR, selector)

def store_in_templates(templates):
    store_in_file('templates.json', templates)

def store_in_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def get_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(chrome_options=chrome_options, service=Service(ChromeDriverManager().install()))

def get_file(filename):
    return open(filename)

def get_templates_json():
    return get_json_file('templates.json')

def get_media_json():
    return get_json_file('media.json')

def get_json_file(filename):
    f = get_file(filename)
    return json.load(f)

def csv2json(csvFilePath):
    data = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for row in csvReader: 
            data.append(row)    
    return data

def json2csv(filename, data):
    data_file = open(filename, 'w')
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    count = 0
    for dict in data:
        if count == 0:
            header = dict.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(dict.values())
    data_file.close()

def fixtemplates():
    templates = get_templates_json()
    templatestodelete = []
    for i, template in enumerate(templates):
        for j in range(i):
            if template['template_name'] == templates[j]['template_name']:
                templates[j]['categories'].extend(template['categories'])
                # templatestodelete.append(templates[i]['template_name'])
                templatestodelete.append(i)

                break
    templatestodelete.reverse()
    for d in templatestodelete:
        del templates[d]
    store_in_templates(templates)
    