# Final_Project ITESMMlops 2023

# Bankruptcy Detection

## Description

This project uses machine learning techniques to predict company bankruptcy using data from the "Company Bankruptcy Prediction" dataset.

## Baseline

The baseline (reference model) will be a simple model that acts as a comparison and is easy to explain. In addition, the baseline will be based on the dataset to create the actual model.

## Scope

The scope of this project is just a proof of concept for the subject. Other models can be trained using different techniques and machine learning algorithms. The final result will be a model capable of predicting company bankruptcy with reasonable accuracy.

## Questions


The problem addressed by this dataset is the prediction of company bankruptcy using machine learning techniques.
There are several notebooks already developed on Kaggle that use this dataset to predict company bankruptcy. Some examples include “Bankruptcy Prediction using Machine Learning” by the user “Siddharth Suresh” and “Bankruptcy Prediction using Neural Networks” by the user “Siddharth Suresh” .
Both of these notebooks contain the minimum necessary to train and save a model. The first notebook uses a Random Forest classifier to predict company bankruptcy, while the second notebook uses a Neural Network to make predictions.


## How to create and activate a virtual environment in windows and linux

## Windows
Open the command prompt (cmd) or PowerShell.
Make sure you have Python and pip installed. You can check if they are installed by running the commands python --version and pip --version. If they are not installed, you can download them from the official Python website.
Install the virtualenv package using the command pip install virtualenv.
Create a new virtual environment by running the command virtualenv [environment_name], replacing [environment_name] with the name you want to give to your virtual environment.
Activate the virtual environment by running the command [environment_name]\Scripts\activate, replacing [environment_name] with the name you gave to your virtual environment.
Once the virtual environment is activated, you can install packages from a requirements.txt file using the command pip install -r requirements.txt. Make sure to specify the correct path to the requirements.txt file.
## Linux
Open a terminal window.
Make sure you have Python and pip installed. You can check if they are installed by running the commands python3 --version and pip3 --version. If they are not installed, you can install them using your distribution’s package manager (e.g., apt-get install python3 python3-pip on Ubuntu).
Install the virtualenv package using the command pip3 install virtualenv.
Create a new virtual environment by running the command virtualenv [environment_name], replacing [environment_name] with the name you want to give to your virtual environment.
Activate the virtual environment by running the command source [environment_name]/bin/activate, replacing [environment_name] with the name you gave to your virtual environment.
Once the virtual environment is activated, you can install packages from a requirements.txt file using the command pip3 install -r requirements.txt. Make sure to specify the correct path to the requirements.txt file.




## Setup

To set up this project, follow these steps:

1. Make sure you have Python 3.10 installed on your system. You can download Python from the official Python website: [Python Downloads](https://www.python.org/downloads/).

2. Install the required libraries using pip. Open a terminal or command prompt and run the following command:

```python
pip install -r requirements.txt
```

3. Once the libraries are installed, you can run the project by executing the main script or running specific commands depending on your project structure.

# Running Tests in My Project

This project includes several test files that can be executed to validate the functionality of the code. Follow the instructions below to run the tests.

## Prerequisites

- Python installed on your machine
- Dependencies installed (if any). Make sure to install the required dependencies by running `pip install -r requirements.txt` if there is a `requirements.txt` file in the project.

## Test Files

- `test.py`: Contains general tests for the project.
- `test_for_data.py`: Contains tests related to data handling and loading.
- `test_my_model.py`: Contains tests for specific functions or classes of the model module.
- `model_test.py`: Contains tests that check the overall functionality of the model.

## API

To run the api open a command window and use the next command
```python
uvicorn main:app --reload
```
it should give something like this

![running API](my_folder_\images\image-4.png)
<div align="center">
    <img src="my_folder_\images\image-4.png" width="1000px"</img> 
</div>
## Running the Tests

To run the tests, follow these steps:

1. Open a command line or terminal window.

2. Navigate to the project directory using the `cd` command.

3. Run the desired test file using the `pytest` command. For example, to run `test.py`, execute the following command:

```python
shell pytest test.py
```


   You can replace `test.py` with `test_for_data.py`, `test_my_model.py`, or `model_test.py` to run the respective test files.

4. Observe the output in the terminal. The test results will be displayed, including any failures or errors encountered during testing.

   - Green checkmarks indicate successful tests.
   - Red crosses indicate failed tests.
   - Detailed error messages are provided for failed tests, allowing for easier debugging if necessary.

That's it! You can now run the tests in your project using the specified test files.

## Notes

- It's recommended to run the tests regularly to ensure the code's correctness and prevent regressions.
- Feel free to customize the tests or add more test files as needed to cover all aspects of the project's functionality.


# Docker Project Instructions

This README.md part of the file contains instructions for building, running, debugging, making predictions, and copying logs in the containerized application.

## Build the Image

To build the Docker image, run the following command:

```python
bash docker build -t final_project .
```

![Expected Output](my_folder_\images\image.png)
<div align="center">
    <img src="my_folder_\images\image.png" width="1000px"</img> 
</div>
## Check the images 

to check the docker images run the following command

```python
 docker images
```

![Expected output](my_folder_\images\image-1.png)
<div align="center">
    <img src="my_folder_\images\image-1.png" width="1000px"</img> 
</div>

## Run the Container

To run the Docker container, execute the following command:

```python
bash docker run -d --rm --name final_project-container -p 3000:8000 final_project
```


##Check the container information

to check this run the following command

```python
docker ps -a

```
![Expected Output](my_folder_\images\image-2.png)
<div align="center">
    <img src="my_folder_\images\image-2.png" width="1000px"</img> 
</div>

## Debug the Container

To access the running container and debug it, use the following command:

```python
bash docker exec -it final_project-container bin bash
```


## Make Predictions on the Local Machine

To make predictions on the local machine using the containerized application, execute the following command:

```python
bash curl http://localhost:3000/predict
```



## Copy Logs from the Container to the Local Machine

To copy logs from the container to the local machine, run the following command:

```python
docker cp bb2de4836286:debug.log .
```




## Check Debug Logs

To check the debug logs of the container, you can use the following command:

```python
docker logs -f bb2de4836286 | Select-String -Pattern "Debug"
```


This command will display the logs generated by the container, including any debug information.

Please ensure that you are in the same directory as the Dockerfile when running these commands.

## Docker Compose


## Create the network

First, create the network AIService by running this command:

## Run Docker Compose

Be sure you are un the directory where the docker-compose.yml file is located

Run next command to start the Server and Frontend APIs
```python
docker-compose up --build
```

## Run the following code to identify the CONTAINER ID of the Server container.

```python
docker ps -a
```


## Save the logs to the local machine

```python
docker cp bb2de4836286:debug.log .
```






For any further questions or assistance, please don't hesitate to reach out at jorgeadrian.dp@gmail.com.
