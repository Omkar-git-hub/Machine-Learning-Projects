// Function to toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    const card = document.querySelector(".card");
    if (card) {
        card.classList.toggle("dark-mode");
    }
    
    const resultDiv = document.getElementById("uiEstimatedPrice");
    if (resultDiv) {
        resultDiv.classList.toggle("dark-mode");
    }
}

// Event listener for the dark mode toggle button
document.getElementById("darkModeToggle").addEventListener("click", toggleDarkMode);

// Function to get the selected number of bathrooms
function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1; // Invalid Value
}

// Function to get the selected number of BHK
function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1; // Invalid Value
}

// Function to estimate the price based on user input
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    //var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx 
    var url = "/api/predict_home_price"; // Use this if  you are using nginx. 

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function (data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
}

// Function to load location names on page load
function onPageLoad() {
    console.log("document loaded");

    //var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx 
    var url = "/api/get_location_names"; // Use this if  you are using nginx. 
    $.get(url, function(data) {
        console.log("got response for get_location_names request");

        if (data) {
            var locations = data.locations;

            var uiLocations = document.getElementById("uiLocations");
            $(uiLocations).empty();

            for (var i in locations) {
                var opt = new Option(locations[i]);
                $(uiLocations).append(opt);
            }
        }
    });
}

// Load location names when the page is loaded
window.onload = onPageLoad;