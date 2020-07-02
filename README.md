"# hertask"



ps aux
kill -9 pid


python migrate.py db stamp head
python migrate.py db migrate
python migrate.py db upgrade



https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

TESTING:
{"message_id": "12822333439","chat_id":"23245","user_id":"234456456","chat_title":"chat_title","text":"text","username":"username","first_name":"first_name","date":"2020-01-14 23:12:12"}


TESTING HEROLO:
{"message_id": "12822333439","sender_id":"23245","reciever_id":"234456456","message":"message","subject":"subject"}


http://127.0.0.1:5000/api/user/234456456/unread/
http://127.0.0.1:5000/api/admin/
http://127.0.0.1:5000/api/read/155339/

https://hertask.herokuapp.com/
