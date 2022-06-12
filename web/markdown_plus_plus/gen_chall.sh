#!/bin/sh
[ -f md++.zip ] && rm md++.zip
zip -r md++.zip app/ requirements.txt
