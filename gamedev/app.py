from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def main():
	return 'ok', 200


@app.route('/api/v1/games')
def games():
	return {'g1': 100, 'g2': 200, 'g3': 300, 'g4': 400}


if __name__ == '__main__':
	app.run(debug=True)
