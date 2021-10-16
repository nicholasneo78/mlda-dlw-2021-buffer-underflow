from flask import Flask, jsonify
import random

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def plant_environment():

    diseases = ['Pepper bell bacterial spot', 'Potato early blight', 'Potato late blight']

    result = {
        'disease_classifier':
            {
                "heathly":False, "disease": random.choice(diseases)
            },
        'recommend_plant':
            {
                'apple': '0.0000000222',
                'banana': '0.0000030293',
                'blackgram': '0.0000006398',
                'chickpea': '0.0000000000',
                'coconut': '0.0000411466',
                'coffee': '0.0000000072',
                'cotton': '0.0042584073',
                'grapes': '0.0000000000',
                'jute': '0.0000617717',
                'kidneybeans': '0.0000000000',
                'lentil': '0.0000033268',
                'maize': '0.0001482871',
                'mango': '0.0000000002',
                'mothbeans': '0.0000094367',
                'mungbean': '0.0045491722',
                'muskmelon': '0.0543002971',
                'orange': '0.0181059018',
                'papaya': '0.0033644827',
                'pigeonpeas': '0.0000000000',
                'pomegranate': '0.0056215208',
                'rice': '0.0000060801',
                'watermelon': '0.9095264673'
            }
    }
    
    resp = jsonify(result)
    resp.status_code = 200
    print(resp)

    return resp

if __name__ == '__main__':
    app.run()