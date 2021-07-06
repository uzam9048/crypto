from patterns.bullish_1hr import bullish_1hr
from patterns.bullish_15 import bullish_15m
from flask import Flask, render_template, url_for,request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from patterns.bullish_engulfing import bullish
from patterns.bearish_engulfing import bearish
from patterns.bullish_15 import bullish_15m
from patterns.bullish_30 import bullish_30m
from patterns.bullish_weekly import bullish_weekly
from patterns.bullish_1hr import bullish_1hr
from patterns.bearish_15 import bearish_15m
from patterns.bearish_30 import bearish_30m
from patterns.bearish_1hr import bearish_1hr
from patterns.bearish_weekly import bearish_1wk




app = Flask(__name__,template_folder= 'template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)




@app.route("/bullishengulfing")
def bullish_engulfing():
    bullish_engulfing = bullish.bullish_engulfing
    return render_template('view.html',tables=[bullish_engulfing.to_html(classes='BULLISH_ENGULFING')],
    titles = ['na','Bullish Engulfing Candlestick Pattern Screener on Daily TimeFrame'])




@app.route("/bullishengulfing/15m")
def bullish_fifteen():
    bullish_engulfing = bullish_15m.bullish_engulfing
    return render_template('view.html',tables=[bullish_engulfing.to_html(classes='BULLISH_ENGULFING')],
    titles = ['na','         BULLISH ENGULFING 15 Minutes Time Frame of Last 7 days'])

@app.route("/bullishengulfing/30m")
def bullish_thirty():
    bullish_engulfing = bullish_30m.bullish_engulfing
    return render_template('view.html',tables=[bullish_engulfing.to_html(classes='BULLISH_ENGULFING')],
    titles = ['na','BULLISH ENGULFING 30 Minutes Time Frame of Last 7 days'])    

@app.route("/bullishengulfing/1hr")
def bullish_hourly():
    bullish_engulfing = bullish_1hr.bullish_engulfing
    return render_template('view.html',tables=[bullish_engulfing.to_html(classes='BULLISH_ENGULFING')],
    titles = ['na','BULLISH ENGULFING Hourly Time Frame of Last 7 days'])   

@app.route("/bullishengulfing/1wk")
def bullish_weekly():
    bullish_engulfing = bullish_weekly.bullish_engulfing
    return render_template('view.html',tables=[bullish_engulfing.to_html(classes='BULLISH_ENGULFING')],
    titles = ['na','BULLISH ENGULFING Weekly Time Frame']) 

@app.route("/bearishengulfing")
def bearish_engulfing():
    bearish_engulfing = bearish.bearish_engulfing
    return render_template('view_bearish.html',tables=[bearish_engulfing.to_html(classes='BEARISH_ENGULFING')],
    titles = ['na','BEARISH ENGULFING Candlestick Pattern Screener on Daily TimeFrame'])       

@app.route("/bearishengulfing/15m")
def bearish_fifteen():
    bearish_engulfing = bearish_15m.bearish_engulfing
    return render_template('view_bearish.html',tables=[bearish_engulfing.to_html(classes='BEARISH_ENGULFING')],
    titles = ['na','BEARISH ENGULFING of 15 minutes TimeFrame of Last 7 days'])  

@app.route("/bearishengulfing/30m")
def bearish_Thirty():
    bearish_engulfing = bearish_30m.bearish_engulfing
    return render_template('view_bearish.html',tables=[bearish_engulfing.to_html(classes='BEARISH_ENGULFING')],
    titles = ['na','BEARISH ENGULFING  30 minutes TimeFrame of Last 7 days'])    



@app.route("/bearishengulfing/1hr")
def bearish_hourly():
    bearish_engulfing = bearish_1hr.bearish_engulfing
    return render_template('view_bearish.html',tables=[bearish_engulfing.to_html(classes='BEARISH_ENGULFING')],
    titles = ['na','BEARISH ENGULFING  1 hour TimeFrame of Last 7 days'])

@app.route("/bearishengulfing/1wk")
def bearish_weekly():
    bearish_engulfing = bearish_weekly.bearish_engulfing
    return render_template('view_bearish.html',tables=[bearish_engulfing.to_html(classes='BEARISH_ENGULFING')],
    titles = ['na','BEARISH ENGULFING  weekly TimeFrame'])    



@app.route('/')
def bullish_home():
    bullish_engulfing = bullish.bullish_engulfing
    return render_template('view.html',tables=[bullish_engulfing.to_html(classes='BULLISH_ENGULFING')],
    titles = ['na','Bullish Engulfing Candlestick Pattern Screener on Daily Tick'])


@app.route('/home',methods=["GET","POST"])
def home_page():
    return render_template('home.html')   

    




if __name__ == "__main__":
    app.run(debug=True)    



  