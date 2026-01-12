# detector-fake-news: projeto em construção 🚧

## estrutura do projeto

```
detector-fake-news/
├── ml-service/             
│   ├── model/                # Onde o modelo treinado será salvo
│   ├── dataset/                # Onde o modelo treinado será salvo
│   ├── src/
│   │   ├── bert_model.py
│   │   ├── dataset_processing.py
│   │   ├── fake_news_dataset.py
│   │   ├── tokenizer.py
│   │   └── trainer.py
│   └── requirements.txt
├── frontend/             # Frontend TypeScript (React)
│   ├── src/
│   │   ├── components/
│   │   └── services/         # Chamadas de API
│   └── package.json
└── backend/           # (Futuro) Orquestrador Spring Boot

```
## Base de dados

Monteiro R.A., Santos R.L.S., Pardo T.A.S., de Almeida T.A., Ruiz E.E.S., Vale O.A. (2018) Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results. In: Villavicencio A. et al. (eds) Computational Processing of the Portuguese Language. PROPOR 2018. Lecture Notes in Computer Science, vol 11122. Springer, Cham
