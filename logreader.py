from flask import Flask
# from flask_restful import Api, Resource

app = Flask(__name__)
# api = Api(app)

@app.route('/')
def logreader():
        a = open("The log file location")
        b = a.read().splitlines()
        return b[-1]
    
if __name__ == "__main__":
#     app.run()
    app.run(host='the Syslog server IP addr', port='5000')
