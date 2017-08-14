#encoding:utf-8
import allure

@allure.step(title="传入的两个数为：{1},{2}")
def sum_1(a, b):
    return int(a + b)