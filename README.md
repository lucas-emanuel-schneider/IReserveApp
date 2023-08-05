# IReserve App

Este projeto faz uso do Django e NUXT 2.
Ele tem como objetivo criar uma aplicação fullstack para marcações de datas para uso de espaços físicos de uma empresa.

## Devido a problemas no versionamento não consegui fazer uso do docker no backend então a aplicação está sem docker:

## Configurando para rodar o backend:

```
python -m venv .venv
```
```
python -m venv .venv
```
```
source .venv/bin/activate
```
```
cd backend
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py runserver
```

## Configurando para rodar front:

```
cd frontend
```
```
npm install
```
```
npm run dev
```

### Todos os usuários e estações de trabalho são criados pelo administrador!!!
### Estações de trabalho devem ser definidas como Available para serem usadas!!!


```
http://localhost:8000/admin
```
[http://localhost:8000/admin](http://localhost:8000/admin)

Email do administrador:
```
admin@admin.com
```
Senha:
```
admin123
```

## O acesso ao front é feito em:

```
http://localhost:3000/
```
[http://localhost:3000/](http://localhost:3000/)

Email:

```
teste@teste.com
```

Senha:

```
teste123
```

Devido a problemas no Django fiquei impossibilitado de fazer uso do docker, das hashs nas senhas e uso do jwt nas requisições do front pelo navegador, então fiz alterações 
para que o front infelizmente não utilizasse o JWT e o CRSF token.
O arquivo ENV.example deve ser renomeado para .ENV com os valores adequados para o seu postgress