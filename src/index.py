from flask import Flask, render_template

# objeto app 
app = Flask (__name__)

#creamos rutas 
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")
#hacer que la app se mantega escuchando
if __name__ == "__main__":
    app.run(debug=True) # para que se actualice debug=True la pagina