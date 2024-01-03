#!/usr/bin/env bash
cp ./reversi/script/web/index.html ../fucusy.github.io/docs/
sed -i '' -e 's/\"\/\"/"http:\/\/81.70.152.141:8080"/g' ../fucusy.github.io/docs/gomoku.html

