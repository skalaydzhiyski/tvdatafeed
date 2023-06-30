#!/bin/bash
python3 setup.py sdist; pip3 install dist/tvdatafeed-2.0.0.tar.gz
ipython3 -i test.py
