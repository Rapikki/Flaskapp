from flask import Flask, render_template
from flask import Response

app = Flask(__name__)


@app.route('/health')
def health():
    return Response(status = 200)
	
@app.route('/hello')
def hello():
    return Response("Hello world", status=200, mimetype='application/json')
	

@app.route("/")
def main():
   return render_template('index.html')
if __name__ == "__main__":
    app.run()
	