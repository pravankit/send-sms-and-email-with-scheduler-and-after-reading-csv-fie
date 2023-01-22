from flask import Flask
import logging
logging.basicConfig(filename='log.txt', level=logging.INFO)
logging.basicConfig(filename='error.txt', level=logging.ERROR)
app = Flask(__name__)
@app.route('/')
def my_logs():
  app.logger.info("Info log information")
  app.logger.error("Error log info")
  return "testing logging levels."

if __name__ =="__main__":
    app.run(debug=True)
