
API TO TEST:

http://hertaskflask-app.herokuapp.com/api/admin/
                    write message (should be added auth + key)

http://hertaskflask-app.herokuapp.com/api/admin/
                    all messages

http://hertaskflask-app.herokuapp.com/api/user/234456456/all/
                    get all  messages for a specific user

http://hertaskflask-app.herokuapp.com/api/user/234456456/unread/
                    get all unread messages for a specific user
                    
http://hertaskflask-app.herokuapp.com/api/read/message_id/39/user_id/23245/
                    read one single message and it changing its status to read but only of it's reciever
