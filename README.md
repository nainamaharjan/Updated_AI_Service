# Updated_AI_Service


Installation and Setup
Follow these steps to install and run the project:

Step 1: Install Python
If Python is not installed on your machine, download and install it from python.org.

Step 2: Install Miniconda
Download and install Miniconda from the following link: Miniconda Installation Guide.

Step 3: Configure Python Interpreter in Your IDE
1. Open your project in your preferred IDE (e.g., PyCharm, VSCode).
2. Navigate to the project settings:
    * For PyCharm: File -> Settings -> Project: <Project Name> -> Python Interpreter.
3. Add a new Python interpreter:
    * Click on Add Interpreter.
    * Select Add Local Interpreter.
    * Choose Conda Environment.
    * Select Create New Environment.
    * Edit the environment name and set the Python version to 3.10.
4. From the Python Interpreter settings, select the newly created environment name.

Step 4: Set Up the Conda Environment
1. Open a terminal in the project directory.
2. Activate the newly created Conda environment: conda activate <newly_created_environment_name>
3. Install all the required packages using the requirements file: pip install -r requirements.txt 
Step 5: Download the Model
1. Run the following command in the terminal to download the model:  huggingface-cli download TheBloke/phi-2-orange-GGUF phi-2-orange.Q8_0.gguf
2. After the model download is completed, note the provided path and copy it.

Step 6: Update the Model Path in the Project
1. Open settings.py in the project directory.
2. Paste the copied path into the appropriate configuration variable.

Step 7: Start the API
1. In the terminal, run the following command to start the API: sh start_api.sh 
Step 8: Start the UI
1. Open an additional terminal.
2. Run the following command to start the UI: sh start_ui.sh  
Now your project should be up and running with the API and UI started.