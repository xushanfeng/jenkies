#encoding:utf-8
import allure

@allure.step(title="传入的两个数为：{0},{1}")
def sum_1(a, b):
    return int(a + b)