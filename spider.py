import requests
from pprint import pprint
from random import random
import time
from tqdm import tqdm
import re
import pandas as pd


def get_question(id_num):
    """
    获取题目id
    :param id_num:
    :return:
    """
    url = f'https://question-back.kaikeba.com/exam/question/detail/{id_num}?offset=0'
    url_answer = f'https://question-back.kaikeba.com/exam/question/answer/{id_num}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/85.0.4183.26 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data1 = response.json().get('data', {})
    class_name = title = difficulty = option_list = answer = answer_type = None
    # print(data)
    if data1 is not None:
        class_name = data1['subjectName']
        title = data1['content']
        difficulty = data1['difficulty']
        option_list = data1['options']
        answer_type = data1['type']
        if answer_type == 1:
            answer_type = '单选题'
        else:
            answer_type = '多选题'

    response2 = requests.get(url_answer, headers=headers)
    data_answer = response2.json().get('data', '')
    if data_answer is not None:
        answer = data_answer
    pprint(f'类别：{class_name}【{answer_type}】， 题目：{title}，难度：{difficulty}，选项：{option_list}， 答案：{answer}')
    data_list = [class_name, answer_type, title, difficulty, option_list, answer]
    return data_list


if __name__ == '__main__':
    # data = get_question(386)
    data_list2 = []
    columns_list = ['类别', '类型', '题目', '难度', '选项', '答案']
    for i in tqdm(range(359, 675)):  # 终点675
        data = get_question(i)
        data_list2.append(data)
        time.sleep(2 * random() + 0.3)
    df = pd.DataFrame(data_list2, columns=columns_list)
    df.to_csv('data_raw.csv', encoding='utf-8-sig')

