#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
-----------------------------------------------
@Software   :   PyCharm
@Project    :   hydra_config_examples
@File       :   config_dataclass
@Version    :   v0.1
@Time       :   2023/6/27 14:10
@License    :   (C)Copyright    2018-2023,  zYx.Tom
@Reference  :   
@Description:   
@Thought    :
"""
import hydra
from omegaconf import DictConfig, OmegaConf
from dataclasses import dataclass
from hydra.core.config_store import ConfigStore


@dataclass
class MySQLConfig:
    driver: str = 'mysql'
    user: str = 'mysql_user'
    password: str = '223456'
    timeout: int = 20
    host: str = 'localhost'
    port: int = 3306


@dataclass
class PostgresSQLConfig:
    driver: str = "postgresql"
    user: str = "jieru"
    password: str = "secret"
    timeout: int = 20


cs = ConfigStore.instance()

# 直接使用类型
cs.store(name="config1", node=MySQLConfig)
# Using an instance, overriding some default values
cs.store(name="config2", node=MySQLConfig(host="test.db", port=3307))
# Using a dictionary, forfeiting runtime type safety
cs.store(name="config3", node={"host": "localhost", "port": 3308})


@hydra.main(version_base=None, config_name="config1")
def main_config1(cfg: DictConfig) -> None:
    print('main_config1--->')
    print(OmegaConf.to_yaml(cfg))
    pass


@hydra.main(version_base=None, config_name="config2")
def main_config2(cfg: DictConfig) -> None:
    print('main_config2--->')
    print(OmegaConf.to_yaml(cfg))
    pass


@hydra.main(version_base=None, config_name="config3")
def main_config3(cfg: DictConfig) -> None:
    print('main_config3--->')
    print(OmegaConf.to_yaml(cfg))
    pass


# ----------------------------------------------------------------------
# 小结
if __name__ == '__main__':
    main_config1()
    main_config2()
    main_config3()
