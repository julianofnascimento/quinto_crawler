import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from casas_crawler.items import CasasCrawlerItem
from bs4 import BeautifulSoup as bs
import json

HOUSE_INFO_PATH = ['props', 'pageProps', 'initialState', 'house', 'houseInfo']
BUSINESS_CONTEXT_PATH = ['props', 'pageProps', 'initialState', 'route', 'businessContext']
HOUSE_INFO_VALUES = ['bedrooms', 'city', 'bathrooms', 'iptu', 'area', 'rentPrice', 'condoPrice',
                     'type', 'address', 'floor', 'isNearSubway', 'salePrice', 'constructionYear', 'suites']


class QuintoAndarSpider(CrawlSpider):
    name = 'quinto_andar'
    allowed_domains = ['www.quintoandar.com.br']
    start_urls = ['https://www.quintoandar.com.br/']

    rules = (
        Rule(LinkExtractor(allow=('imovel', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = CasasCrawlerItem()
        try:
            item = self._build_item(item, response)
            return item
        except:
            pass

    def _build_item(self, item, response):
        bs_object = bs(response.text)
        application_json = bs_object.find(attrs={"id": "__NEXT_DATA__"})
        imovel_data = json.loads(application_json.getText())

        item['link'] = response.url
        item['area'] = self._find_prop(imovel_data, 'area')
        item['bedrooms'] = self._find_prop(imovel_data, 'bedrooms')
        item['city'] = self._find_prop(imovel_data, 'city')
        item['bathrooms'] = self._find_prop(imovel_data, 'bathrooms')
        item['iptu'] = self._find_prop(imovel_data, 'iptu')
        item['rent_price'] = self._find_prop(imovel_data, 'rentPrice')
        item['condo_price'] = self._find_prop(imovel_data, 'condoPrice')
        item['type'] = self._find_prop(imovel_data, 'type')
        item['latitude'] = self._find_prop_address(imovel_data, 'lat')
        item['longitude'] = self._find_prop_address(imovel_data, 'lng')
        item['state'] = self._find_prop_address(imovel_data, 'stateAcronym')
        try:
            item['floor'] = self._find_prop(imovel_data, 'floor')
        except:
            item['floor'] = 0
        item['near_subway'] = self._find_prop(imovel_data, 'isNearSubway')
        item['sale_price'] = self._find_prop(imovel_data, 'salePrice')
        item['construction_year'] = self._find_prop(imovel_data, 'constructionYear')
        item['suites'] = self._find_prop(imovel_data, 'suites')
        item['business_context'] = self._find_prop_business_context(imovel_data)
        item['id'] = self._find_prop(imovel_data, 'id')

        return item

    def _find_prop(self, data, prop):
        for element in HOUSE_INFO_PATH:
            data = data[element]

        return data[prop]

    def _find_prop_address(self, data, prop):
        for element in HOUSE_INFO_PATH:
            data = data[element]

        return data['address'][prop]

    def _find_prop_business_context(self, data):
        for element in BUSINESS_CONTEXT_PATH:
            data = data[element]

        return data

