# coding: utf8

from unittest import TestCase
from unittest.mock import patch

from abathur.abathur import *


class AbathurTest(TestCase):

    @patch("abathur.abathur.os.path")
    def test_get_empty_config_when_target_is_not_abathur_config_file(self, mock_path):
        mock_path.join.return_value = "config"
        mock_path.exists.return_value = False
        self.assertEqual(get_abathur_config("aaa"), list())

    @patch("abathur.abathur.os.path")
    def test_get_empty_config_when_target_is_not_a_file(self, mock_path):
        mock_path.join.return_value = "config"
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = False
        self.assertEqual(get_abathur_config("aaa"), list())

    @patch("abathur.abathur.open")
    @patch("abathur.abathur.os.path")
    def test_get_empty_config_when_target_is_not_a_file(
            self, mock_path, mock_open
    ):
        mock_path.join.return_value = "config"
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = True

        mock_open.return_value.__enter__.return_value.readlines.return_value = [
            " abc  ", "bbb", "  ", "cba"
        ]
        self.assertEqual(
            get_abathur_config("aaa"), ["{abc}", "{bbb}", "{cba}"]
        )

    @patch("abathur.abathur.input")
    @patch("abathur.abathur.get_abathur_config")
    def test_success_load_replace_words_based_on_file(
            self, config_mock, input_mock):
        config_mock.return_value = ["{key}", "{words}", "{abathur}"]
        input_mock.return_value = "\n"

        result = process_configuration("config", {
            "{key}": "111", "{words}": "222", "{abathur}": "333", "{acc}": "44"
        }, "test")

        self.assertEqual(
            result, {
                "{key}": "111",
                "{words}": "222",
                "{abathur}": "333",
                "{PROJECT_NAME}": "test"
            }
        )

    @patch("abathur.abathur.input")
    @patch("abathur.abathur.get_abathur_config")
    def test_success_load_replace_words_for_project_name(
            self, config_mock, input_mock):
        config_mock.return_value = []
        input_mock.return_value = "custom\n"

        result = process_configuration("config", {}, "test")

        self.assertEqual(result, {"{PROJECT_NAME}": "custom"})

    @patch("abathur.abathur.input")
    @patch("abathur.abathur.get_abathur_config")
    def test_load_replace_words_by_input(
            self, config_mock, input_mock
    ):
        config_mock.return_value = ["{key}", "{words}", "{abathur}", "{input}"]
        input_mock.return_value = "555"

        result = process_configuration("config", {
            "{key}": "111", "{words}": "222", "{abathur}": "333", "{acc}": "44"
        }, "test")

        self.assertEqual(
            result, {
                "{key}": "111",
                "{words}": "222",
                "{abathur}": "333",
                "{input}": "555",
                "{PROJECT_NAME}": "555"
            }
        )

    @patch("abathur.abathur.open")
    def test_success_load_custom_config(self, mock_open):
        mock_open.return_value.__enter__.return_value.readlines.return_value = [
            "key = value ",
            " a = 102 2"
        ]

        res = read_custom_config("config")
        self.assertEqual(res, {"{key}": "value", "{a}": "102 2"})
