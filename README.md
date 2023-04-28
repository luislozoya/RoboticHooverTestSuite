# RoboticHooverTestSuite
Test implementation of the imaginary robotic hoover service


### About the project:
This project was created mainly using Python and Cucumber, and other dependencies. 
These can be found inside the requirements.txt which is used to automatically install them.
Other dependencies not inside the txt file are listed in the instructions section.

The project structure is the following:

    RoboticHooverTestSuite
    ├── configs/ ---> For project configurations and properties
    ├── data_provider/ ---> For providing data, in this case config file reader and paths
    ├── features/ ---> Contains the core of the project (steps, environment and hoover feature)
    ├── reports/ ---> Contains generated reports of the features and steps
    ├── runner/ ---> Provides an alternate form of running the project
    ├── src/ ---> Provides the code that the steps need


### Validation strategy:

Although not all was automated due to time concerns like giving a big room size, lots of patches of dirt. 
They were tested using postman. The strategy for validation and testing is the following:

    -Providing invalid input payloads (e.g. negative coordinates, non-existent instructions)
    -Testing edge cases (e.g. a room with dimensions of 1x1, a hoover starting on a patch of dirt)
    -Testing the performance of the service with large inputs (e.g. a room with a lot of patches of dirt)
    -Invalid parameters in the payload
    -Missing payload information
    -Empty room size or coordinates
    -Invalid instructions
    -Hoover going out of bounds
    -Hoover finding already cleaned patch dirt
    -Hoover avoiding cleaning patch dirt and still registering like it did
    -Expected ending position
    -Expected starting position


### Assumptions:

The service is expected to always return a JSON response with keys "coords" and "patches".
The input JSON payload will always contain the following keys: "roomSize", "coords", "patches", "instructions".
The input JSON payload will always have valid data types and formats.
The service will always return valid data types and formats in the JSON response.

### Instructions:

This project requires the following tools:

    python3 : sudo apt-get install python3
    pip : sudo apt-get install python3-pip
    java 8+(for allure reporting) : sudo apt install openjdk-11-jdk
    allure : sudo apt-get install allure
    allure deb (2nd option in case of errors) : wget https://github.com/allure-framework/allure2/releases/download/2.21.0/allure_2.21.0-1_all.deb
        sudo dpkg -i allure_2.18.1-1_all.deb
    

This project requires the requirements.txt dependencies to install them simply run in a terminal inside the project the following command:
        
    pip install -r requirements.txt

There are several ways to run the project, Inside the project run:

    -behave 
        This will run the project and show results in console
        alternatively to save results you can use: 
            --outfile results.json --format json
            --outfile results.txt
    -behave -f allure_behave.formatter:AllureFormatter -o reports/allure
        To generate allure reports in json, then:
    -allure serve reports/allure
        To start a server with an eyecandy report in html.
        Or:
    -allure generate reports/allure -o reports/web/
        To generate an eyecandy report in html
    -python3 runner.py (inside runner/ directory)
        This runner contains the allure json generation and server in one command
      

The report result will show the Cucumber with gherkin format and the passed and failed test.
For the case of allure it will show more information like percentage of failed and passed, 
web navigation to view more detailed results. 

