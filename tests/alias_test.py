# coding: utf8

import json
from unittest import TestCase

from unittest.mock import patch, MagicMock

from abathur.alias import AliasManager, NotSupportException
from abathur.constant import REMOTE_RESOURCE, LOCAL_RESOURCE


class AliasManagerTest(TestCase):

    @patch("abathur.alias.require")
    @patch("abathur.alias.os")
    def setUp(self, mock_os, mock_require):
        mock_fd = MagicMock()
        mock_fd.return_value.read.return_value = json.dumps(dict(
            alias=dict(uri_type="__local_resource__", uri="test")
        ))
        mock_require.return_value.__enter__ = mock_fd

        mock_os.path.abspath.return_value = "test"

        self.manager = AliasManager()

    def test_should_success_load_alias_without_configuration(self):
        self.assertEqual(len(self.manager.aliases), 1)

    @patch("abathur.alias.os")
    def test_should_success_judge_https_link_as_remote(self, mock_os):
        mock_os.path.exists.return_value = False
        url = "https://github.com/yeyuexia/abathur.git"

        self.assertEqual(AliasManager.get_resource_type(url), REMOTE_RESOURCE)

    @patch("abathur.alias.os")
    def test_should_success_judge_ssh_link_as_remote(self, mock_os):
        mock_os.path.exists.return_value = False
        url = "git@github.com:yeyuexia/abathur.git"

        self.assertEqual(AliasManager.get_resource_type(url), REMOTE_RESOURCE)

    @patch("abathur.alias.os")
    def test_should_success_judge_local_uri_as_local(self, mock_os):
        mock_os.path.exists.return_value = True
        url = "git@github.com:yeyuexia/abathur.git"

        self.assertEqual(AliasManager.get_resource_type(url), LOCAL_RESOURCE)

    @patch("abathur.alias.os")
    def test_should_throw_not_support_exception(self, mock_os):
        mock_os.path.exists.return_value = False
        url = "www.baidu.com"

        try:
            self.manager.get_resource_type(url)
        except NotSupportException:
            pass
        else:
            self.fail()

    def test_success_alias_by_name(self):
        self.assertEqual(self.manager.get("alias").to_dict(), dict(
            uri="test", uri_type="__local_resource__"
        ))
