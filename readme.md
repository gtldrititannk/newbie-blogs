# Newbie-Blogs

  It is the Micro Blog Website implemented in Django Framework.


## Newbie-Blogs Installation steps

1:- Repository Clone

```
git clone https://github.com/gtldrititannk/newbie-blogs.git
```

2:- Creating Virtual Environment
 
 > Note:- Virtual Environment is  never committed in Version Control.

```
virtualenv -p python3.6 venv_newbie_blogs
```

- Activate The Virtual Environment

```
source venv_newbie_blogs/bin/activate 
```

3:-  Install dependencies from requirements.txt File.

```
pip install -r requirements.txt
```

4:- Create local.py file 

```
cp newbie_blogs/newbie_blogs/settings/example-production.py newbie_blogs/newbie_blogs/settings/local.py
```

5:- Run migrations

> Note:- manage.py file is located in project root folder

```
python manage.py makemigrations
python manage.py migrate
```

6:- Run the project
```
python manage.py runserver
```

## Blog APIs Testing (postman)

1:- [POST] create token using the following url:

> Note: Enter username and password in body section.
```
 localhost:portnumber/create-token/
```
2:- Blog list [GET]
 
> Note:  Pass Auth token in headers section for authentication. This is mandatory for each operations. 

```
 localhost:portnumber/create-token/
```

3:- Create Blog [POST]

```
 localhost:portnumber/create-token/
```

4:- Update Blog [PUT]

> Note: Pass blog id in the url for retrieve and update blog.
```
 localhost:portnumber/create-token/(id)
```

5:- Delete Blog [DELETE]

> Note: Pass blog id in the url for deleting blog.

```
 localhost:portnumber/create-token/(id)
```