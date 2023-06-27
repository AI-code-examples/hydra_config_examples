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
from dataclasses import dataclass
from dataclasses import field

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig
from omegaconf import OmegaConf

from config.db_config import MySQLConfig
from config.ui_config import UserInterface


@dataclass
class MyConfig:
    db: MySQLConfig = field(default_factory=MySQLConfig)
    ui: UserInterface = field(default_factory=UserInterface)


cs = ConfigStore.instance()

# 使用类
cs.store(name="config1", node=MySQLConfig)
# 初始化为实例，覆盖某些默认值
cs.store(name="config2", node=MySQLConfig(host="test.db", port=3307))
# 使用字典，推动运行期类型安全
cs.store(name="config3", node={"host": "localhost", "port": 3308})
# 使用层次化静态配置
cs.store(name="my_config", node=MyConfig)


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


@hydra.main(version_base=None, config_name="config1")
def main_mysql_config(cfg: MySQLConfig) -> None:
    """不再使用通用类 DictConfig 来定义 cfg

    :param cfg: 容许类的属性静态检查
    :return:
    """
    print('main_mysql_config--->')
    print(OmegaConf.to_yaml(cfg))
    pass


@hydra.main(version_base=None, config_name="my_config")
def main_my_config(cfg: MyConfig) -> None:
    print('main_my_config--->')
    print(OmegaConf.to_yaml(cfg))
    print(f"标题={cfg.ui.title}, 尺寸={cfg.ui.width}x{cfg.ui.height} 像素")
    pass


# ----------------------------------------------------------------------
# 小结
if __name__ == '__main__':
    main_config1()
    main_config2()
    main_config3()
    main_mysql_config()
    main_my_config()
