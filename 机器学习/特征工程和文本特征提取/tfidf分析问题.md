#### Tf 词的频率
#### idf 逆文档频率

```python
import sklearn.feature_extraction import TfidfVectorizer

tf = TfidfVectorizer()

data = tf.fit_transform([{"人生苦短"},{"我爱python"}])

print(tf.get_feature_names())

print(data.toarray())
```