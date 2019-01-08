import os

sql = 'curl http://10.156.10.81:6800/cancel.json -d project=zhidao_spider -d job=3c2cd75805ab11e9bf3b6045cb1c53b6'
os.system(sql)