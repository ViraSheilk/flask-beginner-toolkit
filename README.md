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
   
2. QUICK SUMMARY OF THE TECHNOLOGY
   
   What is Flask?
   Flask is a light weight web framework used to build web applications.
   
   Where is it used?
   It is used in creating small web applications, APIs and websites quickly and efficiently.
   
   Real World Example
   
   Flask is used in real-world projects where developers need to build web applications quickly and efficiently.
   For example, Startups oftenly use python flask to create MVPs like simple dashboards, booking systems or task management apps before scaling them into larger platforms.
   It is also commonly used to build APIs that power mobile apps or connect different services together.
   
3. SYSTEM REQUIREMENTS
   
   To run this project using Flask, the following requirements are needed:
   
   Operating system: Windows, MacOS or Linux.
   
   Programming Languages: Python 3.x version installed.
   
   Package Manager: pip, comes with python.
   
   Code editor: Any that supports flask but visual studio code is more recommended.
   
   Browser: Any modern web browser like chrome, edge, firefox etc.
   
   Virtual environment: venv
   
4. INSTALLATION AND SET UP INSTRUCTIONS
   
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
          
5.4 Deleting Notes features

   In this step you enhance the application features by allowing users to delete notes.

   Step 1: Update your backend that is app.py
                  
    from flask import Flask, render_template, request
    app = Flask(__name__)
     notes = []
      @app.route("/", methods=["GET", "POST"])
      def home():
       if request.method == "POST":
        note = request.form.get("note")
        delete_index = request.form.get("delete")

        # Add note
        if note:
            notes.append(note)

        # Delete note
        if delete_index:
            notes.pop(int(delete_index))

    return render_template("index.html", notes=notes)
    if __name__ == "__main__":
    app.run(debug=True)

  Step 2: Update your frontend (index.html)
     Modify it to include a delete button for each note.
         
    <!DOCTYPE html>
     <html>
    <head>
    <title>Notes App</title>
    </head>
     <body>
    <h1>My Notes</h1>
    <!-- Add Note Form -->
    <form method="POST">
        <input type="text" name="note" placeholder="Enter a note">
        <button type="submit">Add Note</button>
    </form>
    <!-- Notes List -->
    <ul>
        {% for note in notes %}
            <li>
                {{ note }}

                <!-- Delete Form -->
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="delete" value="{{ loop.index0 }}">
                    <button type="submit">Delete</button>
                </form>

            </li>
        {% endfor %}
    </ul>
    </body>
    </html>

Step 3: Run the application

       python app.py
Expected result:

<img width="335" height="150" alt="image" src="https://github.com/user-attachments/assets/1190901e-72b8-425f-b4a9-df16d313762f" />

After clicking delete button:

<img width="235" height="110" alt="image" src="https://github.com/user-attachments/assets/69f1006a-1617-43e2-a01d-c8fc1b4886df" />

5.5 Improving UI styles

In this step we improve the UI style of the Notes app.

Step 1: Update index.html

improve your style using embedded CSS style

    <!DOCTYPE html>
    <html>
    <head>
        <title>Notes App</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0b1f3a;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            width: 400px;
        }

        input {
            padding: 10px;
            width: 70%;
            border-radius: 5px;
            border: none;
        }

        button {
            padding: 10px;
            border: none;
            border-radius: 5px;
            margin-left: 5px;
            cursor: pointer;
        }

        .add-btn {
            background-color: white;
            color: #0b1f3a;
        }

        .delete-btn {
            background-color: red;
            color: white;
            margin-left: 10px;
        }

        li {
            margin-top: 10px;
            list-style: none;
        }
    </style>
     </head>

     <body>

    <div class="container">
        <h1>My Notes</h1>

        <!-- Add Note -->
        <form method="POST">
            <input type="text" name="note" placeholder="Enter a note">
            <button class="add-btn" type="submit">Add</button>
        </form>

        <!-- Notes List -->
        <ul>
            {% for note in notes %}
                <li>
                    {{ note }}

                    <form method="POST" style="display:inline;">
                        <input type="hidden" name="delete" value="{{ loop.index0 }}">
                        <button class="delete-btn" type="submit">Delete</button>
                    </form>

                </li>
            {% endfor %}
        </ul>
    </div>
    </body>
    </html>
Step 2: Run the app

          python app.py

Output

<img width="409" height="192" alt="image" src="https://github.com/user-attachments/assets/37b51824-102e-44a5-9f47-46a0a0bf1c0f" />

Step 3: API response summary

<img width="384" height="122" alt="image" src="https://github.com/user-attachments/assets/f7a28139-128e-4f13-9dc3-6a13497a750b" />

<img width="951" height="436" alt="image" src="https://github.com/user-attachments/assets/a0b623c1-ceb2-4356-9a0a-21eb9d731c93" />




6. AI PROMPT JOURNAL
   
   This section documents how AI was used as a learning assistant throughout the development of the flasks Notes app.

   Prompt 1: Installation and Environment set up

   Prompt used: Give me a step-by-step guide to install Flask on Windows/Mac/Linux using a virtual environment.

   AI's response summary- The AI provided a clear guideline on installing python, creating a virtual environment, activating it and installing Flask using pip. It also helped me understand why virtual environments are important in separating project dependencies.

   Prompt 2: Understanding Flask basics

   Prompt used: Explain Flask to a beginner.

    AI's or Chat gpt's response summary:  The AI explained Flask as a lightweight web framework that uses routes to connect URLs to Python functions.

   Helpful part- routes define what happens when a user visits an URL.

   This helped in understanding the structure before coding.

   Prompt 3: Creating a Basic Flask app structure.

   Prompt used: Show me how to structure a simple Flask application.

   AI response summary: The AI showed how to create app.py, initialize flask and defined a basic route that renders content.

   Prompt 4: Fixing why the app was not running.

   Prompt used: My Flask app is not running after i type python app.py why?

   AI response summary: The AI identified the missing block of code app.run as the issue and advised me on how to embed it correctly.

   Evaluation: This was a critical debugging step that helped run the app.

   Prompt 5: Building the Notes app (logic features)

    Prompt used: How do I store user input in Flask and display it on a page?

    AI's response summary: The AI explained how to use request.form to capture input and store it in a python list.

    Helpful part- suggested i use request.form.get('note') to capture form data.

    This helped in forming the core functionality of the notes app.

   Prompt 6: Connecting Flask to HTML Templates.

    Prompt used: How do I display Python data in an HTML page using Flask?

    AI response summary: The AI explained render_template() and passing variables into HTML templates.

    Helpful part: Pass data using render_template('index.html', notes=notes). which was essential for displaying stored notes in the UI.

   Prompt 7: Building the full notes app

    Prompt used: Help me build a simple Flask notes app step by step.

    AI response summary: The AI combined routing, form handling, and template rendering into a working notes application.

    Helpful part: Use a list to temporarily store notes and update it on POST requests. This was helpful in understanding and developing the final working MVP.

   Prompt 8: Understanding Flask code line by line.

    Prompt used: Explain this flask code line by line for a beginner.

    AI response summary: The AI broke down each part of the Flask app including routes, request handling, and rendering templates.

    Helpful part: @app.route('/') connects a URL to a Python function which helped in solidifying my understanding as i wrote the code in my editor.


7. COMMON ISSUES AND FIXES

   Problem

   Running: app.py

   The server failed to start by producing no output.

   Cause: The flask application missed the line of code to activate the server.

   Fix: The AI recommended i updated the missing the following piece of code in my app.py as it was the missing dependency.

       if __name__ == __"main"__:
       app.run(debug=True)
   What i learned: Flask does not run automatically after installation, a missing dependency may fail to start the server therefore the code to run server is important.

   Issue 2: Virtual Environment Not Activated

    Problem: The flask commands were not working and the modules were not found.

    Cause: The virtual environt (venv) was not activated before running the module.

    Fix: I activated it using this on my git bash:
   
                   source venv/Scripts/activate

   What I learned: Each project needs to use its own environment to avoid dependency conflicts.

   Issue 3: Templates not rendering.

   Problem: Flask returned an error when trying to learn index.html

   Cause: The HTML file was not placed inside a templates folder.

   Fix: Created the corrected structure in the right folder.

   What i learned: Flask only looks for HTML files inside a folder named templates due to the concept of convetion over configuration.

   Issue 4: Form data not being captured

   Problem: Submitting a note did not display any data.

   Cause: Had incorrect handling of form data as it missed POST method in the route.

   Fix: Updated my route to include post.

   What I learned: Forms require POST requests and Flask needs to be configured first to run them.

   Issue 5: Notes not updating on page

   Problem: Notes were not showing after submission

    Cause: The notes list was not being passed to the template.

    Fix: updated the code to pass notes.
   
        return render_template("index.html", notes=notes)

   What i learned: Data must be explicitly passed from Flask to HTML using render_template().

8.HELPFUL RESOURCES

These resources helped resolve issues and deepen understanding:

Flask Official Documentation:

https://flask.palletsprojects.com/

Stack Overflow (for debugging errors):

https://stackoverflow.com/

Python Virtual Environment Guide:

https://docs.python.org/3/library/venv.html

9. REFLECTION

    Through this project, I've learned how Flask is used by developers to quickly build API-based web applications with minimal setup. It showed me how backend logic,
    routing and user input handling come together to create a working application.

   Most of the challenges I faced were caused by small but important issues, such as missing dependencies or configuration steps. Solving these errors helped me better         understand how Flask works step by step and improved my debugging skills.

   Overall, the project strengthened my ability to build and troubleshoot a simple web application from scratch.

   

   

   






    



