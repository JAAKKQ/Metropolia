from flask import Flask, jsonify

app = Flask(__name__)

def alkuluku(luku):
    on_alku_luku = True

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            on_alku_luku = False

    return on_alku_luku

@app.route('/alkuluku/<int:n>', methods=['GET'])
def tarkista(n):
    return jsonify({"Number": n, "isPrime": alkuluku(n)})

app.run(debug=True, port=3000)