import extruct as ex
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from .db import insert_into_table, mydb


def get_driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def get_source(driver, url):
    driver.get(url)
    return driver.page_source

def get_json(source):
    return ex.extract(source, syntaxes=['json-ld'])

def get_next_page(driver):
    elements = driver.find_elements(By.XPATH, '//link[@rel="next"]')
    if elements:
        return driver.find_element(By.XPATH, '//link[@rel="next"]').get_attribute('href')
    else:
        return ''


def save_data(data, df, table_name, category):
    if data['json-ld']:
        for item in data['json-ld']:
            if "itemListElement" in item:
                for product in item['itemListElement']:
                    new_product = product['item']
                    if not isinstance(new_product, str):
                        row = {
                            'name': new_product.get('name'),
                            'price': new_product.get('offers').get('highPrice'),
                            'valid_until': new_product.get('offers').get('offers')[0].get('priceValidUntil'),
                            'category': category
                        }
                        params = (row.get('name'), row.get('price'), row.get('valid_until'), row.get('category'))
                        
                        insert_into_table(table_name, params)

                        new_df = pd.DataFrame([row])
                        df = pd.concat([df, new_df], axis=0, ignore_index=True)
        return df
    else:
        print(data)