import os

sql = 'curl http://127.0.0.1:6800/cancel.json -d project=zhidao_spider -d job=3f71ca7e05b311e9beca9c5c8e259bb2'
os.system(sql)