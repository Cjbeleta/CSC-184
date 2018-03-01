from flask import Flask, request, jsonify

app = Flask(__name__)

anime = [{'title': 'Ao No Exorcist'},
		 {'title': 'Boku No Hero Academia'},
		 {'title': 'Code Geass'},
		 {'title': 'Danganronpa'},
		 {'title': 'Fairy Tail'},
		 {'title': 'HunterXHunter'}]

@app.route('/anime', methods = ['GET'])
def showall():
	return jsonify({'anime': anime})

@app.route('/anime', methods = ['POST'])
def addanime():
	ani = {'title': request.json['title']}
	
	anime.append(ani)
	return jsonify({'anime': anime})

@app.route('/anime/<string:title>', methods = ['PUT'])
def editanime(title):
	select = [ani for ani in anime if ani['title'] == title]
	select[0]['title'] = request.json['title']
	return jsonify({'anime': select[0]})

@app.route('/anime/<string:title>', methods = ['DELETE'])
def deleteanime(title):
	select = [ani for ani in anime if ani['title'] == title]
	anime.remove(select[0])
	return jsonify({'anime': anime})

if __name__ == '__main__':
	app.run(debug=True, port=5000)