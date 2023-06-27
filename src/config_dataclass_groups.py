#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
-----------------------------------------------
@Software   :   PyCharm
@Project    :   hydra_config_examples
@File       :   config_dataclass_groups
@Version    :   v0.1
@Time       :   2023/6/27 15:06
@License    :   (C)Copyright    2018-2023,  zYx.Tom
@Reference  :   
@Description:   
@Thought    :
"""
from dataclasses import dataclass
from typing import Any

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf

from config.db_config import MySQLConfig
from config.db_config import PostGreSQLConfig


@dataclass
class Config:  # `db`的参数运行时添加
    db: Any


# Create config group `db` with options 'mysql' and 'postgreqsl'
cs = ConfigStore.instance()
cs.store(name="config_db", node=Config)
cs.store(group="db", name="mysql", node=MySQLConfig)
cs.store(group="db", name="postgresql", node=PostGreSQLConfig)


@hydra.main(version_base=None, config_name="config_db")
def main(cfg: Config) -> None:
    """

    运行方式需要添加 `+db=`，因为`db`没有默认值
    `python src/config_dataclass_groups.py +db=mysql`

    :param cfg:
    :return:
    """
    print(OmegaConf.to_yaml(cfg))
    pass


# ----------------------------------------------------------------------
# 小结
if __name__ == '__main__':
    main()
