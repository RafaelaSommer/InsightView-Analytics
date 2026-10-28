
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

---

<div align="center">

### ⭐ Gostou do projeto?

Se o InsightView Analytics foi útil ou interessante, considere deixar uma estrela no repositório!

**InsightView Analytics — dados mais claros, decisões melhores.**

</div>
