#!/usr/bin/env bash

rm -rf viper.db
echo 'removed viper.db'
python3 tabledef.py
echo 'created viper.db'
sqlite3 viper.db < create.sql
echo 'finished viper.db'
sqlite3 viper.db "select * from users;"
sqlite3 viper.db "select * from watchlists;"
sqlite3 viper.db "select * from watchlist_items;"
sqlite3 viper.db "select * from symbols;"