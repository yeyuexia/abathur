# coding: utf8

import os.path
from unittest import TestCase

from abathur.builder import TemplateBuilder


class BuilderTest(TestCase):
    ignore_dir = "test_ignore_dir"
    ignore_hide_file = ".ignore"

    ignores = [ignore_dir, r"(.*/)?\.ignore.*"]

    def setUp(self):
        placeholders = dict(placeholder1="aaaaaa", p2="bbbb", p3="ccccccc")
        self.builder = TemplateBuilder(
            "project", "source", "desc", placeholders, self.ignores
        )

    def test_should_success_ignore_all_files_ignore_directory(self):
        self.assertTrue(
            self.builder.is_ignored(os.path.join(self.ignore_dir, "aaa"))
        )
        self.assertTrue(
            self.builder.is_ignored(
                os.path.join(self.ignore_dir, "abc", "1aa")
            )
        )

    def test_should_success_ignore_hide_file(self):
        self.assertTrue(
            self.builder.is_ignored(self.ignore_hide_file)
        )

    def test_should_success_ignore_hide_file_in_directory(self):
        self.assertTrue(
            self.builder.is_ignored(os.path.join("dir", self.ignore_hide_file))
        )

    def test_should_success_ignore_hile_directory(self):
        self.assertTrue(
            self.builder.is_ignored(
                os.path.join(self.ignore_hide_file, "adbasd")
            )
        )

    def test_should_replace_all_placeholder(self):
        src = "abc/placeholder1_p2_asd_p4_p3"
        result = self.builder.replace(src)
        self.assertEqual(result, "abc/aaaaaa_bbbb_asd_p4_ccccccc")
