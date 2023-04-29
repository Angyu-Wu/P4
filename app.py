from flask import Flask, request, jsonify
import joblib
import pickle
import pandas as pd
app = Flask(__name__)

#def model(vol_moving_avg,adj_close_rolling_med):
 #   directory = rf'C:\Users\Wu\Desktop\book\stock dataset'
  #  filename = directory+r'\finalized_model.sav'
    #loaded_model = pickle.load(open(filename, 'rb'))
    #d = [{'vol_moving_avg': vol_moving_avg, 'adj_close_rolling_med': adj_close_rolling_med}]
    #d = [{'vol_moving_avg': 1000, 'adj_close_rolling_med': 100}]
    #X = pd.DataFrame(data=d)
    #y_predicted = loaded_model.predict(X)
    #return str(y_predicted[0])
directory = rf'C:\Users\Wu\Desktop\book\stock dataset'
filename = directory+r'\finalized_model.sav'
loaded_model = joblib.load(open(filename, 'rb'))

@app.route('/predict', methods=['GET'])
def respond():
    # Retrieve the name from the url parameter /getmsg/?name=
    vol_moving_avg = request.args.get("vol_moving_avg",None)
    adj_close_rolling_med = request.args.get("adj_close_rolling_med", None)
    #print(f"Received: {vol_moving_avg}")
    #print(f"Received: {adj_close_rolling_med}")
    # For debugging
    #print(f"Received: {name}")
    #directory = rf'C:\Users\Wu\Desktop\book\stock dataset'
    #filename = directory+r'\finalized_model.sav'
    #loaded_model = joblib.load(filename)
    #d = {'vol_moving_avg': [vol_moving_avg], 'adj_close_rolling_med': [adj_close_rolling_med]}
    d = [{'vol_moving_avg': vol_moving_avg, 'adj_close_rolling_med': adj_close_rolling_med}]
    #d = [{'vol_moving_avg': 1000, 'adj_close_rolling_med': 100}]
    X = pd.DataFrame(data=d)
    y_predicted = loaded_model.predict(X)
    result = f''+str(y_predicted[0])
    #vol_moving_avg = str(vol_moving_avg)
    #adj_close_rolling_med = str(adj_close_rolling_med)
    

    
    response = {}
    #response["Prediction"] = f''+str(y_predicted[0])
    response["Prediction"] = f'vol_moving_avg is  {vol_moving_avg} and adj_close_rolling_med {adj_close_rolling_med} then result is {result}'
    # Check if the user sent a name at all

    # Return the response in json format
    return jsonify(response)

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)