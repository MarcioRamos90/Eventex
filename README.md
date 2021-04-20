# Eventex

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.8
3. Ative seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/MarcioRamos90/Eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configuracões para o heroku.
3. Defina um SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o servico de email.
6. Envie o código para o heroku.


```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o Email
git push heroku master --force
```