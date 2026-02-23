import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

filepath = "data_small/stations.txt"
all_available_stations = pd.read_csv(filepath, skiprows=17)
all_available_stations = all_available_stations[['STAID','STANAME                                 ']]
@app.route("/")
def home():
    return render_template("index.html",
                           station_data=all_available_stations.to_html())

@app.route("/api/v1/<station_id>/<date>")
def date_wise(station_id, date):
    filepath = "data_small/TG_STAID" + str(station_id).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    description_dictionary = {"station_id": station_id,
                   "date": date,
                   "temperature": temperature}
    return description_dictionary

@app.route("/api/v1/yearly/<station_id>/<year>")
def yearly(station_id, year):
    filepath = "data_small/TG_STAID" + str(station_id).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(year)].to_dict(orient="records")
    return result

@app.route("/api/v1/<station_id>")
def all_data(station_id):
    filepath = "data_small/TG_STAID" + str(station_id).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result

if __name__=="__main__":
    app.run(debug=True, port=5001)