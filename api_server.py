import json
import os
import uuid
import random
from datetime import datetime

from flask import Flask, Response, request, send_file, abort

app = Flask('DIRECTOR')

#create upload folder if not exists
storageDir = "storage"
if not os.path.exists(storageDir):
    os.mkdir(storageDir)

app = Flask('FileService')

@app.route('/')
def index():
    return "Server is running"

@app.route('/get_id/', methods=["GET"])
def get_id():
    id = str(uuid.uuid4())
    os.mkdir(os.path.join(storageDir, id))

    data = {
        'id': id
    }

    return Response(json.dumps(data), mimetype='application/json')

@app.route('/submit/<string:id>', methods=["POST"])
def submit(id):
    if not os.path.exists(os.path.join(storageDir, id)):
        abort(404)

    #generate filename
    filename = datetime.now().strftime('%Y%m%d %H%M%S%f') + '.json'

    #store json in folder, using id
    json_data = request.get_json(force=True)
    with open(os.path.join(storageDir, id, filename), 'w') as f:
        json.dump(json_data, f)

    #give response object
    data = {
        'status': "success",
        'id': id
    }
    return Response(json.dumps(data), mimetype="application/json")


@app.route('/score/<string:id>')
def get_score(id):
    if not os.path.exists(os.path.join(storageDir, id)):
        abort(404)
        
    # generate nicely distributed scores for each of the 5 indicators
    scores = [random.gauss(2.5, 1.25) for _ in range(5)]
    scores = [i if i >= 0 and i <= 5 else 5 for i in scores]

    # set up categories and numbered indicators for each category
    categories = ['innovation', 'capabilities', 'strategy', 'hrm', 'organization']
    indicators = [f'indicator{i}' for i in range(5)]
    indicator_dicts = [dict(zip(indicators, random.sample(scores, k=len(scores)))) for category in categories]

    data = {
        'id': id,
        'scores': dict([(categories[i], {'overall': scores[i], 'indicators': indicator_dicts[i]}) for i in range(5)])
    }

    return Response(json.dumps(data), mimetype='application/json')

app.run(debug=True, host='0.0.0.0', port=5001)
