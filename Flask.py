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
   urls = [("Hungry boi, invest now frens", "https://i.redd.it/uvenlxagz1z31.jpg"),
            ("Rick and Morty formats are always great choice. Stop asking questions and invest in this format!","https://i.redd.it/7rora8l032z31.jpg"),
            ("Do it! Invest in the most important super hero of all time. So you always can bury good corpses..","https://i.redd.it/vv5arx2bw0z31.jpg"),
            ("Fresh template, invest right now!","https://i.redd.it/2pd4lwd511z31.jpg"), ("Fresh template, invest right now!", "https://i.redd.it/2pd4lwd511z31.jpg")
            , ("Invest in brand new meme template","https://i.redd.it/l8h48opu42z31.jpg"),("Fresh Trump template, invest now!","https://i.redd.it/7xaj1pigg2z31.jpg"),
            ("Veyr cash money","https://i.redd.it/binbz7w7u0z31.jpg"),("Invest in the broken dam","https://i.redd.it/u50ecmr04yy31.jpg"),
            ("You gotta love Keanu Reeves formats!", "Invest in this new meme format!,https://i.redd.it/"),("Invest in my dad and brother","https://i.redd.it/3fa0vk33jwy31.jpg"),
            ("Invest today!","https://i.redd.it/wi5b15u1m2z31.jpg"),("Dope or Nope meme format! Invest now!","https://i.redd.it/d29veri8l0z31.jpg"),
            ("Invest before becoming a victim to the next emergency,https://i.redd.it/b9dz1hulsxy31.jpg")]

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
