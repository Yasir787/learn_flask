from flask import Flask


app = Flask(__name__) 
@app.route('/user/<username>') 
def home(username): 
    return f"hello world {username}!"

if __name__ == '__main__':
    app.run(debug=True)