from flask import Flask, jsonify,request, render_template
from utils import Penguine
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/Penguine", methods=["GET", "POST"])
def penguin_prediction():
    try:
        if request.method == "POST":
            data = request.form
            bill_length_mm = data['bill_length_mm']
            bill_depth_mm = data['bill_depth_mm']
            flipper_length_mm = data['flipper_length_mm']
            body_mass_g = data['body_mass_g']
            species = data['species']
            island = data['island']

            obj = Penguine(bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, species, island)
            r = obj.Pred_Penguine()
        elif request.method == 'GET':
            data = request.args
            bill_length_mm = data.get('bill_length_mm')
            bill_depth_mm = data.get('bill_depth_mm')
            flipper_length_mm = data.get('flipper_length_mm')
            body_mass_g = data.get('body_mass_g')
            species = data.get('species')
            island = data.get('island')

            obj = Penguine(bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, species, island)
            r = obj.Pred_Penguine()

        return render_template("index.html", result=r)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUMBER, debug=False)
