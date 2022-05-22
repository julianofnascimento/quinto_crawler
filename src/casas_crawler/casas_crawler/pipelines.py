# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from mysql import connector


class CasasCrawlerPipeline:
    def process_item(self, item, spider):
        sql, val = self._build_query(item)
        mydb = self._connect()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        return item

    def _connect(self):
        mydb = connector.connect(
            host="35.199.79.204",
            user="crawler",
            password=",e=\[Ho*dU'}%PSn",
            database="houses"
        )

        return mydb

    def _build_query(self, item):
        columns = [
            'link',
            'business_context',
            'area',
            'bedrooms',
            'city',
            'bathrooms',
            'iptu',
            'rent_price',
            'condo_price',
            'type',
            'latitude',
            'longitude',
            'floor',
            'near_subway',
            'sale_price',
            'construction_year',
            'suites'
        ]
        val = (
            item['link'],
            item['business_context'],
            item['area'],
            item['bedrooms'],
            item['city'],
            item['bathrooms'],
            item['iptu'],
            item['rent_price'],
            item['condo_price'],
            item['type'],
            item['latitude'],
            item['longitude'],
            item['floor'],
            item['near_subway'],
            item['sale_price'],
            item['construction_year'],
            item['suites'],
            item['state']
        )
        sql = "INSERT INTO imoveis_quinto_andar\
            (\
                link,\
                business_context,\
                area,\
                bedrooms,\
                city,\
                bathrooms,\
                iptu,\
                rent_price,\
                condo_price,\
                type,\
                latitude,\
                longitude,\
                floor,\
                near_subway,\
                sale_price,\
                construction_year,\
                suites,\
                state\
            )\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                     %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        return sql, val

        

    

