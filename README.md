# Falcon Tutorial

API para testar a framework Falcon e suas funcionalidades

## Dependências

- falcon `3.1.3`
- gunicorn `21.2.0`
- pylint `3.1.0`
- msgpack `1.0.8`

## Como executar o servidor

```bash
  gunicorn --reload src.server
```

## Criar e ativar o ambiente virtual

```bash
  python3 -m venv .venv && source .venv/bin/activate
```

OU

```bash
  virtualenv .venv && source .venv/bin/activate
```

## Instalar as dependências

```bash
  pip3 install -r requirements.txt
```
