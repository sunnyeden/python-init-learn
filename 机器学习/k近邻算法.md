##### 如果一个样本在特征空间中k个最相似(即特征空间最临近)的样本中的大多数属于某一个类别,则其也属于该类别

#### 两个样本的距离公式,也叫欧式距离

```python
a(a1, a2, a3) b(b1, b2, b3)

(a1-b1)^2 + (a2-b2)^2 + (a3-b3)^2 开根号
```

#### k近邻预测用户签到位置

```python
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd

def knncls():
    """
    x,y 用户坐标
    time 用户行动的时间戳
    place_id 签到人数总数特征
    """
    data = pd.read_csv('文件路径')

    # print(data.head(10))

    # 缩小范围
    data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

    # 处理时间戳到秒
    time_value = pd.to_datetime(data['time'], unit='s')

    # 返回时间字典格式
    time_value = pd.DatetimeIndex(time_value)

    # print(time_value)

    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 把时间戳删除, 1表示列
    data = data.drop(['time'], axis=1)

    # 处理签到位置
    place_count = data.groupby('place_id').count()

    tf = place_count[place_count.row_id > 3].reset_index()

    data = data[data['place_id'].isin(tf.place_id)]

    # 取出数据的特征值和目标值
    y = data['place_id'] # 目标值

    data = data.drop(['place_id'], axis=1)

    # 进行数据的分割训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 标准化
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train= std.fit_transform(x_train)

    x_test = std.transform(x_test)

    # 算法
    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(x_train, y_train)

    # 得出预测结果
    y_predict = knn.predict(x_test)

    print("预测的签到位置:", y_predict)

    # 得出准确率
    print("预测准确率:", knn.score(x_test, y_test))

if __name__ == "__main__":
    knncls()
```

#### 缺点

* k值很小: 容易受异常点影响

* k值很大: 容易受样本数量的波动

* 性能问题: 懒惰算法,对测试样本计算量大,内存开销大

#### 优点

* 简单,易于理解,易于实现,无需估计参数,无需训练
