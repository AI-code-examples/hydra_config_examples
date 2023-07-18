#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
-----------------------------------------------
@Software   :   PyCharm
@Project    :   hydra_config_examples
@File       :   user_config
@Version    :   v0.1
@Time       :   2023/7/18 17:04
@License    :   (C)Copyright    2018-2023,  zYx.Tom
@Reference  :   
@Description:   
@Thought    :
"""
from dataclasses import dataclass

from omegaconf import MISSING


@dataclass
class UserConfig:  # 将共用字段抽取出来作为父类
    user: str = MISSING
    password: str = '123456'


@dataclass
class UserMySQL(UserConfig):
    user: str = 'mysql'
    disk: bool = True


@dataclass
class UserPostGreSQL(UserConfig):
    user: str = 'postgresql'
    mem: bool = True
