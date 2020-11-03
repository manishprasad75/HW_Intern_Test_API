API Guid
End Point:-
    1. GET http://127.0.0.1:8000/api/
        {
            "email": "admin@gmail.com"
        }

                or
        {
            "user_id": 1,
            "password": "admin"
        }
    2. POST http://127.0.0.1:8000/api/
        {
            "email": "admin@gmail.com",
            "password": "123456",
            "first_name": "Manish",
            "last_name": "Prasad"
        }