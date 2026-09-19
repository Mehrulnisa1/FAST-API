# Pydantic Patient Model

This project is a basic Patient model created using Pydantic. I used Pydantic to define the structure of patient data, validate the data, and perform different types of validation.

## What I Learned and Implemented

Created a nested Address model and used it inside the Patient model.

Used BaseModel to create Pydantic models for patient data.

Used Field() to add constraints and additional information to fields such as name, age, and weight.

Used Annotated to combine a Python type with field validation and metadata.

Used EmailStr to validate email addresses and AnyUrl to validate LinkedIn URLs.

Used Optional fields and default values for fields such as allergies and married.

Used field_validator() to create custom validation for email, name, and age.

Used before and after validation modes to understand when validation is performed.

Used model_validator() to validate multiple fields together, such as requiring an emergency contact for patients older than 60.

Used computed_field and property to calculate the patient's BMI.

Used model_dump() to convert a Pydantic model into a Python dictionary.

Used model_dump_json() to convert a Pydantic model into JSON.

Used include and exclude with model_dump() to control which fields are included in the output.

## What I Practiced

Through this project, I practiced creating Pydantic models, nested models, field validation, model validation, type validation, custom validators, computed fields, and converting Pydantic models into dictionaries and JSON.

[View Code](./main.py)
