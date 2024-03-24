# rating_system

## Database schema

![alt Database](https://github.com/muhammadkhanusmanov/rating_system/blob/main/db.png?raw=true)

## Enpoints

| ENPOINT | METHOD | DESCRPTION |
|---------|--------|------------|
| user/login/ | Post | Basic Authentication |
| student/subjects/ | Get | get student's subjects by token authentication |
| teachers/<str:id> | Post | Get subject's teacher by token authentication<br/>**id** - subject id |
| putmark/ | Put | Put the mark to teacher by student |
| getmarkarchive/ | Post | Get the mark archive of the student<br/>by token authentaction|


## Useing enpoints

#### user/login/
> ##### Request
>> `Authoration > Basic Authentication` <br/>`Body > None`
> ##### Response
>> `Token:str, Status: User role`

#### student/subjects/
> ##### Request
>> `Authorization > Token Authentication` <br/> `Body > None`
> ##### Response
>> `[{'id','name','full_name','img','teachers'}...]`