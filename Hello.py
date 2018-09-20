import socket
from flask import Flask, redirect, url_for, request, render_template
from ec2bot import get_best_lines

app = Flask(__name__)

"""
@app.route("/hello/<name>")
def hello(name):
    return "Hello World! %s" % name
"""

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

@app.route('/chat/<response>')
@app.route('/chat')
def chat(response = None):
    if(not response):
        return render_template('chat.html', Answer_list = None)
    lines = get_best_lines(response)
    return render_template('chat.html', Answer_list = lines)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/answer',methods = ['POST', 'GET'])
def answer():
   if request.method == 'POST':
      question = request.form['question']
      return redirect(url_for('chat',response = question,_external=True,_scheme="https"))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user,_external=True,_scheme="https"))


if __name__ =="__main__":
    print("hostname is " + socket.gethostname())
    app.run(host='0.0.0.0', port=8080, debug=True)
    






