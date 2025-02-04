import re

LIBRARY_REGEX = re.compile(
    r"import\s+([a-zA-Z0-9_]+)|from\s+([a-zA-Z0-9_]+)\s+import"
)
MODEL_REGEX = re.compile(
    r"(U[-_]?Net|FPN|ResNet|EfficientNet|VGG|YOLO|Mask R-CNN|DenseNet|Inception|SegNet)", 
    re.IGNORECASE
)
CLEANING_REGEX = re.compile(
    r"(dropna|fillna|replace|astype|StandardScaler|MinMaxScaler|OneHotEncoder|SimpleImputer)"
)
ARCHITECTURE_REGEX = re.compile(
    r"(CNN|RNN|LSTM|GRU|Transformer|Autoencoder|GAN|ViT|DNN)", 
    re.IGNORECASE
)
OPTIMIZER_REGEX = re.compile(
    r"(Adam|SGD|RMSprop|Adagrad|Adadelta|AdamW|Nadam)", 
    re.IGNORECASE
)
LOSS_FUNCTION_REGEX = re.compile(
    r"(categorical_crossentropy|binary_crossentropy|MSE|MAE|Huber|Hinge|Dice Loss|IoU Loss)", 
    re.IGNORECASE
)
METRIC_REGEX = re.compile(
    r"(accuracy|precision|recall|f1-score|IoU|Dice Coefficient|AUC|ROC)", 
    re.IGNORECASE
)
AUGMENTATION_REGEX = re.compile(
    r"(ImageDataGenerator|albumentations|random_flip|random_rotation|elastic_transform)", 
    re.IGNORECASE
)
