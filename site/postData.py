import requests
import random
import numpy as np
import pandas as pd


from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/sendData')
def sendData():
    data_csv={"data":request.args.get('fileName')}
    response=requests.post('http://127.0.0.1:5000/', json=data_csv)
    time.sleep(1000000)