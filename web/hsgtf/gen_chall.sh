#!/bin/sh
[ -f hsgtf.zip ] && rm hsgtf.zip
zip -r hsgtf.zip app/ requirements.txt
