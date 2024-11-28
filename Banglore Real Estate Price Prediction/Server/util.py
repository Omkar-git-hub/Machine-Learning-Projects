import json  # Import the json module for working with JSON data
import pickle  # Import the pickle module for loading saved model data
import numpy as np  # Import NumPy for numerical operations

__locations = None  # Initialize a variable to hold location names
__data_columns = None  # Initialize a variable to hold data column names
__model = None  # Initialize a variable to hold the trained model

def get_estimated_price(location, sqft, bhk, bath):
    # Function to estimate the price of a house based on location, size, and number of rooms
    try:
        # Get the index of the location in the data columns (lowercase)
        loc_index = __data_columns.index(location.lower())
    except:
        # If the location is not found, set loc_index to -1
        loc_index = -1

    # Create an array of zeros with the length of data columns
    x = np.zeros(len(__data_columns))
    x[0] = sqft  # Assign the size of the house (in sqft) to the first index
    x[1] = bath  # Assign the number of bathrooms to the second index
    x[2] = bhk  # Assign the number of bedrooms to the third index
    if loc_index >= 0:
        # If the location index is valid, set that index in x to 1
        x[loc_index] = 1

    # Predict the price using the trained model and return the rounded result
    return round(__model.predict([x])[0], 2)

def get_location_names():
    # Function to return the list of locations
    return __locations

def load_saved_artifacts():
    # Function to load saved model artifacts (data and model)
    print("loading saved artifacts...start")  # Print a message indicating the start of loading
    global __data_columns  # Declare that we are using the global variable __data_columns
    global __locations  # Declare that we are using the global variable __locations
    global __model  # Declare that we are using the global variable __model

    # Load data columns from a JSON file
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']  # Read and store the data columns
        __locations = __data_columns[3:]  # Store location names (all columns after the first three)

    # Load the trained model from a pickle file
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)  # Load and store the model
    print("loading saved artifacts...done")  # Print a message indicating the completion of loading

if __name__ == '__main__':
    # Check if the script is being run directly (not imported)
    load_saved_artifacts()  # Load the saved artifacts
    print(get_location_names())  # Print the list of location names
    # Print estimated prices for specified locations and house details
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))  # Estimate price for location with 3 BHK and 3 baths
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))  # Estimate price for location with 2 BHK and 2 baths
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # Estimate price for another location with 2 BHK and 2 baths
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # Estimate price for another location with 2 BHK and 2 baths
