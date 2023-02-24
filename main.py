from flask import Flask

from lib.constants import EXITO_URL, OLIMPICA_URL
from lib.scrape import scrape_data

app = Flask(__name__)
app.secret_key = 'scrapedata_from_stores'

@app.route('/scrape', methods=['GET'])
def scrape_olimpica(category):
    # when building the url just pass the category after a slash
    url = f'{OLIMPICA_URL}/{category}'
    pass

@app.route('/categories')
def categories():
    pass