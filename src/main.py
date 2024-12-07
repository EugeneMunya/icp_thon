from kybra import (
    query,
    update,
)


# This is a global variable that is stored on the heap
patient_data:dict[str,str]={}


@query
def get(u_id:str) -> str:
    return patient_data[u_id]


@update
def insert(u_id:str, img:str) -> str:
    patient_data[u_id]=img
    return patient_data[u_id]

