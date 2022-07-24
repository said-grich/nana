from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def getIndexPage():  # put application's code here
    return render_template("index.html");

@app.route('/page/<index>')
def getPage(index):
    print(index)
    return render_template("page.html",variable=index);


if __name__ == '__main__':
    app.run()
