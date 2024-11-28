from flask import Flask, request, jsonify  # Import necessary modules from Flask
import util  # Import the utility functions from the util module

app = Flask(__name__)  # Create a new Flask application instance

@app.route('/get_location_names', methods=['GET'])  # Define a route for getting location names
def get_location_names():
    # Create a JSON response with the list of locations
    response = jsonify({
        'locations': util.get_location_names()  # Call the utility function to get location names
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow cross-origin requests

    return response  # Return the response

@app.route('/predict_home_price', methods=['GET', 'POST'])  # Define a route for predicting home prices
def predict_home_price():
    # Get the total square footage from the request form and convert it to float
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']  # Get the location from the request form
    bhk = int(request.form['bhk'])  # Get the number of bedrooms (BHK) and convert it to int
    bath = int(request.form['bath'])  # Get the number of bathrooms and convert it to int

    # Create a JSON response with the estimated price
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)  # Call utility function to estimate price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow cross-origin requests

    return response  # Return the response

if __name__ == "__main__":  # Check if the script is being run directly
    print("Starting Python Flask Server For Home Price Prediction...")  # Print a message indicating the server is starting
    util.load_saved_artifacts()  # Load saved artifacts (data and model)
    app.run()  # Run the Flask application
