# coding: utf8

import json
from unittest import TestCase

from unittest.mock import patch, MagicMock

from abathur.alias import AliasManager
from abathur.constant import REMOTE_RESOURCE, LOCAL_RESOURCE


class AliasManagerTest(TestCase):

    @patch("abathur.alias.require")
    def setUp(self, mock_require):
        mock_fd = MagicMock()
        mock_fd.return_value.read.return_value = json.dumps(dict(
            alias=dict(uri_type="__local_resource__", uri="test")
        ))
        mock_require.return_value.__enter__ = mock_fd
        self.manager = AliasManager()

    @patch("abathur.alias.require")
    def test_should_success_load_alias_without_configuration(
            self, mock_require
    ):
        self.assertEqual(len(self.manager.aliases), 1)

    @patch("abathur.alias.os")
    def test_should_success_judge_https_link_as_remote(self, mock_os):
        mock_os.path.exists.return_value = False
        url = "https://github.com/yeyuexia/abathur.git"

        self.assertEqual(self.manager.get_resource_type(url), REMOTE_RESOURCE)

    @patch("abathur.alias.os")
    def test_should_success_judge_ssh_link_as_remote(self, mock_os):
        mock_os.path.exists.return_value = False
        url = "git@github.com:yeyuexia/abathur.git"

        self.assertEqual(self.manager.get_resource_type(url), REMOTE_RESOURCE)

    @patch("abathur.alias.os")
    def test_should_success_judge_local_uri_as_local(self, mock_os):
        mock_os.path.exists.return_value = True
        url = "git@github.com:yeyuexia/abathur.git"

        self.assertEqual(self.manager.get_resource_type(url), LOCAL_RESOURCE)
