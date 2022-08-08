import unittest
from unittest.mock import patch
from parameterized import parameterized
from app import *


class TestFunctions(unittest.TestCase):

    @parameterized.expand([("10006", True), ("10007", False), ("11-2", True)])
    def test_check_document_existance(self, user_doc_number, doc_founded):
        results = check_document_existance(user_doc_number)
        etalon = doc_founded
        self.assertEqual(results, etalon)

    @parameterized.expand([("10006", "Аристарх Павлов"), ("10007", None), ("11-2", "Геннадий Покемонов")])
    def test_get_doc_owner_name(self, user_doc_number, name):
        etalon = name
        # Имитируем пользовательский ввод
        with patch("builtins.input", return_value=user_doc_number):
            results = get_doc_owner_name()
            self.assertEqual(results, etalon)

    def test_get_all_doc_owners_names(self):
        results = get_all_doc_owners_names()
        etalon = {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'}
        self.assertEqual(results, etalon)

    @parameterized.expand([("1", ("1", False)), ("3", ("3", False)), ("5", ("5", True))])
    def test_add_new_shelf(self, shelf_number, response):
        etalon = response
        # Имитируем пользовательский ввод
        with patch("builtins.input", return_value=shelf_number):
            results = add_new_shelf()
            self.assertEqual(results, etalon)

    @parameterized.expand([("10006", "2"), ("10007", None), ("2207 876234", "1")])
    def test_get_doc_shelf(self, doc_number, directory_number):
        etalon = directory_number
        # Имитируем пользовательский ввод
        with patch("builtins.input", return_value=doc_number):
            results = get_doc_shelf()
            self.assertEqual(results, etalon)

    @parameterized.expand(
        [("10006", "1", ("10006", "1")), ("10007", "4", ("10007", "4")), ("2207 876234", "3", ("2207 876234", "3"))]
    )
    def test_move_doc_to_shelf(self, user_doc_number, user_shelf_number, response):
        etalon = response
        # Имитируем пользовательский ввод
        with patch("builtins.input", side_effect=[user_doc_number, user_shelf_number]):
            results = move_doc_to_shelf()
            self.assertEqual(results, etalon)

    def test_show_all_docs_info(self):
        etalon = ['passport "2207 876234" "Василий Гупкин"',
                  'invoice "11-2" "Геннадий Покемонов"',
                  'insurance "10006" "Аристарх Павлов"']
        results = show_all_docs_info()
        self.assertEqual(results, etalon)

    # @parameterized.expand([("12345", "passport", "Mr.BAZINGA", "3"), ("54321", "who will read this?", "Пыж", "2")])
    # def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number):
    #     etalon = new_doc_shelf_number
    #     # Имитируем пользовательский ввод
    #     with patch(
    #             "builtins.input", side_effect=[new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number]
    #     ):
    #         results = add_new_doc()
    #         self.assertEqual(results, etalon)
    #
    # @parameterized.expand([("10006", ("10006", True)), ("10007", None), ("11-2", ("11-2", True))])
    # def test_delete_doc(self, doc_number, response):
    #     etalon = response
    #     # Имитируем пользовательский ввод
    #     with patch("builtins.input", return_value=doc_number):
    #         results = delete_doc()
    #         self.assertEqual(results, etalon)
"""Последние 2 теста запускать отдельно, т.к. вносят изменения при работе"""