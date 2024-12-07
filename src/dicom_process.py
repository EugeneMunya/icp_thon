import os
from pydicom import dcmread
import numpy as np

#DICOM image datasets
#https://www.kaggle.com/datasets/unidatapro/chest-xray

def choises():
    print("------------------------------------------------")
    print(
        'please chose an action to perform\n\n'
        '1: Search patient medical image\n'
        '2: upload medical image (DICOM file)\n'
        '3: exit the program\n'
    )
    print("------------------------------------------------")

    
user_id,img_url=None,None
choises()
while not (choise :=int(input("# ") or 3)) == 3:
    if choise ==1:
        user_id = input("please enter patient id: ")
        print(user_id)
        command=f"dfx canister call dicom_chain get '(\"{user_id}\")'"
        process = os.popen(command).read()
        print("=============================================")
        print({"userid":user_id,'image_data':process}, "patient information")
    elif choise == 2:
        img_url= input("please drag the imge and drop it here: ")
        
        dicom_data = dcmread('/home/eugene/kybra_hello_world/images/MR.1.2.246.352.221.4703919215052487572534317490624787106.dcm')
        patient_id = dicom_data.PatientID
        if len(patient_id) <=1:
            break
        img_arr = np.array(dicom_data.pixel_array)
        print("".join(str(n) for n in img_arr))
        img_str="".join(str(n) for n in img_arr.flatten()[:50])
        command=f"dfx canister call dicom_chain insert '(\"{patient_id}\",\"{img_str}\")'"
        process = os.popen(command).read()
        print("=============================================")
        print({"patient_id":patient_id,'image_data':img_str}, "patient medical image saved sussefully")
    choises()
    