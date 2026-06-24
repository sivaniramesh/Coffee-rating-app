# ☕ Coffee Rating App

A simple full-stack web application that allows users to vote for their favorite coffee. The application is built using **Flask**, **SQLite**, **HTML**, **CSS**, and **JavaScript**.

## Features

* View a list of coffee varieties
* Vote for your favorite coffee
* Real-time vote count updates
* Data stored in SQLite database
* Responsive and user-friendly interface

## Technologies Used

* Python
* Flask
* SQLite
* HTML5
* CSS3
* JavaScript

## Project Structure

```text
Coffee Rating App/
│
├── app.py
├── coffee_db.sqlite
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── main.js
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/sivaniramesh/Coffee-rating-app.git
cd Coffee-rating-app
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Get All Coffees

```http
GET /coffees
```

### Vote for a Coffee

```http
POST /vote
```

Request Body:

```json
{
  "name": "Latte"
}
```

Response:

```json
{
  "name": "Latte",
  "votes": 1
}
```

## Future Enhancements

* Add authentication
* Display voting charts
* Prevent duplicate votes
* Add more coffee varieties
* Deploy to cloud platforms

## Author

**Sivani Ramesh**

GitHub: https://github.com/sivaniramesh

