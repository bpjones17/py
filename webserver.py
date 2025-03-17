from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')  # The "main" page of the website. The root.
def home():
  return "Webserver OK, Discord Bot OK"


def run():
  app.run(host="0.0.0.0", port=0, debug=False
          )  # Use port 0 to let Flask automatically pick an available port


def keep_alive():
  t = Thread(
      target=run
  )  # We use threading so the function doesn't block the discord client from running.
  t.start()
