from flask import Flask, render_template, request
from compare_sen import compareSen
from io import BytesIO, open
import base64
import csv
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/compare', methods=['POST'])
def compare():
	ch1, ch2 = map(int, (request.form["chapter1"], request.form["chapter2"]))
	img = BytesIO()

	senti = []
	breaks = [(0, 175), (176, 361), (362, 537), (538, 853), (854, 1144), (1145, 1618), (1619, 2479)]

	with open('static/glass_data.tsv', "r", encoding='utf-8', errors='ignore') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='\t')
		for row in reader:
			senti.append(float(row['movingave']))

	sentiment = np.array(senti)
	frame = plt.gca()

	line1 = plt.plot(sentiment[breaks[ch1-1][0]:breaks[ch1-1][1]], color = "Green")
	line2 = plt.plot(sentiment[breaks[ch2-1][0]:breaks[ch2-1][1]], color = "Yellow")

	frame.axes.get_xaxis().set_ticks([])
	plt.title("Sentiment over Chapters in The Glass Menagerie")
	plt.ylabel("Sentiment Rating")

	plt.savefig(img, format='png')
	img.seek(0)
	coded_img = img.getvalue()
	img.close()

	plot_url = base64.b64encode(coded_img).decode()
	return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == "__main__":
	app.run(debug=True)