import unittest
from parameterized import parameterized
from API_Yandex import YaDisk


class TestAPI(unittest.TestCase):
    # Перед запуском первого теста убеждаемся в отсутствии создаваемой папки на диске
    @parameterized.expand([
        ("", '<Response [201]>'),
        ("", '<Response [409]>')
    ])  #Передать токен в качестве аргумента декоратора parameterized.expand
    def test_cls_YaDisk(self, token, response):
        testing = YaDisk(token)
        results = str(testing.new_folder())
        etalon = response
        self.assertEqual(results, etalon)

    @parameterized.expand([
        ("123456789qwertyuio", '<Response [201]>'),
        ("123456789qwertyuio", '<Response [409]>')
    ])
    @unittest.expectedFailure
    def test_cls_YaDidk_failure(self, token, response):
        testing = YaDisk(token)
        results = str(testing.new_folder())
        etalon = response
        self.assertEqual(results, etalon)

