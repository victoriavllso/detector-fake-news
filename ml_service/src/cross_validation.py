from fake_news_dataset import FakeNewsDataset
from bert_model import model_init
from transformers import Trainer
from trainer import compute_metrics, training_args
from sklearn.model_selection import StratifiedKFold
from tokenizer import tokenize_function
from dataset_processing import texts, labels

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


 # --------- treinamento com validação cruzada

for fold, (train_idx, test_idx) in enumerate(skf.split(texts, labels), start=1):
    print(f"\n=== Fold {fold} ===")

    x_train = texts.iloc[train_idx]
    x_test = texts.iloc[test_idx]
    y_train = labels.iloc[train_idx]
    y_test = labels.iloc[test_idx]

    train_encodings = tokenize_function(x_train.tolist())
    test_encodings = tokenize_function(x_test.tolist())

    train_dataset = FakeNewsDataset(train_encodings, y_train)
    test_dataset = FakeNewsDataset(test_encodings, y_test)

    trainer = Trainer(
        model=model_init(),  # modelo por fold
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        compute_metrics=compute_metrics
    )

    trainer.train()