# -*- coding: utf-8 -*-
from uuid import uuid4

from django.test import TestCase

from ..models import (
    user,
    website_manage,
)


class BaseModelTest(TestCase):

    superuser = None
    user = None

    user_username = 'user123'
    user_password = '123456'

    superuser_username = 'admin123'
    superuser_password = '123456'

    base_response_key = ['code', 'data', 'msg']

    @classmethod
    def setUpTestData(cls):
        """
        重写方法增加初始信息创建
        """
        # 创建用户
        cls.superuser = user.User.objects.create_superuser(
            cls.superuser_username,
            'admin123@admin.com',
            cls.superuser_password,
            phone=uuid4().hex[:11],
        )
        cls.user = user.User.objects.create_user(
            cls.user_username,
            'user123@admin.com',
            cls.user_password,
            phone=uuid4().hex[:11],
        )
        # 创建website_manage
        old_website_manage = website_manage.WebsiteManage.objects.all()
        if not old_website_manage.exists():
            website_manage.WebsiteManage.objects.create(
                website_name='测试',
                ICP_number='测试123456',
                website_image='https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg',
                ad_1='https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg',
                ad_1_url='https://www.qq.com/',
                ad_2='https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg',
                ad_2_url='https://www.qq.com/',
                github='https://www.qq.com/',
                email='admin@admin.com',
                friendship_link='http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com;'
                                'http://www.1.com'
            )

    def check_key_in_dict(self, key_list, check_dict):
        """
        检测key是否在dict里面
        :param key_list: 待检测的key的list
        :type key_list: list
        :param check_dict: 待检测的dict
        :type check_dict: dict
        :rtype: bool
        """
        self.assertIsInstance(key_list, list)
        self.assertIsInstance(check_dict, dict)
        res = True
        error_key = []
        for k in key_list:
            if k not in check_dict:
                error_key.append(k)
                res = False
        error_msg = 'key: <{}> of key_list: <{}> not in dict keys: <{}>'\
            .format(error_key, key_list, check_dict.keys())
        self.assertTrue(res, msg=error_msg)

    def base_response_check(self, response):
        """
        基本的返回检测
        :param response: 原始的返回
        """
        # 返回码200
        self.assertEqual(response.status_code, 200)
        # 对应的数据结果
        self.check_key_in_dict(self.base_response_key, response.json())
