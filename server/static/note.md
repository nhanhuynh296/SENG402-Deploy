| Syntax                            |                  Description                   | Notes                |
|:----------------------------------|:----------------------------------------------:|:---------------------|
| VGG16_golden_binary_finetune      | val_loss: 0.4605 - val_binary_accuracy: 0.7500 | Always stays at 0.75 |
| VGG16_golden_binary               | val_loss: 0.1065 - val_binary_accuracy: 1.0000 ||
| VGG16_golden_categorical_finetune |    val_loss: 0.6462 - val_accuracy: 0.7500     | Always stays at 0.75 |
| VGG16_golden_categorical          |    val_loss: 0.0394 - val_accuracy: 1.0000l    |
| EfficientnetB4_golden_categorical |    val_loss: 0.0013 - val_accuracy: 1.0000     |
| EfficientnetB4_golden_binary      | val_loss: 0.1565 - val_binary_accuracy: 1.0000 ||

## EfficientnetB4_golden_binary

```
              precision    recall  f1-score   support

         0.0     0.9848    0.6512    0.7840      1786
         1.0     0.7153    0.9886    0.8300      1583

    accuracy                         0.8097      3369
   macro avg     0.8500    0.8199    0.8070      3369
weighted avg     0.8581    0.8097    0.8056      3369
```

## EfficientnetB4_golden_categorical

## VGG16_golden_binary

```
              precision    recall  f1-score   support

         0.0     0.9341    0.5241    0.6714      1786
         1.0     0.6409    0.9583    0.7681      1583

    accuracy                         0.7281      3369
   macro avg     0.7875    0.7412    0.7198      3369
weighted avg     0.7963    0.7281    0.7169      3369
```

## VGG16_golden_categorical

# Compare

|     Reference      |   Architecture    | Transfer learning |      Dataset (G/ B)      | Accuracy (%) | Nathan Model |
|:------------------:|:-----------------:|:-----------------:|:------------------------:|:------------:|:------------:|
|    Saha et. al     |      AlexNet      |        Yes        | 7,000 images (~96% good) |     100      |
|  Sun et al. [60]   | GoogleNet & VGG16 |        Yes        | 5,064 images (2692/2372) |    97.12     |
| Costa et al. [61]  |        CNN        |        No         |     DRIMDB (125/69)      |     100      |
|                    |        VGG        |        Yes        |                          |    90.47     |
|  Zago et al. [62]  |   Inception-V3    |        Yes        |     DRIMDB (125/69)      |    98.55     |
|                    |                   |                   |   ELSA-Brasil (817/25)   |     94.0     |
| Coyner et al. [63] |   Inception-V3    |        Yes        |   6,139 (~50.8% good)    |    88.75     |
|  Wang et al. [64]  |       VGG16       |        Yes        |     DRIMDB (125/69)      |     97.2     |
|                    |                   |                   |     DR1 (1300/1392)      |     98.2     |


# Our database
## Model full
```
             precision    recall  f1-score   support
           0       0.98      0.93      0.95      1786
           1       0.93      0.97      0.95      1583
    accuracy                           0.95      3369
   macro avg       0.95      0.95      0.95      3369
weighted avg       0.95      0.95      0.95      3369
```

## EfficientnetB4_golden_binary
```
              precision    recall  f1-score   support

           0       0.98      0.65      0.78      1786
           1       0.72      0.99      0.83      1583

    accuracy                           0.81      3369
   macro avg       0.85      0.82      0.81      3369
weighted avg       0.86      0.81      0.81      3369
```

## VGG16_golden_binary
```
              precision    recall  f1-score   support

           0       0.93      0.52      0.67      1786
           1       0.64      0.96      0.77      1583

    accuracy                           0.73      3369
   macro avg       0.79      0.74      0.72      3369
weighted avg       0.80      0.73      0.72      3369
```

# DRIMDB
## EfficientnetB4_golden_binary
```
              precision    recall  f1-score   support

           0       0.93      0.84      0.89       376
           1       0.76      0.89      0.82       208

    accuracy                           0.86       584
   macro avg       0.85      0.87      0.85       584
weighted avg       0.87      0.86      0.86       584
```
## VGG16_golden_binary
```
              precision    recall  f1-score   support

           0       0.76      0.88      0.82       376
           1       0.70      0.50      0.59       208

    accuracy                           0.75       584
   macro avg       0.73      0.69      0.70       584
weighted avg       0.74      0.75      0.74       584
```
## VGG16 (model full)
```              
              precision    recall  f1-score   support

           0       0.38      1.00      0.55       208
           1       1.00      0.10      0.19       376

    accuracy                           0.42       584
   macro avg       0.69      0.55      0.37       584
weighted avg       0.78      0.42      0.32       584
```
    

