from flask import Flask, render_template, session, request, redirect, url_for
#deal with other imports later like db or sql
#possibly use react/next.js to make website look better

app = Flask(__name__)
app.secret_key = "temp" #possibly don't need a login for this since I won't run this on a server anyway

@app.route("/")
def landing_page():
    return render_template("landing.html")

@app.route("/login")
def login_page():
    return "under construction"

@app.route("/register")
def register_page():
    return "still under construction"

@app.route("/home")
def home_page():
    return "home page with post recommendations maybe"

@app.route("/user/<int:UserID>")
def user_page(UserID):
    #get information about user's id?
    #or maybe make 2 profile pages:
    #one that the user logged in can edit
    #one that other people see
    if UserID == 1:
        return "test userid page"
    else:
        return "access denied"
    
@app.route("/user/<int:UserID>/<string:userPostID>")
def user_posts(UserID, userPostID):
    #idk what userid is used for right here
    return userPostID

@app.route("/community/<string:communityName>")
def community(communityName):
    if communityName == "subreddit":
        return "you're in the right place"
    else:
        return "go away"
    
@app.route("/community/<string:communityName>/<string:communityPostID>")
def community_posts(communityName, communityPostID):
    return communityPostID

if __name__ == "__main__":
    app.debug = True
    app.run()