#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
-----------------------------------------------
@Software   :   PyCharm
@Project    :   hydra_config_examples
@File       :   config_dataclass_groups_defaults
@Version    :   v0.1
@Time       :   2023/6/27 15:38
@License    :   (C)Copyright    2018-2023,  zYx.Tom
@Reference  :   
@Description:   
@Thought    :
"""
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from omegaconf import OmegaConf

from config.db_config import MySQLConfig
from config.db_config import PostGreSQLConfig

defaults = [
    # 从配置组`db`中加载`postgresql`配置
    # {"db": MISSING},  # MISSING 会要求显示提供值
    {"db": 'postgresql'}
]


@dataclass
class Config:
    # this is unfortunately verbose due to @dataclass limitations
    defaults: List[Any] = field(default_factory=lambda: defaults)

    # Hydra will populate this field based on the defaults list
    db: Any = MISSING
    # debug: bool = True    # ToDo: debug examples for completion


cs = ConfigStore.instance()
cs.store(group="db", name="mysql", node=MySQLConfig)
cs.store(group="db", name="postgresql", node=PostGreSQLConfig)
cs.store(name="config_db", node=Config)


@hydra.main(version_base=None, config_name="config_db")
def main(cfg: Config) -> None:
    print(OmegaConf.to_yaml(cfg))
    pass


# ----------------------------------------------------------------------
# 小结
if __name__ == '__main__':
    main()
