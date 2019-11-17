from flask import Flask, render_template, jsonify, request, current_app
import pandas as pd
import numpy as np
import json 
app = Flask(__name__, static_url_path='')



@app.route('/')
def hello_world():
   return app.send_static_file("index.html")

@app.route('/login')
def login_page():
   return app.send_static_file("login.html")

@app.route('/api/post')
def get_post():
   # Add feature to get info from specific post
   pass
   

@app.route('/api')
def return_4_post():
   vals = np.random.choice(data.url.shape[0], 4)
   name = list(data.title[vals])
   link = list(data.permalink[vals])
   ids = list(data.id[vals])
   urls = list(data.url[vals])
   scores = list(data.score[vals])
   
   #scores = [str(score) for score in scores]
   return jsonify(list(zip(ids, urls, scores, name, link)))

@app.route('/api/single')
def return_single_post():
   vals = np.random.choice(data.url.shape[0], 1)
   name = list(data.title[vals])
   link = list(data.permalink[vals])
   ids = list(data.id[vals])
   urls = list(data.url[vals])
   scores = list(data.score[vals])
   #scores = [str(score) for score in scores]
   return jsonify(list(zip(ids, urls, scores, title, permalink)))

@app.route('/api/vote', methods=['POST'])
def vote():
   id_photo = str(request.form['id'])
   app.state.data.loc[app.state.data.id == id_photo, ['score']] += 1
   print(app.state.data[app.state.data.id == id_photo])
   return "Success"
   

class State():
   def __init__(self, data, name):
      self.name = name
      self.data = data
   
def clean_data(data):
   data = data[data['url'].str.contains("redd.it")]

   print("Now data has got -> " + str(data.shape))

if __name__ == '__main__':
   data = pd.read_csv('export_simple.csv')
   
   print("Now data has got -> " + str(data.shape))

   data['score'] = 0
   app_state = State(data, "Meme recommender")
   app.state = app_state
   app.run(debug=True)
