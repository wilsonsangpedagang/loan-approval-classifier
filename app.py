from flask import Flask, render_template, request, redirect, url_for
from views import views

app = Flask(__name__) # Initialize flask
app.register_blueprint(views) # Register the views blueprint

if __name__ == '__main__':
    app.run(debug=True, port=5000) # run the web in port 5000