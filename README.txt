# 🏪 Loja TC-SPORTS

Este é um projeto de catálogo de produtos desenvolvido com o objetivo de **exibir produtos esportivos** e suas informações. Ele oferece uma interface simples e funcional, onde os **clientes podem visualizar os produtos** e, ao clicarem no botão de contato, são redirecionados para o **WhatsApp do vendedor**, onde a negociação é realizada.

> ⚠️ **Importante:** Este projeto **não realiza vendas nem cadastros de clientes** diretamente pela aplicação, mas essas funcionalidades podem ser adicionadas futuramente conforme o projeto evolua.

---

## 📸 Funcionalidades

- ✅ Página principal com exibição de todos os produtos cadastrados
- ✅ Página com produtos organizados por **categorias**
- ✅ Página dedicada a **promoções**
- ✅ Página de detalhes de produto com botão para **contato via WhatsApp**
- ✅ Área administrativa protegida com login para:
  - ✅ Cadastro, edição e exclusão de **produtos**
  - ✅ Cadastro, edição e exclusão de **categorias**

---

## 🧪 Tecnologias Utilizadas

- 🐍 Python
- 🌐 Django (com sistema de autenticação nativo)
- 🖼️ Pillow (para gerenciamento de imagens)
- 🧾 HTML e CSS
- 🎨 Bootstrap
- 💨 Tailwind CSS

---

## 🧰 Instalação e Execução

Siga os passos abaixo para executar o projeto localmente:

```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/loja-tc-sports.git

# 2. Acesse a pasta do projeto
cd loja-tc-sports

# 3. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Realize as migrações do banco de dados
python manage.py migrate

# 6. Crie um superusuário para acessar o admin
python manage.py createsuperuser

# 7. Execute o servidor
python manage.py runserver



## 👤 Autor

- **Sanderley Nascimento**
  GitHub: https://github.com/SanderleySilva
  E-mail: sandernascimento98@gmail.com
