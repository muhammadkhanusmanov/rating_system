# rating_system

## Enpoints

| ENPOINT | METHOD | DESCRPTION |
|---------|--------|------------|
| user/login/ | Post | Basic Authentication |
| student/subjects/ | Get | get student's subjects by token authentication |
| teachers/<str:id> | Post | Get subject's teacher by token authentication__`id` - subject id |