# FastAPI Patient API

This project is a basic Patient API built using FastAPI. I used a JSON file to store patient data and created different API endpoints to access and work with that data.

## What I Learned and Implemented

FastAPI Setup – Created a FastAPI application using FastAPI() and learned how the application is structured.

GET Routes – Created different GET endpoints such as /, /about, and /view to return different responses.

JSON Data – Used a patient.json file to store patient information and loaded the data into Python using the json module.

Path Parameters – Used /{patient_id} to receive a patient's ID directly from the URL and find the corresponding patient.

Path – Used Path() to describe and document the path parameter.

HTTPException – Used HTTPException to return proper error responses when a patient is not found or an invalid value is provided.

Query Parameters – Used Query() to receive additional information from the URL, such as which field to sort by and the sorting order.

Query Parameter Validation – Added validation to allow sorting only by height, weight, or bmi, and to allow only asc or desc as the order.

Sorting Data – Used Python's sorted() function and lambda to sort patient records based on height, weight, or BMI.

Ascending and Descending Order – Added support for both ascending and descending sorting using the order query parameter.

API Error Handling – Returned appropriate status codes and messages for invalid patient IDs, fields, and sorting orders.

## Endpoints

/ – Returns a basic welcome message.

/about – Returns information about the API.

/view – Returns all patient data.

/patient/{patient_id} – Returns details of a specific patient.

/sort – Sorts patients based on height, weight, or BMI.

## What I Practiced

Through this project, I practiced creating APIs with FastAPI, working with path and query parameters, reading JSON data, validating inputs, handling errors, and processing data before returning it through an API.

[View Code](./main.py)
