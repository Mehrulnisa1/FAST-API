from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator ,  computed_field
from typing import Optional, Annotated

class Address (BaseModel):
    city:str
    state: str
    pincode:str



class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="name of the patient",
            description="Give the name of the patient in less than 50 chars",
            examples=["Nitish", "Mehr"]
        )
    ]
    address: Address 
    email: EmailStr
    linkedin: AnyUrl
    age: int = Field(gt=0, lt=120)
    height: float
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: bool = False
    allergies: Optional[list[str]] = None
    contact_details: dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]

        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value
    @field_validator('name')
    @classmethod
    def transform_name (cls, value):
        return value.upper()


    @field_validator('age', mode='after')      #mode='before' will create error becuase int is string in dict and it cant compare int and str
    @classmethod
    def validate_age (cls, value):
        if 0 < value < 100:
            return value
        else:
           raise ValueError ('Age should be in between 0 and below 100')


    @model_validator (mode='after')
    def vaidate_emergency_contact(cls, model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact numbers')
        return model

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi



def insert_patient_data(patient: Patient):

     print(patient.name)
     print(patient.age)
     print("inserted")


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.calculate_bmi)
    print("updated")

address_dict= {'city': 'Btm', 'state':'sxr', 'pincode': '190010'}
address1= Address(**address_dict)




patient_info = {
    "name": "Mehr",
    "age": 30,
    "email": "email@hdfc.com",
    "linkedin": "http://linkedin.com/1322",
    "weight": 54.7,
    "height": 1.60 ,
    "allergies": ["pollens", "dust"],
    "contact_details": {
        "phone": "982222888" 
    } ,
    "address":address1
}
patient_dict = {"name":"mehr" , "gender":"female" , "address": address1}

patient1= Patient(**patient_dict)
print (patient1)
print (patient1.address.pincode)    #nested models
patient1 = Patient(**patient_info)  #validation & type coercion is done in this step

insert_patient_data(patient1)

update_patient_data(patient1)

temp = patient1.model_dump(include =['name'])   #dum_json = for json    (exclude=['name', gender]) // (exclude{'address': ['state']}) // exclude_unset=True

print(temp)
print(type(temp))