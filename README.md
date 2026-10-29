<div align="center">

# 📊 InsightView Analytics

### Transforme planilhas em decisões inteligentes.

**Dashboard empresarial em Python com interface gráfica moderna, análise de dados e exportação de relatórios para Excel.**

<br>

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/Interface-CustomTkinter-1F6AA5?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Export-Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Status](https://img.shields.io/badge/Projeto-Em%20desenvolvimento-orange?style=for-the-badge)

</div>

---

## 🚀 Sobre o projeto

O **InsightView Analytics** é uma aplicação desktop desenvolvida em Python para facilitar a análise de dados empresariais por meio de uma interface gráfica moderna, intuitiva e organizada.

A proposta é transformar dados armazenados em planilhas em informações mais claras, permitindo visualizar indicadores, explorar gráficos, aplicar filtros e gerar relatórios em Excel.

O projeto foi pensado para demonstrar conhecimentos em **Python, análise de dados, visualização estatística, automação de relatórios e desenvolvimento de interfaces gráficas**.

## ✨ Dois aplicativos em um projeto

<table>
<tr>
<td width="50%" valign="top">

### 📈 01. InsightView Dashboard

Aplicativo principal para explorar os dados visualmente.

- 📂 Importação de arquivos Excel e CSV
- 📊 Indicadores e gráficos
- 🔎 Filtros para explorar os dados
- 🏢 Detecção de área empresarial
- 🧹 Informações sobre dados ausentes e duplicados
- 🎨 Interface desktop em tema escuro

**Arquivo:** `insightview_app.py`

</td>
<td width="50%" valign="top">

### 📑 02. InsightView Report Studio

Aplicativo independente para preparar e exportar relatórios.

- 📥 Carregamento de planilhas
- 🔍 Visualização de registros e colunas
- 📋 Informações sobre qualidade dos dados
- 📊 Análises conforme as colunas disponíveis
- 📤 Exportação de relatórios para Excel

**Arquivo:** `insightview_report_studio.py`

</td>
</tr>
</table>

## 🖥️ Interface e experiência

O projeto utiliza uma interface em tema escuro, com organização visual voltada à leitura de indicadores e exploração de dados.

> **Objetivo:** tornar a análise de planilhas mais acessível, visual e prática para rotinas empresariais.

*Adicione aqui uma captura de tela real do aplicativo quando estiver disponível.*

```text
docs/
└── screenshots/
    ├── dashboard.png
    └── report-studio.png
```

Depois de adicionar as imagens ao repositório, você pode exibi-las assim:

```markdown
![InsightView Dashboard](docs/screenshots/dashboard.png)
![InsightView Report Studio](docs/screenshots/report-studio.png)
```

## 🏢 Aplicações empresariais

O InsightView pode ser utilizado como base para análises de diferentes áreas, conforme os dados disponíveis na planilha.

| Área | Exemplos de análise |
|---|---|
| 💰 Financeiro | Receitas, despesas e resultados |
| 🛒 Vendas | Faturamento, produtos e desempenho |
| 📦 Estoque | Quantidades e categorias de produtos |
| 👥 Recursos Humanos | Indicadores presentes nas bases de RH |
| 🎯 Marketing | Campanhas e métricas disponíveis |
| ⚙️ Operações | Volumes, registros e indicadores operacionais |

*Os indicadores dependem das colunas existentes nos arquivos importados. Nem todas as métricas estão disponíveis para todas as áreas.*

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| CustomTkinter | Interface gráfica desktop |
| Pandas | Manipulação e análise de dados |
| NumPy | Operações numéricas |
| Matplotlib | Visualização gráfica |
| OpenPyXL | Leitura e geração de arquivos Excel |
| Pillow | Recursos de imagem da interface |
| Pytest | Testes automatizados |

## 📁 Estrutura do projeto

```text
InsightView-Analytics/
│
├── insightview_app.py
├── insightview_report_studio.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── analytics/
│   ├── config/
│   ├── data/
│   ├── export/
│   └── ui/
│
├── samples/
│   ├── exemplo_vendas.csv
│   └── exemplo_vendas.xlsx
│
├── assets/
│   ├── icons/
│   └── images/
│
└── tests/
    ├── test_kpi_engine.py
    └── test_excel_reader.py
```

## ⚙️ Instalação

### 1. Pré-requisitos

- Windows 10 ou Windows 11
- Python 3.11 ou superior
- Git (opcional)
- Visual Studio Code (recomendado)

### 2. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/InsightView-Analytics.git
```

Entre na pasta:

```bash
cd InsightView-Analytics
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative no Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## ▶️ Como executar

### Dashboard principal

```bash
python insightview_app.py
```

### Report Studio

```bash
python insightview_report_studio.py
```

Após abrir o aplicativo, selecione uma planilha `.xlsx`, `.xls` ou `.csv` e explore os dados disponíveis.

> **Observação:** arquivos `.xls` antigos precisam da dependência `xlrd`, incluída no arquivo de dependências deste projeto.

## 📤 Exportação para Excel

O InsightView Report Studio permite selecionar o destino do relatório gerado.

Conforme os dados e os recursos disponíveis, o arquivo pode conter abas como:

- Dashboard
- Dados
- KPIs
- Estatísticas
- Análise por categoria
- Comparação temporal

A composição final depende das colunas encontradas na base carregada.

## 📦 Gerar executáveis para Windows

É possível empacotar os aplicativos como arquivos `.exe` usando PyInstaller.

Instale:

```bash
python -m pip install pyinstaller
```

Gere o executável do Dashboard:

```bash
pyinstaller --noconfirm --clean --windowed --name InsightView-Analytics --add-data "src;src" insightview_app.py
```

Gere o executável do Report Studio:

```bash
pyinstaller --noconfirm --clean --windowed --name InsightView-Report-Studio --add-data "src;src" insightview_report_studio.py
```

Os executáveis serão criados na pasta `dist/`.

*Os comandos devem ser executados no Windows. Recursos adicionais, como ícones e arquivos de configuração, podem exigir ajustes no empacotamento.*

## 🧪 Testes

O projeto inclui testes para componentes de leitura de dados e cálculo de indicadores.

Para executar:

```bash
python -m pytest -v
```

Execute os testes no ambiente local antes de publicar uma versão e informe no README os resultados efetivamente verificados.

## 🔐 Qualidade e confiabilidade dos dados

O projeto busca facilitar a inspeção dos dados importados, incluindo:

- Identificação de valores ausentes
- Contagem de linhas duplicadas
- Estatísticas de colunas numéricas
- Análises condicionadas aos dados disponíveis

Os dados não devem ser considerados automaticamente corretos apenas por terem sido carregados. Recomenda-se conferir os resultados antes de utilizá-los em decisões empresariais.

## 🗺️ Próximas melhorias

- [ ] Adicionar capturas de tela e demonstração em GIF
- [ ] Melhorar os indicadores específicos de cada área
- [ ] Adicionar filtros avançados e seleção de períodos
- [ ] Criar instalador para Windows
- [ ] Adicionar testes de interface e exportação
- [ ] Implementar pipeline de integração contínua
- [ ] Preparar pacote de distribuição com identidade visual

## 👩‍💻 Sobre o desenvolvimento

Este projeto demonstra a aplicação de Python na criação de ferramentas desktop para análise de dados e apoio à tomada de decisão.

**Principais competências demonstradas:**

`Python` · `Pandas` · `Data Analysis` · `Data Visualization` · `CustomTkinter` · `Excel Automation` · `Software Engineering`

## 🤝 Contribuições

Sugestões, melhorias e relatos de problemas são bem-vindos.

1. Faça um fork do projeto.
2. Crie uma branch para sua alteração.
3. Faça commits claros e objetivos.
4. Abra um Pull Request descrevendo as mudanças.

## 📄 Licença

Defina uma licença antes de distribuir ou permitir reutilização do código. Se o projeto ainda não possui uma licença, não presuma que outras pessoas têm autorização para reutilizá-lo.
=======
<p align="center">
  <img src="Banner.jpeg" alt="Banner — Rafaela Sommer" width="100%">
</p>

<h1 align="center">🌟Rafaela Sommer Gonçalves🌟</h1>

---

<p align="center">
  ⚡💻 <b>Desenvolvedora Backend • Engenharia da Computação • Arquitetura de Sistemas & Integração de APIs</b> ⚡
</p>
>>>>>>> 0c6d1a27abebfe4473040f3a69e0173aeb1a0b1c

---

<div align="center">
<<<<<<< HEAD

### ⭐ Gostou do projeto?

Se o InsightView Analytics foi útil ou interessante, considere deixar uma estrela no repositório!

**InsightView Analytics — dados mais claros, decisões melhores.**

</div>
=======
  <img
    src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=C77DFF&center=true&vCenter=true&width=480&lines=Cursando+Engenharia+da+Computação+na+FHO;Transformando+ideias+em+projetos;Localizada+em+Araras+-+SP"
    alt="Typing SVG">
</div>

---

# ✨ Sobre mim

Sou **Rafaela Sommer**, Desenvolvedora Backend focada em criar soluções inteligentes, escaláveis e bem arquitetadas.
Tenho paixão por automação, integrações e eficiência, transformando processos complexos em sistemas simples, rápidos e confiáveis.

Trabalho com foco em performance, organização de código e boas práticas de arquitetura, sempre pensando em crescimento, manutenção e impacto real no negócio.

🚀 **O que eu faço**:

* **Desenvolvimento de APIs** e microserviços escaláveis
* **Automação de processos corporativos** para ganho de produtividade
* **Integrações** entre sistemas e arquitetura de dados
* **Aplicações robustas**, seguras e de alto desempenho
* **Soluções backend** que resolvem problemas e geram eficiência

💡 **Código limpo**, **arquitetura sólida** e **soluções** que funcionam de verdade.

---

# 🛠️ Tecnologias & Ferramentas

## 💻 Linguagens

<img src="https://img.shields.io/badge/Python-8A2BE2?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Java-5A2CA0?style=for-the-badge&logo=openjdk&logoColor=white">
<img src="https://img.shields.io/badge/Node.js-6A0DAD?style=for-the-badge&logo=node.js&logoColor=white">
<img src="https://img.shields.io/badge/C%23-9932CC?style=for-the-badge&logo=csharp&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-BA55D3?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/TypeScript-1565C0?style=for-the-badge&logo=typescript&logoColor=white">
<img src="https://img.shields.io/badge/Go-00ACC1?style=for-the-badge&logo=go&logoColor=white">
<img src="https://img.shields.io/badge/PHP-6A1B9A?style=for-the-badge&logo=php&logoColor=white">
<img src="https://img.shields.io/badge/Ruby-D81B60?style=for-the-badge&logo=ruby&logoColor=white">
<img src="https://img.shields.io/badge/Kotlin-7B1FA2?style=for-the-badge&logo=kotlin&logoColor=white">
<img src="https://img.shields.io/badge/Swift-FF9800?style=for-the-badge&logo=swift&logoColor=white">
<img src="https://img.shields.io/badge/Scala-AB47BC?style=for-the-badge&logo=scala&logoColor=white">
<img src="https://img.shields.io/badge/Rust-212121?style=for-the-badge&logo=rust&logoColor=white">
<img src="https://img.shields.io/badge/Shell-607D8B?style=for-the-badge&logo=gnu-bash&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">

---

## 🏗️ Frameworks

<img src="https://img.shields.io/badge/Django-4B0082?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-9400D3?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/Express-7B1FA2?style=for-the-badge&logo=express&logoColor=white">
<img src="https://img.shields.io/badge/Spring-8E24AA?style=for-the-badge&logo=spring&logoColor=white">
<img src="https://img.shields.io/badge/.NET-512DA8?style=for-the-badge&logo=dotnet&logoColor=white">
<img src="https://img.shields.io/badge/Laravel-FF2968?style=for-the-badge&logo=laravel&logoColor=white">
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black">
<img src="https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white">

---

## 🗄️ Bancos de Dados

<img src="https://img.shields.io/badge/MySQL-7E57C2?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-6A1B9A?style=for-the-badge&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/MongoDB-9C27B0?style=for-the-badge&logo=mongodb&logoColor=white">
<img src="https://img.shields.io/badge/SQLite-AB47BC?style=for-the-badge&logo=sqlite&logoColor=white">
<img src="https://img.shields.io/badge/Redis-A93226?style=for-the-badge&logo=redis&logoColor=white">
<img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black">

---

## ⚙️ DevOps / Infra

<img src="https://img.shields.io/badge/Docker-3B8AC4?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white">
<img src="https://img.shields.io/badge/GitHub%20Actions-7B2CBF?style=for-the-badge&logo=githubactions&logoColor=white">
<img src="https://img.shields.io/badge/Terraform-5A31A5?style=for-the-badge&logo=terraform&logoColor=white">
<img src="https://img.shields.io/badge/Prometheus-FF6F00?style=for-the-badge&logo=prometheus&logoColor=white">
<img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white">

---

## ☁️ Cloud

<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">
<img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white">
<img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white">

---

# 🚀 Projetos em Destaque

<a href="https://github.com/RafaelaSommer/Gerador-de-pastas-e-Excel">
  <img width="450"
       src="https://github-readme-stats.vercel.app/api/pin/?username=RafaelaSommer&repo=Gerador-de-pastas-e-Excel&bg_color=000000&title_color=BD93F9&text_color=F8F8F2&icon_color=BD93F9&hide_border=true" />
</a>

---

## 📊 Atividade no GitHub

<img
src="https://github-readme-stats.vercel.app/api?username=RafaelaSommer&show_icons=true&theme=dracula"
alt="Rafaela Sommer GitHub Stats"
width="100%" />

<img
src="https://github-readme-stats.vercel.app/api/top-langs/?username=RafaelaSommer&layout=compact&theme=dracula"
alt="Top Languages"
width="100%" />

<img
src="https://github-readme-activity-graph.vercel.app/graph?username=RafaelaSommer&bg_color=282a36&color=f8f8f2&line=bd93f9&point=bd93f9&area=true&hide_border=true"
alt="GitHub Activity Graph"
width="100%" />

---

# 🤝 Como Contribuir

Adoramos contribuições! ❤️
Seguindo o fluxo abaixo, você ajuda a manter o projeto organizado, fácil de revisar e agradável para toda a comunidade.

🔁 **Passo a passo**

1️⃣ Faça um fork do repositório

2️⃣ Crie uma nova branch a partir da main:

```bash
git checkout -b feature/nova-feature
```

3️⃣ Implemente sua melhoria com foco em código limpo e boas práticas

4️⃣ Faça commits claros e objetivos, seguindo o padrão:

```bash
git commit -m "feat: descrição clara da mudança"
```

5️⃣ Envie sua branch para o repositório remoto:

```bash
git push origin feature/nova-feature
```

6️⃣ **Abra um Pull Request** 🚀

📝 Ao abrir o Pull Request, descreva:

* ✅ O que foi alterado
* 🎯 O motivo da mudança
* 🧪 Como testar (se aplicável)

✨ **Boas práticas importam**

* Código limpo e legível
* Commits bem descritos
* Respeito e colaboração

💡 Boas práticas + colaboração = projeto evoluindo constantemente

Obrigada por contribuir! 🙌
Cada melhoria faz a diferença 🚀❤️

---

# 📬 Contato

<a href="mailto:camilaerafaelagoncalves@hotmail.com">
  <img src="https://img.shields.io/badge/Email-C77DFF?style=for-the-badge&logo=minutemailer&logoColor=white">
</a>
<a href="https://www.facebook.com/share/17qcYDNHN7/">
  <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white">
</a>
<a href="https://www.instagram.com/rafaelasommerg_16">
  <img src="https://img.shields.io/badge/Instagram-9D4EDD?style=for-the-badge&logo=instagram&logoColor=white">
</a>
<a href="https://www.linkedin.com/in/rafaelasommergonçalves16">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://wa.me/5519971015465">
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white">
</a>

---

⭐ *Se esse conteúdo te ajudou, deixe uma estrela no repositório!* ⭐
# rafaela-sommer-goncalves
>>>>>>> 0c6d1a27abebfe4473040f3a69e0173aeb1a0b1c
