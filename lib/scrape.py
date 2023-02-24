import pandas as pd

from lib.utils import (get_driver, get_json, get_next_page, get_source,
                       save_data)


def scrape_data(url):
    df = pd.DataFrame(columns=['name', 'price', 'valid_until'])
    driver = get_driver()
    source = get_source(driver, url)
    json = get_json(source)
    df = save_data(json, df)

    next_page = get_next_page(driver, source)
    paginated_urls = []
    paginated_urls.append(next_page)

    if paginated_urls:
        for url in paginated_urls:
            if url:
                driver = get_driver()
                source = get_source(driver, url)
                json = get_json(source)
                df = save_data(json, df)
                next_page = get_next_page(driver, source)
                paginated_urls.append(next_page)
                df.to_csv("data.csv")
        print('Saved to CSV file: data.csv')