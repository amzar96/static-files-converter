from flask import Flask, jsonify, abort, request, make_response, url_for, render_template, redirect, flash
import json

app = Flask(__name__)


@app.route('/')
def index():
    output="Please Enter path"
    path = "none"
    return render_template('form.html', output=output, path=path)


@app.route('/convert', methods=['POST'])
def convert():
    #path = request.form.get('path')
    #folder = request.form.get('folder')


    path =  request.form['path']
    folder =  request.form['folder']

    path2 = ("{}/{}".format(folder,path))
    newpath =  "{{ url_for('static', filename='"+path2+"') }}"

    return json.dumps({'status':'OK','path':path,'newpath':newpath})


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5050, debug=True)
    #app.run(host="0.0.0.0", port=constants.API_PORT, debug=True)

