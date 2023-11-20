# FivePersonalityTestAI
### Aluno: Thiago Bittencourt Santana
![ocean-e1584891996382](https://github.com/oThiagoBittencourt/FivePersonalityTestAI/assets/106789198/34ce841d-28f4-4e25-ae6f-f18416cf4fad)

Projeto acadêmico que visa desenvolver, através do uso de `IA(Scikit-Learn)`, o teste das cinco grandes personalidades; com integração de um `front-end(HTML/CSS/JS)` e uma `API Rest utilizando WebFlask`

---

### Index:
<!--ts-->
   * [Data Set e Funcionamento](#data-set-e-funcionamento)
   * [Detalhes](#detalhes)
   * [Front-End e API](#front-end-e-api)
<!--te-->

---

### Data Set e Funcionamento:
- Link: [FivePersonalityDB](https://www.kaggle.com/datasets/tunguz/big-five-personality-test)
- **Número de linhas:** 1015341
- **Número de colunas:** 110
- **Entradas:**
> Os seguintes itens foram apresentados em uma página e cada um foi avaliado em uma escala de cinco pontos usando botões de opção. A ordem na página foi EXT1, AGR1, CSN1, EST1, OPN1, EXT2, etc.
> A escala foi rotulada como 1=Discordo, 3=Neutro, 5=Concordo
- **Saída:**
> Cluster = 0 - Extroversão; 1 - Abertura para experiências; 2 - Agradabilidade; 3 - Conscienciosidade (ou escrupulosidade); 4 - Neuroticismo

---

### Detalhes:
- API Flask
- Algorítmo `KMeans (Clustering)` do Scikit-Learn para o aprendizado de máquina
- Modelo salvo em um `Joblib`
- Arquivo `"requirements.txt"`
```
pip install -r requirements.txt
```
- **Imports:**
```python
# app.py
import joblib
from flask import Flask, request, jsonify
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
```
```python
# training.py
import pandas as pd
import joblib
from sklearn.cluster import KMeans
```
---

### Funcionalidade:
O usuário navegará através das páginas html (páginas de navegação), e através da página teste responderá as 50 perguntas referentes a sua personalidade.

Ao enviar, através do JS, será realizado (após transformar os inputs em Json) um request para a API; a qual, de acordo com as respostas fornecidas para as 50 questões, devolverá após o processamento do modelo de clustering, uma respota de 0 a 4.

O JS então, redirecionará o usuário de acordo com o index da resposta para uma das 5 páginas de resultado.

---

### Front-End e API:
- **Rotas:**
```python
# Páginas de Navegação
@app.route('/')                                # Apresentação sobre o teste (index.html)
@app.route('/teste')                           # Página para a realização do teste (teste.html)
@app.route('/resultado', methods=['POST'])     # Página que consulta a API e de acordo com a resposta redireciona o usuário

# Páginas Respostas
@app.route('/0')    # Página de Resposta: Extroversão (0.html)
@app.route('/1')    # Página de Resposta: Abertura para experiências (1.html)
@app.route('/2')    # Página de Resposta: Agradabilidade (2.html)
@app.route('/3')    # Página de Resposta: Conscienciosidade (ou escrupulosidade) (3.html)
@app.route('/4')    # Página de Resposta: Neuroticismo (4.html)
```
- **Json Format:**
```json
{
    "EXT1": 1, "EXT2": 1, "EXT3": 1, "EXT4": 1, "EXT5": 1, "EXT6": 1, "EXT7": 1, "EXT8": 1, "EXT9": 1, "EXT10": 1,
    "EST1": 1, "EST2": 1, "EST3": 1, "EST4": 1, "EST5": 1, "EST6": 1, "EST7": 1, "EST8": 1, "EST9": 1, "EST10": 1,
    "AGR1": 1, "AGR2": 1, "AGR3": 1, "AGR4": 1, "AGR5": 1, "AGR6": 1, "AGR7": 1, "AGR8": 1, "AGR9": 1, "AGR10": 1,
    "CSN1": 1, "CSN2": 1, "CSN3": 1, "CSN4": 1, "CSN5": 1, "CSN6": 1, "CSN7": 1, "CSN8": 1, "CSN9": 1, "CSN10": 1,
    "OPN1": 1, "OPN2": 1, "OPN3": 1, "OPN4": 1, "OPN5": 1, "OPN6": 1, "OPN7": 1, "OPN8": 1, "OPN9": 1, "OPN10": 1
}
```

- **JavaScript API conexão e redirecionamento:**
```JS
// teste.html
document.getElementById("myForm").addEventListener("submit", function (e) {
            e.preventDefault();
            
            const formData = new FormData(this);

            // Converte os dados do formulário para um objeto JSON
            const jsonData = {};
            formData.forEach((value, key) => {
                jsonData[key] = value;
            });

            // Envia os dados para a API REST
            fetch('http://127.0.0.1:5000/resultado', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            })
            .then(response => response.json())
            .then(data => {
                var result = JSON.stringify(data);
                var x = JSON.parse(result);

                switch (x.personality) {
                    case "0":
                        window.location.replace("http://127.0.0.1:5000/0");
                        break;
                    case "1":
                        window.location.replace("http://127.0.0.1:5000/1");
                        break;
                    case "2":
                        window.location.replace("http://127.0.0.1:5000/2");
                        break;
                    case "3":
                        window.location.replace("http://127.0.0.1:5000/3");
                        break;
                    case "4":
                        window.location.replace("http://127.0.0.1:5000/4");
                        break;
                }
            })
            .catch(error => {
                document.getElementById("responseMessage").textContent = "Erro: " + error.message;
            });
        });
```
