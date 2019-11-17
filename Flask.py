from flask import Flask, render_template, jsonify, request, current_app
import pandas as pd
import numpy as np
import json 
app = Flask(__name__, static_url_path='')



@app.route('/')
def hello_world():
   return app.send_static_file("index.html")

@app.route('/api/post')
def get_post():
   # Add feature to get info from specific post
   pass
   

@app.route('/api')
def hello_worlds():
   
   vals = np.random.choice(data.url.shape[0], 4)
   ids = list(data.id[vals])
   urls = list(data.url[vals])
   scores = list(data.score[vals])
   #scores = [str(score) for score in scores]
   return jsonify(list(zip(ids, urls, scores)))

@app.route('/api/vote', methods=['POST'])
def vote():
   id_photo = str(request.form['id'])
   app.state.data.loc[app.state.data.id == id_photo, ['score']] += 1
   print("Now:")
   print(app.state.data[app.state.data.id == id_photo])
   return "Success"
   

class State():
   def __init__(self, data, name):
      self.name = name
      self.data = data
   

if __name__ == '__main__':
   data = pd.read_csv('export_simple.csv')
   data['score'] = 0
   app_state = State(data, "Meme recommender")
   app.state = app_state
   app.run(debug=True)
