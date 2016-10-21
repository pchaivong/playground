from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import abort

from sklearn.externals import joblib


app = Flask(__name__)
api = Api(app)
clf = joblib.load('/data/iris-svm.pkl')
parser = reqparse.RequestParser()
parser.add_argument('features', type=list, location='json')


class IrisSVM(Resource):

        def post(self):
                args = parser.parse_args()
                features = args['features']
                if len(features) != 4:
                        abort(404)


                predict = clf.predict([features])[0]
                prob = clf.predict_proba([features])[0]
                prob = max(prob)*100
                app.logger.info('Predict : %d', (predict))
                app.logger.info('Probability : %.2f \%', (prob))

                return { 'result' : predict , 'probability': prob}

api.add_resource(IrisSVM, '/iris')

if __name__=='__main__':
        app.run(debug=True, host='0.0.0.0')