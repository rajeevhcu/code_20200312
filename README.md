# code-20200312
###Assessment test
I have made restful service with two end point one is to insert the data in db and another endpoint to get total count of overweight

In insert endpoint i am taking three field data in request body which is mentioned in json and calculating the bmi. Based on bmi value i am finding the category and health risk according to bmi range specified. And then saving the data in db.

I have created db as customer and table as bmi. Table have six fields. You can find the db details in database folder

# To Run the service
1. first need to install the package from requirements.txt
2. Do the db connection by putting right credential in config.py module in config folder.
3. Run the db query which i have kept in db_query.sql file in database folder.
4. After doing all setup Run 
   ######  Python3 wsgi.py
    

