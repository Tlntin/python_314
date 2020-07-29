from flask import Flask, render_template, request
import pandas as pd
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/test/<int:num>/')
def test(num):
    data = get_data(num)
    data.insert(0, num)
    data[4] = '★' * int(data[4]) + '☆' * (5 - int(data[4]))
    # print(data[5])
    # print(data[4])
    return render_template('test.html', data=data)


def get_data(num, data_path='data_raw.csv'):
    """
    编写一个获取题目的函数，题目储存在csv
    :param num: int类型，题目id
    :param data_path: 数据储存的位置，默认存同目录
    :return:
    """
    df = pd.read_csv(data_path, index_col=0)
    data1 = df.iloc[num-1].values.tolist()  # 获取一行的值
    option_str = data1[4]
    option_list = parse_content(option_str)
    data1[4] = option_list
    row_num = data1[2].count('\n')
    data1.append(row_num)
    return data1


def parse_content(content: str):
    """
    将字符串格式的content转回list
    :param content: 内容
    :return:
    """
    content = content.replace('[\'', "")  # 去除左括号
    content = content.replace('\']', "")  # 去除右中括号
    content = content.replace(' \'', "")  # 去除 `符号
    option_list = content.split('\',')
    dict1 = {}
    for i in range(65, 65 + len(option_list)):
        key = chr(i)
        dict1[key] = option_list[i-65]
    return dict1


if __name__ == '__main__':
    app.run(port=8005)
    # data = get_data(1)
    # print(data)