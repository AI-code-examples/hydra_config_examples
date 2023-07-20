#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
-----------------------------------------------
@Software   :   PyCharm
@Project    :   hydra_config_examples
@File       :   config_examples
@Version    :   v0.1
@Time       :   2023/6/27 11:05
@License    :   (C)Copyright    2018-2023,  zYx.Tom
@Reference  :   
@Description:   
@Thought    :
"""
import logging
import os

import hydra
from omegaconf import DictConfig
from omegaconf import OmegaConf


@hydra.main(version_base=None, config_path='../conf', config_name='config')
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    assert cfg.node.loompa == 10  # attribute style access
    assert cfg["node"]["loompa"] == 10  # dictionary style access

    assert cfg.node.zippity == 10  # Value interpolation
    assert isinstance(cfg.node.zippity, int)  # Value interpolation type
    assert cfg.node.do == "oompa 10"  # string interpolation

    # cfg.node.waldo  # raises an exception

    print(f"Current working directory : {os.getcwd()}")
    print(f"Orig working directory    : {hydra.utils.get_original_cwd()}")
    print(f"to_absolute_path('foo')   : {hydra.utils.to_absolute_path('foo')}")
    print(f"to_absolute_path('/foo')  : {hydra.utils.to_absolute_path('/foo')}")
    print()

    log.info("Info level message")
    log.debug("Debug level message")
    pass


# ----------------------------------------------------------------------
# 小结
if __name__ == '__main__':
    log = logging.getLogger(__name__)
    main()
