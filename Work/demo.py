import allure

@allure.step(title="传入的两个数为：{0},{1}")
def sum(a, b):
    return int(a + b)