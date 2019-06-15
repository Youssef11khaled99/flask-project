from flask import Flask, redirect, url_for, request, render_template, request
import requests

app = Flask(__name__)


@app.route('/task',methods = ['POST'])
def task():
   if request.method == 'POST':
      target = request.form['target']
      array_size = request.form['array_size']
      numbers = request.form['numbers']
      if target == '' or array_size == '' or numbers == '' :
        return "Please fill all input fields!!"
      r = requests.post('https://gp-task-algorithm.herokuapp.com/', data={"n":6, "t":2, "i":[1,2,3]} )
      json_object = r.text
      return json_object




if __name__ == '__main__':
   app.run(debug = True)
