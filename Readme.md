# Automate Birthday Wisher

Automatic Birthay Wisher by sending email to your friends and family from your **gmail** Id.

All the data of person and their birthday is stored in birthday.csv file

Make sure that you replace email and passsword with your email and password in the code

Before running the program you have to change some settings. 

We are using Google's Gmail service to send mail. So we need some settings (if required) for google's security purposes. If those settings are not set up, then the following code may not work, if the google doesnot support the access from third-party app.

To allow the access, we need to set 'Less Secure App Access' settings in the google account. If the two step verification is on, we cannot use the less secure access.

To complete this setup, go to the Google's Admin Console, and search for the Less Secure App setup.

![image](https://user-images.githubusercontent.com/83356501/132890553-1a650060-dcb4-4d61-befc-b98ff31961d3.png)

Check this Video if still didn't understood.
https://www.youtube.com/watch?v=XG8sRznnK4M

Now we have deloy this program on cloud so that we don't have to run this program everyday by ourself.

I will suggest pythonanywhere to deploy this program.

**To schedule, a Python script for execution on PythonAnywhere, follow these simple steps:**

- Sign up on https://www.pythonanywhere.com/ the account for Beginners is free with some T&C.
- Go to your Dashboard, Files, Upload a File and upload the Python file you want to schedule for execution.
- Go to Tasks and set the time of the day you want your script to be executed and type in the name of the Python file you uploaded (e.g., myfirstpyscript.py).
  **Note: The time entered should be in UTC.**
- Click “create” and you are done.

#### Please star this repository if you liked
