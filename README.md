## About
Goal of this project is to query metar station data from their APIs and present it in a client friendly manner, along with caching the data to improve client experience. 

## Get started

1.  Setup virtualenv

	```
    virtualenv venv
    ```
    
	```
    source venv/bin/activate
    ```

2. Install dependencies using requirements.txt

	```
    pip install -r requirements.txt
    ```

3. Start the django server

	```
    python manage.py runserver
    ```
    
4. Start the redis server

    
    ```
    brew install redis
    ```
    
    ```
    brew services start redis
    ```


make sure redis server is running on 127.0.0.1 local host on port 6379 (default settings).

5. Endpoints and Query parameters

	There is one active endpoint on which scode's could be queried on.

	`http://127.0.0.1:8000/api/`

	Accepted query parameters are **scode** and **nocache**.
	i) scode - Recognized Station code's could be queried against, **to find out which are the supported stations check weatherAPI/Assets/stations.csv**
	ii) nocache - by default if data is present in cache, will be returned but in case no cache is set to 1, it will fetch the latest weather data and update the cache.

Example: 


![Screen Shot 2022-04-10 at 3 04 59 PM](https://user-images.githubusercontent.com/17986447/162612008-a2be4faf-f2ee-449a-aac0-e9878f7c48aa.png)

_Querying first time, data gets stored in cache._




![Screen Shot 2022-04-10 at 3 29 09 PM](https://user-images.githubusercontent.com/17986447/162612993-007e63b7-5ffe-4a46-a5a8-6af328aa6980.png)

_Getting cached response from next time._




![Screen Shot 2022-04-10 at 3 29 39 PM](https://user-images.githubusercontent.com/17986447/162612981-e1838efd-3b22-4584-ace3-6bbd5bada324.png)

_Setting nocache=1 to get fresh data._


 ## Project structure
Following is a breakdown of the project folder structure, along with use cases.
weatherAPI directory holds, 
1. Assets - Will hold all the constants and fixture type data.
2. Modules - Will hold all the buisness logic for the project.
3. Serializers - Add all the Serializers here.
4. Views - Client facing views to be defined here.



