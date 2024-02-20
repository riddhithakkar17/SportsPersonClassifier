from flask import Flask, request, jsonify, render_template, send_from_directory
import util
import os


template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'SportsPersonClassifier')
template_dir = os.path.join(template_dir, 'UI')

app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)



@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    if request.method == 'GET':
        return render_template('app.html')
    
    elif request.method == 'POST':
        image_data = request.form['image_data']

        response = jsonify(util.classify_image(image_data))

        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    

@app.route('/<path:filename>')
def custom_static(filename):
    print("dssfddfs")
    return send_from_directory(template_dir, filename, as_attachment=True)

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)