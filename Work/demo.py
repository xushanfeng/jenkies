import allure

@allure.step(title="传入的两个数为：{1},{2}")
def sum(a, b):
    return int(a + b)