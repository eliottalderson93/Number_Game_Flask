from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes

# Routing rules and rest of server.py below
# our index route will handle rendering our form

@app.route('/')
def index():
    if 'initial' in session:
        session['initial'] = False
        #print(session)
    else:
        session['initial'] = True #initialize
        session['random'] = random.randrange(0,101)
        session['high'] = False
        session['low'] = False
        session['correct'] = False
        session['guess'] = -57
        print(session)
    if session['initial'] == False:
        if session['guess'] == -57:
            pass #it was a reload, no submit
        elif session['random'] < session['guess']:
            session['high'] = True
            #pass #high
        elif session['random'] > session['guess']:
            session['low'] = True
            #pass #low
        else:
            session['correct'] = True
            #pass #correct
    else:
        pass
    return render_template("code.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/guess', methods=['POST'])
def high():
    print(request.form['guess'])
    #session['guess'] = request.form['guess']
    return redirect('/')  # Notice that we changed where we redirect to
                              # Now we go to the page that displays the name and email!

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    # run our server
    app.run(debug=True)