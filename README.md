This is my first project after joining CodeClan. This project was created using Python, Flask, PostgreSQL and Jinja2. 


For the purpose and main functions of the Record Shop Manager, please refer to: 
https://github.com/taksgarby/record_shop_project_new/blob/main/presentation/record%20shop%20app.pdf



To run Record Shop Manager, please follow these steps:

1. On terminal, cd into db. Then DROP any existing conflicting db managers in terminal: 'dropdb record_shop_manager'
2. CREATE your db manager in terminal: 'createdb record_shop_manager'
3. JOIN the two with the following terminal command and create your tables: 'psql -d record_shop_manager -f record_shop_manager.sql'
4. cd back into the project directory. LOAD existing data in terminal by: 'python3 console.py'
5. RUN the app so you can access local host in terminal by: 'flask run'
6. OPEN host by clicking on '* Running on http://127.0.0.1:7000' use either option/cmd click to open this in a new browser
