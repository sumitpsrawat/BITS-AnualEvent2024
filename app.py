from flask import Flask, render_template, request, redirect, url_for
# from database import connect_to_db

app = Flask(__name__)

# admin credentials for login
def verify_user(email, password):
    if email == "admin@bits-pilani.ac.in" and password == "admin":
        return True
    return False

@app.route("/")
def home():
    # return render_template("index.html")
    # connection = connect_to_db()
    # if connection:
    #     # Fetch event details
        event_data = {"name": "Sample Event", "date": "2024-03-31", "description": "This is a sample event."}
    #     connection.close()
        return render_template("index.html", event=event_data)
    # else:
    #     return "Error: Database connection failed."

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        event_data = {"name": "Sample Event", "date": "2024-03-31", "description": "This is a sample event."}
        return render_template("register.html", event=event_data)
    elif request.method == "POST":
        # form validation and data storage
        name = request.form.get("name")
        email = request.form.get("email")
        # ... (other registration fields)
        return f"Registration successful! Name: {name}, Email: {email}"

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if verify_user(request.form.get("email"), request.form.get("password")):
        # actual admin functionalities
        return "Welcome admin!"
    else:
        return "Invalid login credentials."

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
