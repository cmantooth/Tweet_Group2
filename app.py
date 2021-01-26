from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html',my_arg='The cats are getting along now!')

    # if request has args (?tweet=some_tweet)
    if request.args:

        # get the value of the arg
        tweet = request.args.get('tweet')   
        
        return tweet

    return 'Hello World!'

@app.route('/about')
def about():

    about_text = """
    Having a hard time reading the subtext of tweets? Worry no more! Mantooth Labs has brought you a way to analyze Twitter emotions in the blink of an eye.
    """
    return about_text

if __name__=='__main__':

    app.run(debug=True)
    
    