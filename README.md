
#  Detector de Fake News (em construção 🚧)

Este projeto tem como objetivo o desenvolvimento de um sistema de detecção automática de fake news em português, utilizando **Processamento de Linguagem Natural (PLN)** e  **deep learning**.
Atualmente, o foco está na construção e treinamento do modelo de classificação.

Esse projeto tem como objetivos futuros:

- Evoluir para classificação multiclasse (Fake, Real, Sensacionalista)

- Incorporar futuramente Visão Computacional para verificação de imagens e vídeos

##  Arquitetura

O projeto se beseia na arquitetura de microserviços, a fim de garantir escalabilidade, facilidade de manutenção e modularidade

## Modelo de machine learning

O modelo utilizado neste projeto é o **BERTimbau Base** (`neuralmind/bert-base-portuguese-cased`), um modelo BERT pré-treinado para a língua portuguesa.

Foi realizado o **fine-tuning** do modelo para a tarefa de classificação binária de notícias, distinguindo entre:

* **Fake news**
* **Notícias verdadeiras**

O BERTimbau Base possui:

* 12 camadas de *encoders*
* arquitetura Transformer
* treinamento prévio em português

## Frontend

O frontend foi desenvolvido com o objetivo de permitir que o usuário insira o texto de uma notícia, envie essa informação para a API e visualize o resultado da classificação de forma clara e intuitiva. Ele atua exclusivamente como camada de interface, sendo responsável por capturar a entrada do usuário, realizar a requisição ao backend e exibir a resposta retornada pelo modelo.
Para isso, as tecnologias utilizadas foram:

- **Axios**: responsável pela realização de requisições HTTP, permitindo a comunicação entre a interface do usuário e o backend.
- **MUI (Material UI)**: biblioteca de componentes para React que fornece uma interface consistente, acessível e reutilizável, facilitando a construção de layouts e formulários.

## Backend

Esse módulo foi estabelecido com a responsabilidade de intermediar a comunicação entre o frontend e o modelo de Machine Learning. Ele recebe as requisições HTTP contendo o texto a ser analisado, realiza as validações necessárias, aciona o serviço de inferência e retorna a predição em formato estruturado. Além disso, concentra responsabilidades relacionadas à persistência de dados, como o armazenamento do histórico de consultas, e aspectos de segurança da aplicação.

## Base de dados

A base de dados utilizada é um **corpus em português para detecção de fake news**, amplamente utilizado na literatura acadêmica.


> Monteiro, R. A., Santos, R. L. S., Pardo, T. A. S., de Almeida, T. A., Ruiz, E. E. S., & Vale, O. A. (2018).
> *Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results.*
> In: Villavicencio A. et al. (eds) **Computational Processing of the Portuguese Language (PROPOR 2018)**.
> Lecture Notes in Computer Science, vol 11122. Springer, Cham.


