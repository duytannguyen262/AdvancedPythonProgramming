from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    ketqua = "<h1> Xin chào </h1>"
    return (ketqua)




if __name__ == '__main__':
    app.run(port=5050)