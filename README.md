# Análisador Léxico

Análisador léxico construído para disciplina INE5426-06208 (20231) - Construção de Compiladores para gramática CC-2023-1. Feito pelos alunos Felipe Valentin Nascimento (20100523) e Anderson Sales Zambeli (20104138).

## Instalação
### Ferramentas:
Antes de instalar as bibliotecas é necessário instalar as ferramentas:
- python 3.10.6 (testado também com a 3.11.2)
- pip (normalmente vem com python)
- make

### Bibliotecas
As bibliotecas utilizadas estão dentro da pasta requirements.txt e podem ser instaladas:

```shell
make setup
```

## Execução
Para rodar basta executar:

```shell
make run FILE="pathto-file"
```
A saída será no terminal, uma lista de tokens e uma tabela de símbolos.

## Programas

Os programas de teste podem ser encontrados no diretório `examples`.
