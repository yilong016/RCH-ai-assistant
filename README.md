# rch-ai-assistant
rch assistent powered by generative AI

This is sample code demonstrating the use of Amazon Bedrock and Anthropic Claude 3 to satisfy multi-modal use cases. The application is constructed with a simple streamlit frontend where users can input zero shot requests to satisfy a broad range of use cases, including image to text multi-modal style use cases.

# **Goal of this Repo:**
The goal of this repo is to provide users the ability to use Amazon Bedrock (specifically Claude3) and generative AI to leverage its multi-modal capabilities, allowing users to insert text questions, images, or both to get a comprehensive description/or answer based on the image and/or question that was passed in.
This repo comes with a basic frontend to help users stand up a proof of concept in just a few minutes.

The architecture and flow of the sample application will be:

![Alt text](images/architecture.png "POC Architecture")

When a user interacts with the GenAI app, the flow is as follows:

1. (1a) The user uploads an image file to the streamlit app, with or without a text question. (Home.py). (1b) The user inserts a text question into to the streamlit app, with or without an image. (Home.py).
2. The streamlit app, takes the image file and/or text and saves it. The image and/or text is passed into Amazon Bedrock (Anthropic Claude 3). (llm_invoke.py).
3. A natural language response is returned to the end user, either describing the image, answering a question about the image, or answering a question in general. (Home.py).

# How to use this Repo:

## Prerequisites:
1. Amazon Bedrock Access and CLI Credentials.
2. Ensure Python 3.9 installed on your machine, it is the most stable version of Python for the packages we will be using, it can be downloaded [here](https://www.python.org/downloads/release/python-3911/).

## Step 1:
The first step of utilizing this repo is performing a git clone of the repository.

```
git clone https://github.com/yilong016/rch-ai-assistant.git
```

## Step 2:
Set up a python virtual environment in the root directory of the repository and ensure that you are using Python 3.9. This can be done by running the following commands:
```
pip install virtualenv
python3.9 -m venv venv
```
The virtual environment will be extremely useful when you begin installing the requirements. If you need more clarification on the creation of the virtual environment please refer to this [blog](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).
After the virtual environment is created, ensure that it is activated, following the activation steps of the virtual environment tool you are using. Likely:
```
cd venv
cd bin
source activate
cd ../../ 
```
After your virtual environment has been created and activated, you can install all the requirements found in the requirements.txt file by running this command in the root of this repos directory in your terminal:
```
pip install -r requirements.txt
```

## Step 3:
Now that the requirements have been successfully installed in your virtual environment we can begin configuring environment variables.
You will first need to create a .env file in the root of this repo. Within the .env file you just created you will need to configure the .env to contain:

```
profile_name=<AWS_CLI_PROFILE_NAME>
save_folder=<PATH_TO_ROOT_OF_THIS_REPO>
```
Please ensure that your AWS CLI Profile has access to Amazon Bedrock!

## Step 4:
As soon as you have successfully cloned the repo, created a virtual environment, activated it, installed the requirements.txt, and created a .env file, your application should be ready to go. 
To start up the application with its basic frontend you simply need to run the following command in your terminal while in the root of the repositories' directory:

```
streamlit run Home.py
```
As soon as the application is up and running in your browser of choice you can begin uploading images and or text questions and generating natural language responses detailing the images or the specific questions that were asked.. 

## ***The contents of this repository represent my viewpoints and not of my past or current employers, including Amazon Web Services (AWS). All third-party libraries, modules, plugins, and SDKs are the property of their respective owners.***
