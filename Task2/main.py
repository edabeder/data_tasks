import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='html_file')


def scrape_items(url):
    request = requests.get(url)
    if request.status_code == 503:
        print('Amazon has blocked request, try again...')
        exit(0)

    soup = BeautifulSoup(request.content, 'html5lib')
    item_names = soup.findAll('span', class_='a-size-base-plus a-color-base a-text-normal')
    item_prices = soup.findAll('span', class_='a-offscreen')
    return list(zip(map(lambda x: x.string.replace('\xa0', ' ').strip(), item_names),
                    map(lambda x: x.string.replace('\xa0', ' ').strip(), item_prices)))


@app.route('/', methods=("POST", "GET"))
def html():
    return render_template('simple.html', items=items, len_items=len(items))


if __name__ == '__main__':
    page_url = 'https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1' \
               '%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid' \
               '=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4 '
    items = scrape_items(url=page_url)
    print(items)
    app.run(host='127.0.0.1')
