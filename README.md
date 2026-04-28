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

  pip install flask

  Step 6: Verify the Installation:

  Check the installed packages

  pip list

  You should see Flask in the list

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
   

  



