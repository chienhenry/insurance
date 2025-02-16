# 第九章/generate_model.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)
# 读取数据集，并指定字符编码为gbk，防止中文报错
insurance_df = pd.read_csv('data/insurance-chinese.csv', encoding='gbk')

# 定义医疗费用为目标输出变量
output = insurance_df['医疗费用']

# 使用年龄、性别、BMI、子女数量、是否吸烟、区域作为特征列
features = insurance_df[['年龄', '性别', 'BMI', '子女数量', '是否吸烟', '区域']]
# 对特征列进行独热编码
features = pd.get_dummies(features)


# 从features和output 这两个数组中划分数据集为训练集和测试集。
# 训练集为80%，测试集为20%（1-80%）
# 返回的x_train和 y_train为划分得到的训练集特征和标签。
# x_test和y_test为划分得到的测试集特征和标签。
# 这里标签和目标输出变量是一个意思

x_train, x_test, y_train, y_test = train_test_split(features, output, train_size=0.8)

# 构建一个随机森林回归模型的实例
rfr = RandomForestRegressor()

# 使用训练集数据x_train和y_train来拟合(训练)模型。
rfr.fit(x_train, y_train)

# 用训练好的模型rfr对测试集数据x_test进行预测，预测结果存储在y_pred中
y_pred = rfr.predict(x_test)

# 计算模型的可决系数（R-squared）
# - R-squared的值界定在0-1之间。
# - R-squared接近0,表示模型仅能做出与平均值相当的预测。
# - R-squared接近1,表示模型对数据的变异有很好的解释能力。
# - 一般来说,R-squared值超过0.5以上才被认为模型有良好的预测能力

r2 = r2_score(y_test, y_pred)
print(f'该模型的可决系数（R-squared）是：{r2}')
