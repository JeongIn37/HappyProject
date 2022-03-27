# Django REST Framework를 이용한 회원가입, 로그인 기능 구현

## 회원가입
```python
POST /user/signup
```
- Request
```json
{
    "id": "happy",
    "password": "happy123",
    "nickname": happy
}
```

- Response
```json
{
    "success": "True",
    "status code": 201,
    "message": "user registered successfully!"
}
```


## 로그인
```python
POST /user/login
```
- Request
```json
{
    "id": "happy",
    "password": "True",
}
```
- Response

```json
{
    "id": "happy",
    "success": "True",
    "status_code": 200,
    "message": "Login success!"
}
```
