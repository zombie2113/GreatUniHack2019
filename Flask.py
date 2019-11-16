from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import json 
app = Flask(__name__, static_url_path='')



@app.route('/')
def hello_world():
   return app.send_static_file("index.html")

@app.route('/api')
def hello_worlds():
   urls = [("Hungry boi, invest now frens", "https://i.redd.it/uvenlxagz1z31.jpg"),
            ("Rick and Morty formats are always great choice. Stop asking questions and invest in this format!","https://i.redd.it/7rora8l032z31.jpg"),
            ("Do it! Invest in the most important super hero of all time. So you always can bury good corpses..","https://i.redd.it/vv5arx2bw0z31.jpg"),
            ("Fresh template, invest right now!","https://i.redd.it/2pd4lwd511z31.jpg")]
   vals = np.random.choice(data.url.shape[0], 4)
   urls = list(data.url[vals])
   return jsonify(urls)

if __name__ == '__main__':
   data = pd.read_csv('export_simple.csv')
   app.run(debug=True)
