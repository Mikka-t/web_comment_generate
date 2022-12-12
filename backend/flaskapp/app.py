from flask import Flask ,render_template, request, jsonify

import db
import markov

app = Flask(__name__)

# debug
@app.route('/')
def index():
    return "Flask is working!!!"

# debug
@app.route('/api', methods=['GET'])
def api():
    return "API is working!!!"

@app.route('/api/url', methods=['POST'])
def post_url():
    post_data = request.get_json()
    url = post_data["url"]
    db.insertURL(url)
    return url

@app.route('/api/generate', methods=['GET'])
def get_message():
    url = request.args.get('url')
    comments = markov.generate(url)
    messages = dict(zip( range(len(comments)), comments ))
    return jsonify(messages)


if __name__=="__main__":
    # app.debug = True 
    app.run(host='0.0.0.0', debug=True)