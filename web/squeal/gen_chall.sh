#!/bin/sh
[ -f squeal.zip ] && rm squeal.zip
zip -r squeal.zip public/ package.json index.js
