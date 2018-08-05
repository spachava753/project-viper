from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from quote_provider import get_all_quotes
import datetime
import random
import hashlib


