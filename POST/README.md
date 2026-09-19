# FastAPI Patient API

This project is a Patient API built using FastAPI. I used a JSON file to store patient data and created different API endpoints to view, create, update, sort, and delete patient records.

## What I Learned and Implemented

Created a FastAPI application using FastAPI() and learned how API routes are created and handled.

Used Pydantic BaseModel to define the structure of patient data and validate incoming data.

Used Field() to add validation and descriptions to patient fields such as age, height, and weight.

Used Literal to restrict the gender field to specific values.

Used computed_field and property to calculate BMI and determine the patient's health verdict.

Used a patients.json file to store patient data and created functions to load and save the data.

Used path parameters to receive a patient ID from the URL.

Used query parameters to sort patients based on height, weight, or BMI in ascending or descending order.

Used HTTPException to handle errors such as invalid patient IDs, invalid sorting fields, and duplicate patients.

Created a POST endpoint to add a new patient.

Created a PUT endpoint to update existing patient information.

Created a DELETE endpoint to remove a patient.

Used model_dump() to convert Pydantic objects into dictionaries before storing the data in the JSON file.

## Endpoints

/ – Returns a welcome message.

/about – Returns information about the API.

/view – Returns all patient data.

/patient/{patient_id} – Returns details of a specific patient.

/sort – Sorts patients based on height, weight, or BMI.

/create – Creates a new patient.

/edit/{patient_id} – Updates an existing patient's information.

/delete/{patient_id} – Deletes a patient.

## What I Practiced

Through this project, I practiced building a CRUD API with FastAPI, using Pydantic for validation, working with path and query parameters, handling JSON data, calculating values using computed fields, handling errors, and performing create, read, update, and delete operations.

[View Code](./main.py)
