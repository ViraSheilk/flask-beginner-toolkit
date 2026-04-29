1. TITLE AND OBJECTIVES
   
   Title:Prompt-Powered Kickstart: Flask Notes and Routes
   
   Objective: To document the learning journey as I explore web development using Flask, a lightweight python framework used to build web applications and APIs.
   
   By following this toolkit a beginner will be able to:
   
   -Set up a development environment using python and a virtual environment.
   
   -Understand Flask basics which include routes and request handling.
   
   -Build a simple web app that can add and display notes.
   
   -Learn how to structure a simple web project in a clean and organized way.
   
   -Gain confidence in using AI tools to learn, debug and personal improvement.
   
   Why Flask?
   
   I chose Flask because it is simple and beginner-friendly, making it easy to learn web development.
   It helps me quickly build web applications while understanding core concepts like routes and requests and its also based on python making it easier to read and use.
   
   End Goal
   
   The project results in a minimal viable product: A Flask Notes web app which allows users to add notes through a form and view them in a simple webpage.
   
3. QUICK SUMMARY OF THE TECHNOLOGY
   
   What is Flask?
   Flask is a light weight web framework used to build web applications.
   
   Where is it used?
   It is used in creating small web applications, APIs and websites quickly and efficiently.
   
   Real World Example
   
   Flask is used in real-world projects where developers need to build web applications quickly and efficiently.
   For example, Startups oftenly use python flask to create MVPs like simple dashboards, booking systems or task management apps before scaling them into larger platforms.
   It is also commonly used to build APIs that power mobile apps or connect different services together.
   
5. SYSTEM REQUIREMENTS
   
   To run this project using Flask, the following requirements are needed:
   
   Operating system: Windows, MacOS or Linux.
   
   Programming Languages: Python 3.x version installed.
   
   Package Manager: pip, comes with python.
   
   Code editor: Any that supports flask but visual studio code is more recommended.
   
   Browser: Any modern web browser like chrome, edge, firefox etc.
   
   Virtual environment: venv
   
7. INSTALLATION AND SET UP INSTRUCTIONS
   
   Step 1: Install Python
   
   Download and install Python 3 from the official website: https://www.python.org
   
   During installation, make sure to check “Add Python to PATH”.

   Verify installation:

   python --version

   Step 2: Create Project Folder

   Create and move into your project:
   
  mkdir flask-notes-app
  
  cd flask-notes-app

  Step 3: Create a virtual environment:

  A virtual environment keeps project dependencies separate.

  python -m venv venv

  Step 4: Activate the virtual environment:

  Git Bash:

  source venv/Scripts/activate

  Windows CMD:

  venv\Scripts\activate
  
  You should see (venv) in your terminal if activation is successful.

  On MacOs/Linux:

  source venv/bin/activate

  Step 5: Install Flask:

  Install Flask inside the virtual environment

  <img width="303" height="182" alt="image" src="https://github.com/user-attachments/assets/c9e722d2-a3ab-41c6-9f70-48176e8306f6" />


  pip install flask

  Step 6: Verify the Installation:

  Check the installed packages

  <img width="541" height="217" alt="image" src="https://github.com/user-attachments/assets/d3616a66-6023-4ef6-a23b-4cb8e8a59c6b" />


  pip list

  You should see Flask in the list

  <img width="292" height="184" alt="image" src="https://github.com/user-attachments/assets/3b9a36ab-a5aa-48f7-924c-2a3de7243f4c" />

  Troubleshooting

  Issue 1: python not recognized

  Cause: Python is not added to your systems path during installation.

  Fix : Reinstall python and make sure you check : 'Add python to PATH during setup.'

  Issue 2: venv\Script\activate not working.

  Cause: Wrong terminal or wrong activation command.

  Fix: Use the correct command based on your OS.

  Issue 3: Flask not found after installation.

  Cause: Flask installed outside virtual environment.

  Fix: Activate virtual environment first and then you reinstall.

5. MINIMAL WORKING EXAMPLE
   
   Overview
   
   This steps walks you through building and running a simple Flask Notes application.

   This project is split into one minimal web MVP that demonstrates Flask components:

   Creating a web server.

   Defining routes.

   Returning responses in the browser.

   At this stage, the application does not yet store notes permanently but instead focuses on understanding how flask works before adding features.

   Project Structure

   Your repository should look like this:

   <img width="191" height="224" alt="image" src="https://github.com/user-attachments/assets/e649dc9e-5595-4e3e-bef2-8c71e34b2e92" />

   Part 1: Basic Flask Web Server

   app.py

   This is the starting point of your web application.

   In you app.py write the following code:

   Step 1: Import Flask

   from flask import Flask

   Step 2: Create the Flask app

   app=Flask(__name__)

   Explanation
   
   Flask is the framework used to create web applications.

   __name__ tells Flask where the application is located.

   This initializes your web server.

   Step 3: Create a route

   @app.route("/")
     def home():
    return "Welcome to my Notes App"

   "app.route("/") defines the homepage of your web app.

   When a user visits /, Flask runs the home() function.

   The function then returns text that is displayed in the browser.

   Step 4: Run the server

   if __name__== "__main__":

   app.run(debug=True)

   This starts the Flask development server.

   debug=True allows automatic reloading and error messages

     <img width="319" height="165" alt="image" src="https://github.com/user-attachments/assets/846c0d07-85d8-4519-bd74-be059fac9df8" />


   Running the Application

   Step 1: Start the server
   
   <img width="300" height="50" alt="image" src="https://github.com/user-attachments/assets/6fa6bf0b-5814-4b27-be03-6e6fad7dd9c9" />

   Step 2: Visit the browser
   
   <img width="672" height="118" alt="image" src="https://github.com/user-attachments/assets/d90a09c6-52d9-425d-9da9-562c75a51c3d" />

   Expected output:

   <img width="361" height="216" alt="image" src="https://github.com/user-attachments/assets/0f785a3c-32b2-4371-bb59-ea9437dc28b0" />

   In this stage Flask:

   -Starts a local web server.
   
   -Responds to your browser requests.
   
   -Displays a basic message on the homepage.

   This confirms your backend set up works correctly before adding more features.

 Common Beginner Issues

 Issue                                                         Cause                                                       Fix
 
 ModuleNotFoundError: Flask                                    Flask not intalled                                          Run pip install Flask
 
 Page not loading                                              Server not running                                          Run python app.py
 
 Port already in use                                           Another Flask app running                                   Change port or stop previous server
 

 5.2 Connecting Flask to HTML Templates

 In this step we replace plain text responses with a real HTML page.

 Step 1: Update your app.py

  Update your import line to:  from flask import Flask, render_template 

  Flask creates the app, while render_template sends the HTML files to the browser.

Step 2: Modify your routes

 Upgrade your routes to:

  @app.route("/")
def home():
    return render_template("index.html") 

This now loads the HTML file that comes from the templates folder.

Step 3: Create your HTML File

<img width="608" height="228" alt="image" src="https://github.com/user-attachments/assets/2cf33b89-226d-4797-b2f5-05f3edda9033" />

Step 3: Run your app

Run and open your browser through python app.py

<img width="317" height="109" alt="image" src="https://github.com/user-attachments/assets/ec067e2c-d01c-4de0-8c04-2476dc50fd4d" />

This helps you understand:

How Flask serves HTML Files.

How render_templates() works.

How frontend connects to backend.

5.3 Adding Notes Functionality Core Features

We upgrade the notes application from a static web page to its core features in this step.

 We will:

 -Accept user inputs from a form.

 -Store notes temporarily in memory.

 -Display notes on the webpage.

 These introduces key backend components like:

 -HTTP form requests that is GET and POST.

 -Form handling.

 -Dynamic content handling.

 Step 1: Create a Notes Storage

    notes =[]
   This is a python list that stores notes entered by users.

Step 2: Update your routes handle form

 <img width="371" height="216" alt="image" src="https://github.com/user-attachments/assets/a73ad577-ab4d-4260-81f5-5ff1968c6e12" />

 Methods GET and POST- GET loads the page while POST sends data from the form.

 request.form.get("note")- gets the value from the form input.

 notes.append(note)- adds the new note to the list.

 render_template("index.html", notes=notes)- sends notes to the HTML making them visible to the page.

Step 3: Running the Flask application

In the terminal execute 
      python app.py

You should see this output or similar:

<img width="587" height="141" alt="image" src="https://github.com/user-attachments/assets/7662ce21-4ea5-4af2-94a3-483dda01de98" />


Then open your browser the following should be displayed:

<img width="275" height="144" alt="image" src="https://github.com/user-attachments/assets/5af8f7ad-4f9d-4cd7-bd0d-35a3f53331f4" />

Write a note then click add note on your page, the note is displayed as shown below:

<img width="342" height="214" alt="image" src="https://github.com/user-attachments/assets/caf3f7b8-33ec-43e6-a530-6c79e4e6591b" />

Issues encountered.

Issue 1: Flask app not running

Cause: Missing app.run() block.

Fix:  Add 

          if __name__ == "__main__":
          app.run(debug=True)
   






    

 




   
   


   
   

  



