
#  Detector de Fake News (em construção 🚧)

Este projeto tem como objetivo o desenvolvimento de um **sistema de detecção automática de fake news em português**, utilizando **aprendizado de máquina** e **Processamento de Linguagem Natural (PLN)**.
Atualmente, o foco está na construção e treinamento do modelo de classificação.



##  Estrutura base do projeto

```text
detector-fake-news/
├── ml-service/                    # Serviço de Machine Learning
│   ├── model/                     # Modelos treinados e checkpoints
│   ├── dataset/                   # Conjunto de dados (fake e verdadeiras)
│   ├── src/        			   # Scripts de configuração e treinamento
│   └── requirements.txt           
│
├── frontend/                      #  Em andamento
├── backend/                       # (A fazer) Backend em Kotlin + Spring Boot
└── README.md
```


## Modelo

O modelo utilizado neste projeto é o **BERTimbau Base** (`neuralmind/bert-base-portuguese-cased`), um modelo BERT pré-treinado para a língua portuguesa.

Foi realizado o **fine-tuning** do modelo para a tarefa de **classificação de notícias**, distinguindo entre:

* **Fake news**
* **Notícias verdadeiras**
* **Sensacionalista**

O BERTimbau Base possui:

* 12 camadas de *encoders*
* arquitetura Transformer
* treinamento prévio em português

## Frontend

No frontend, foram utilizadas as seguintes bibliotecas:

- **Axios**: responsável pela realização de requisições HTTP, permitindo a comunicação entre a interface do usuário e o serviço de Machine Learning.
- **MUI (Material UI)**: biblioteca de componentes para React que fornece uma interface consistente, acessível e reutilizável, facilitando a construção de layouts e formulários.

## Backend

** A fazer

## Base de dados

A base de dados utilizada é um **corpus em português para detecção de fake news**, amplamente utilizado na literatura acadêmica.


> Monteiro, R. A., Santos, R. L. S., Pardo, T. A. S., de Almeida, T. A., Ruiz, E. E. S., & Vale, O. A. (2018).
> *Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results.*
> In: Villavicencio A. et al. (eds) **Computational Processing of the Portuguese Language (PROPOR 2018)**.
> Lecture Notes in Computer Science, vol 11122. Springer, Cham.


