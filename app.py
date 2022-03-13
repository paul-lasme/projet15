from flask import Flask
import os
my_port = int(os.environ.get("PORT", 8030))
app = Flask(__name__)
visit_cnt=0
@app.route('/')
def hello_world():
    global visit_cnt
    visit_cnt+=1
    return "444"
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=my_port)