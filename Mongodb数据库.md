#### 安装monogo

`pip install pymongo`

#### 使用

```python
from pymongo import MongoClient

class TestMongo:
    def __init__(self):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.collection = client['test']['t1'] # 选择数据库和集合

    def test_insert(self):
        ret = self.collection.insert({'name': 'test', 'age': 33})
        print(ret)

    def test_insert_many(self):
        item_list = [{'name': 'test' + i, 'age': i} for i in range(10)]
        t = self.collection.insert_many(item_list)

        for i in t.inserted_ids:
            print(i)

    def delete_one(self):
        ret = self.collection.delete_one({'name': 'test'})
        print(ret)

    def delete_many(self):
        ret = self.collection.delete_many({'name': 'test'})
        print(ret)
```