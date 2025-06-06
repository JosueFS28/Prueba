from flask import Flask
app=Flask(__name__)
@app.route("/")
def hmain():
    return "<h1> Prueba realizada con exito <h1>"

