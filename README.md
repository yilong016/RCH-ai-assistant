# build ecommerce assistant with genai

This is sample code demonstrating the use of Amazon Bedrock. The application is constructed with a streamlit frontend where users can input requests to satisfy a broad range of use cases, including text to image, image to image and image question-answer use cases.

# **Goal of this Repo:**
The goal of this repo is to provide users the ability to use Amazon Bedrock and generative AI capabilities to boost their business innovation and efficiency by using natural language.

# How to deploy:

## Prerequisites:
1. Amazon Bedrock Access.
2. Ensure Python 3.9 installed on your machine, it is the most stable version of Python for the packages we will be using, it can be downloaded [here](https://www.python.org/downloads/release/python-3911/).

Step 1:
The first step of utilizing this repo is performing a git clone of the repository.

Step 2:
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

Step 3:
Now that the requirements have been successfully installed in your virtual environment we can begin configuring environment variables.
You will first need to create a .env file in the root of this repo. Within the .env file you just created you will need to configure the .env to contain:

```
save_folder=<PATH_TO_ROOT_OF_THIS_REPO>
```

Step 4:
As soon as you have successfully cloned the repo, created a virtual environment, activated it, installed the requirements.txt, and created a .env file, your application should be ready to go. 
To start up the application with its basic frontend you simply need to run the following command in your terminal while in the root of the repositories' directory:

```
streamlit run Home.py
```
As soon as the application is up and running in your browser of choice you can begin uploading images and or text questions and generating responses detailing to the images or the specific questions that were asked.. 


## License

This library is licensed under the MIT-0 License. See the LICENSE file.