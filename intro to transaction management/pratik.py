from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'user': 'root',              
    'password': '313141',  # Change as per your MySQL password
    'host': 'localhost',
    'database': 'testdb'         # Ensure this is the correct database name
}

@app.route('/')
def index():
    return render_template('index.html')

# Add User Function
@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Insert the user into the database
        insert_query = "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (username, email, password, role))
        connection.commit()  # Commit the transaction
        
        cursor.close()
        connection.close()
        
        return f"User added successfully!<br>Username: {username}<br>Email: {email}<br>Role: {role}"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error: {err}"

# Delete User Function
@app.route('/delete_user', methods=['POST'])
def delete_user():
    username_or_email = request.form['username_or_email']
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        
        delete_query = "DELETE FROM users WHERE username = %s OR email = %s"
        cursor.execute(delete_query, (username_or_email, username_or_email))
        connection.commit() 
        
        cursor.close()
        connection.close()
        
        if cursor.rowcount > 0:
            return f"User '{username_or_email}' deleted successfully!"
        else:
            return f"No user found with username or email '{username_or_email}'."
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return f"Error: {err}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
