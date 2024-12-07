DICOMchain an application which decentralize medical images and allows quick access and collaboration between hosipitals and clinics
To run this application locally you must follow this steps

 - install the following in your machine
   https://demergent-labs.github.io/kybra/installation.html
- git colne this repo
- cd into the root folder
- create and source a virtual environment by running
   ~/.pyenv/versions/3.10.7/bin/python -m venv venv
   source venv/bin/activate
- install Kybra and the Kybra dfx extension by running
   pip install kybra
   python -m kybra install-dfx-extension

- in terminal run  dfx start --background
- run again dfx deploy
- open new terminal and cd in the src folder and run python dicom_process.py and follow the instractions
