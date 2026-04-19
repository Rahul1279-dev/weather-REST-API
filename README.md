# 🌤️ European Weather Data REST API

A lightweight REST API built with **Flask** and **Pandas** that serves historical daily temperature data for European weather stations. The data is sourced from the [European Climate Assessment & Dataset (ECA&D)](https://www.ecad.eu).

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Data Source](#data-source)
- [Technologies Used](#technologies-used)

---

## Overview

This project exposes historical surface air temperature records from 100+ European weather stations via a simple REST API. Users can query temperature data for a specific date, an entire year, or the full historical record for any station.

A home page lists all available weather stations alongside their Station IDs, making it easy to find the right station before querying the API.

---

## Features

- 🏠 **Home page** listing all available weather stations with their IDs
- 📅 **Date-wise query** — get the temperature for a specific station on a specific date
- 📆 **Yearly query** — retrieve all daily temperature records for a given year
- 📊 **Full history query** — fetch the complete historical dataset for any station
- ⚡ Fast and lightweight — pure Flask with no database required

---

## Project Structure

```
rest_api/
├── main.py                          # Flask application & API routes
├── templates/
│   └── index.html                   # Home page template
└── data_small/
    ├── stations.txt                 # Station metadata (ID, name, location)
    ├── TG_STAID000001.txt           # Temperature data — Station 1
    ├── TG_STAID000002.txt           # Temperature data — Station 2
    └── ...                          # (100 station files total)
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/rest-api-weather.git
   cd rest-api-weather
   ```

2. **Install dependencies**
   ```bash
   pip install flask pandas
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Open in your browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## API Endpoints

### `GET /`
Home page — displays all available weather stations and their IDs in a table.

---

### `GET /api/v1/<station_id>/<date>`
Returns the temperature for a specific station on a specific date.

| Parameter    | Type   | Format       | Example      |
|--------------|--------|--------------|--------------|
| `station_id` | int    | numeric ID   | `10`         |
| `date`       | string | `YYYY-MM-DD` | `1988-10-25` |

**Example Request:**
```
GET /api/v1/10/1988-10-25
```

**Example Response:**
```json
{
  "date": "1988-10-25",
  "station_id": "10",
  "temperature": -0.9
}
```

---

### `GET /api/v1/yearly/<station_id>/<year>`
Returns all daily temperature records for a station in a given year.

| Parameter    | Type   | Format     | Example |
|--------------|--------|------------|---------|
| `station_id` | int    | numeric ID | `10`    |
| `year`       | string | `YYYY`     | `1988`  |

**Example Request:**
```
GET /api/v1/yearly/10/1988
```

**Example Response:**
```json
[
  { "DATE": "19880101", "TG": 37, "Q_TG": 0, "SQUID": 36122, "STAID": 10 },
  { "DATE": "19880102", "TG": 43, "Q_TG": 0, "SQUID": 36122, "STAID": 10 },
  ...
]
```

> **Note:** Temperature values (`TG`) are stored as integers in tenths of degrees Celsius. The date-wise endpoint automatically divides by 10 to return the actual °C value.

---

### `GET /api/v1/<station_id>`
Returns the complete historical temperature dataset for a station.

| Parameter    | Type | Format     | Example |
|--------------|------|------------|---------|
| `station_id` | int  | numeric ID | `10`    |

**Example Request:**
```
GET /api/v1/10
```

---

## Data Source

Data is provided by the **European Climate Assessment & Dataset (ECA&D)** project.

> Klein Tank, A.M.G. and Coauthors, 2002. *Daily dataset of 20th-century surface air temperature and precipitation series for the European Climate Assessment.* Int. J. of Climatol., 22, 1441–1453.

Data and metadata available at [https://www.ecad.eu](https://www.ecad.eu)

The `stations.txt` file contains station metadata including:
- **STAID** — Station identifier
- **STANAME** — Station name
- **CN** — Country code (ISO 3116)
- **LAT / LON** — Latitude and Longitude
- **HGHT** — Station elevation in meters

Missing values are encoded as `-9999`.

---

## Technologies Used

| Technology | Purpose                          |
|------------|----------------------------------|
| Python     | Core programming language        |
| Flask      | Web framework & routing          |
| Pandas     | Data loading and manipulation    |
| HTML/Jinja2| Home page templating             |

---

## License

This project is open source and available under the [MIT License](LICENSE).
