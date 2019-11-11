# Group-Project
COSC 4351 Software Engineering

**#Virtual Environment(Optional, I just want to try this out during development)**  
To create, cd OUTSIDE project folder(Next to portal directory) and run the following command:  

```python3 -m venv ENV```  

ENV is the name you choose for your virtual environment  
#Activate virtual environment  
On Windows:  
```ENV\Scripts\activate.bat```  
On MAC:  
```source ENV/bin/activate```  
#Install necessary things in the virtual environment  
run command:  
```pip install -r```  
This will install everything in the requirements.txt file  
**If you install anything new for the project i.e Bootstrap 4.0, please run the following command:**  
```pip freeze```  
**copy and paste into requirements.txt and tell the team**  



**#Run the project**  
CD into your project folder and run:  
```python manage.py runserver```  
