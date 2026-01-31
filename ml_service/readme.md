## Arquitetura alto nível

```
Texto da notícia
        ↓
Tokenizer BERT
        ↓
BERT pré-treinado
        ↓
Camada de classificação
        ↓
Probabilidade Fake / Real
```

## Comparação entre os folds obtidos no cross-validation

```bash

| Fold | F1-macro   |
| ---- | ---------- |
| 1    | **0.9858** |
| 2    | **0.9528** |
| 3    | **0.9765** |
| 4    | **0.9921** |
| 5    | **0.9830** |

```