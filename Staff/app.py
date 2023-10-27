from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def staff():
   return render_template('staff.html')

if __name__ == "__main__":
  app.run(debug = True)

