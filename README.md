<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-licença">Licença</a>
</p> 

<h1 align="center">Sistema de Agenda Telefônica em Python com PostgreSQL</h1>


## ⚙ Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
</br>

## 💻 Projeto

<p>
Este é um sistema de agenda telefônica construído em Python com o banco de dados relacional PostgreSQL. Ele é manipulado por comando no terminal e oferece as seguintes funcionalidades:
</p>
* Cadastro de pessoa com nome e telefone
</br>
* Adicionar pessoas cadastradas na lista de contatos de outra pessoa já cadastrada
</br></br>

## ⏩ Processo de criação
Como forma de boas praticas e para organização do sistema o mesmo foi separado em diversas pastas para que ficassem distribuidas de acordo com suas funções.

1. DB (Manipulação do banco de dados)
3. env (Ambiente virtual)
4. main.py (Arquivo base de execução)
5. requirements.txt (Arquivo com as necessidades de instalação)
</br></br>

## 🌌 Instalação
Siga estas etapas para instalar e executar o sistema:

1. Instale o PostgreSQL e crie um banco de dados.
2. Instale a biblioteca psycopg2 para Python, que é responsável pela conexão com o banco de dados PostgreSQL. Você pode instalar usando o seguinte comando:
```
pip install psycopg2
```
3. Clone o repositório do Github com o seguinte comando:
```
git clone https://github.com/seu-usuario/seu-repositorio.git
```
4. Ao clonar o repositorio digite no terminal:
```
pip install -r requirements.txt
```
5. Instale o PGAdmin(Pode ser em outro gerenciador também) no seu computador
6. Crie um database em localhost com o nome 'minha_agenda'
7. No console crie um novo usuário e um novo banco de dados executando os seguintes comandos (Ao criar analise se o usuario esta com todas as permissões):
```
CREATE USER meu_usuario WITH PASSWORD 'minha_senha';
CREATE DATABASE minha_agenda OWNER meu_usuario;
```
Pronto! Agora você tem um novo banco de dados PostgreSQL criado em localhost. Basta usar as informações de conexão adequadas no seu script Python para acessar o banco de dados.

## Execução
Rode no terminal 'main.py' e se divirta (Lembrando o banco deve ser configurado)

## ✔✔ Contribuição
Contribuições são sempre bem-vindas! Se você tiver alguma sugestão ou encontrar algum bug, por favor, abra uma issue ou faça um pull request.
</br></br>

## 📄 Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
</br></br>

## Autor

 <img style="border-radius: 50%" src="https://avatars.githubusercontent.com/u/69722024?v=4" width="100px" style="border-radius:50%"/>

 <sub><b>Carlos Vinicius</b></sub><a href="">🚀</a>
<br />

Feito com ❤️ por Carlos Vinicius 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Carlos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://https://www.linkedin.com/in/carlos-vinicius-95745a1a4)](https://www.linkedin.com/in/carlos-vinicius-95745a1a4) 
[![Gmail Badge](https://img.shields.io/badge/-carlosvinicius.index@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:carlosvinicius.index@gmail.com)](mailto:carlosvinicius.index@gmail.com)
