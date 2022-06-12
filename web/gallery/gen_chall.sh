#!/bin/sh
[ -f gallery.zip ] && rm gallery.zip
zip -r gallery.zip app/
