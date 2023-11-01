#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6800899037:AAForVZUJLfD0LznPLTPD1yxwqzJUSr5ZIQ")
    API_ID = int(os.environ.get("API_ID", "29257953"))
    API_HASH = os.environ.get("API_HASH", "31dae8eac39b38583898e3bc78b96406")
    

