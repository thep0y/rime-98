#!/bin/bash

fatal() {
  echo -e "\033[31m fatal: \033[0m$1"
  exit 1
}

error() {
  echo -e "\033[31m error: \033[0m$1"
}

info() {
  echo -e "\033[32m info: \033[0m$1"
}

if [ $(uname) == 'Darwin' ]; then
  RIME_USER_DIR=$HOME/Library/Rime
  THEME=$SCRIPT_DIR/themes/squirrel.custom.yaml
elif [ $(expr substr $(uname -s) 1 5) == 'Linux' ]; then
  RIME_USER_DIR=$HOME/.config/fcitx5
  # TODO: 克隆 fcitx5 皮肤仓库到本地后再处理
else
  fatal '不支持此平台'
fi

if [ ! -d $RIME_USER_DIR ]; then
  fatal '未找到 rime 目录，请检查鼠须管是否已安装'
fi

rm -rf $RIME_USER_DIR/*

SCRIPT_DIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)

cp $SCRIPT_DIR/dist/* $RIME_USER_DIR 

if [ $THEME ]; then
  cp $THEME $RIME_USER_DIR
fi

info '词库已安装，手动重新部署词库后即可生效'
