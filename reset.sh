#!/usr/bin/env bash

rm -rf viper.db
#python3 tabledef.py
sqlite3 viper.db < create.sql