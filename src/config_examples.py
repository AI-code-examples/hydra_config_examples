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
import hydra
from omegaconf import DictConfig
from omegaconf import OmegaConf


@hydra.main(version_base=None, config_path='../conf', config_name='config')
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    pass


# ----------------------------------------------------------------------
# 小结
if __name__ == '__main__':
    main()