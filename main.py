import sys

sys.path.append('/lib')

from flask import Flask, jsonify, request

from lib.constants import EXITO_URL, OLIMPICA_URL
from lib.db import get_data, get_data_test
from lib.scrape import scrape_data

app = Flask(__name__)
app.secret_key = 'scrapedata_from_stores'

@app.route('/scrape/<site>/<category>', methods=['POST'])
def scrape_site(site, category):
    # when building the url just pass the category after a slash
    if site == 'olimpica':
        url = f'{OLIMPICA_URL}/{category}'
    if site == 'exito':
        url = f'{EXITO_URL}/{category}'
    try:
        scrape_data(url, site, category)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'message': 'Script ran successfully'}), 200

@app.route('/products/<site>/<category>', methods=['GET'])
def get_products(site, category):
    limit = request.args.get('limit')
    data = get_data(site, category, limit)

    return jsonify(data), 200

@app.route('/products', methods=['GET'])
def get_all():
    data = get_data_test()

    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)