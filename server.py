"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
INSULTS = [
  "jerk", "stupid", "trump"
]
LEVELS = ['high', 'medium', 'low']
@app.route("/")
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<a href='/hello'>Hello!</a></html>"


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    options = ""
    for compliment in AWESOMENESS:
      options += f"<option value='{compliment}'>{compliment}</option>"
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        
        Would you like to be <a href='/compliment'>complimented</a> or <a href='/diss'>insulted</a>?


      </body>
    </html>
    """.format(options)
# <option value = "awesome">awesome</option>
#           <option value = "terrific">terrific</option>
#           <option value = "fantastic">fantastic</option>
#           <option value = "neato">neato</option>
#           <option value = "fantabulous">fantabulous</option>
#           <option value = "wowza">wowza</option>
#           <option value = "oh-so-not-meh">oh-so-not-meh</option>
#           <option value = "brilliant">brilliant</option>
#           <option value = "ducky">ducky</option>
#           <option value = "coolio">incredible</option>
#           <option value = "wonderful">wonderful</option>
#           <option value = "smashing">smashing</option>
#           <option value = "lovely">lovely</option>
          

@app.route("/compliment")
def greet_person():
    """Get user by name."""


    #print(request.args)
    #player = request.args.get("person")

    #compliment = request.args.get("AWESOMENESS")

    #y = x
    level_options = ""
    for level in LEVELS:
      level_options += "<option value = '{}'> {}</option>".format(level,level)


    return """

    <!doctype html>
    <html>
      <head>
        <title>Compliment</title>
      </head>
      <body>
        Hi, ! I think you're !
        <form action="/complimentLevel">

          Choose your compliment level: <br>
          <br>
          <select name = "compliment_level">
            {}
          </select>
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(level_options)

@app.route("/complimentLevel")
def return_compliment():
  
  level = request.args.get('compliment_level')
  valid_options = ""
  html_options = ""
  
  if level == "high":
    valid_options = AWESOMENESS[0:4]
  elif level == "medium":  
    valid_options = AWESOMENESS[4:9]
  elif level == "low":  
    valid_options = AWESOMENESS[9:]
  
  for option in valid_options:
    html_options += "<option value='{}'> {}</option>".format(option,option)

  return """
    <form>
      <select>
      {}
      </select>
    </form>
  """.format(html_options)

@app.route("/diss")
def insult():
  """insult the user"""
  user_name = request.args.get("your_name")
  insult = choice(INSULTS)
  available_insults = " ".join(INSULTS)
  insults_as_headers = ""
  for insult in INSULTS:
    insults_as_headers += "<h3>{}</h3>".format(insult)


  return """
          <form action = "/diss">
          Enter your name:<br>
          <input type="text" name="your_name"><br>
          <input type="submit" value="Insult">
        </form>

    <h3>{}, you {}!!!</h3>
    <p> Available insults are: {} </p> 
    {}
  """.format(user_name,insult,available_insults,insults_as_headers)




if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
