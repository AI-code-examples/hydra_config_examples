#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
-----------------------------------------------
@Software   :   PyCharm
@Project    :   hydra_config_examples
@File       :   db_config
@Version    :   v0.1
@Time       :   2023/6/27 15:39
@License    :   (C)Copyright    2018-2023,  zYx.Tom
@Reference  :   
@Description:   
@Thought    :
"""
from dataclasses import dataclass

from omegaconf import MISSING

from config.user_config import UserConfig
from config.user_config import UserMySQL
from config.user_config import UserPostGreSQL


@dataclass
class DBConfig:  # 将共用字段抽取出来作为父类
    driver: str = MISSING  # 没有默认值的要排在前面，MISSING与???等价
    port: int = MISSING
    user_config: UserConfig = MISSING
    host: str = 'localhost'
    timeout: int = 20


@dataclass
class MySQLConfig(DBConfig):
    driver: str = "mysql"
    port: int = 3306
    user_config: UserMySQL = UserMySQL


@dataclass
class PostGreSQLConfig(DBConfig):
    driver: str = "postgresql"
    port: int = 5432
    user_config: UserPostGreSQL = UserPostGreSQL
    timeout: int = 10
