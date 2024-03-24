# rating_system

## Enpoints

| ENPOINT | METHOD | DESCRPTION |
|---------|--------|------------|
| user/login/ | Post | Basic Authentication |
| student/subjects/ | Get | get student's subjects by token authentication |
| teachers/<str:id> | Post | Get subject's teacher by token authentication<br/>**id** - subject id |
| putmark/ | Put | Put the mark to teacher by student |


## Useing enpoints

> #### user/login/
>> `Authoration > Basic Authentication <br/> Body > None` 