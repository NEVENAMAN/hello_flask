from flask import Flask , render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# ------------------------------------------------------------------------------------------------------------

# localhost:5000/ - have it say "Hello World!"
@app.route('/hello_world')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
    
# -------------------------------------
@app.route('/<phrase>/<times>')
def repeat(phrase,times):
    return render_template("index.html", phrase=phrase, times=int(times))

# -------------------------------------
# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# -------------------------------------
# localhost:5000/say/flask - have it say "Hi Flask!"
@app.route('/say/<name>')
def say(name):
    return 'Hi '+ name
 
    
# ------------------------------------------------------------------------------------------------------------
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

