def standardize_model(model):
    model = model.lower().replace("-", "").replace("_", "")
    mapping = {
        "unet": "UNet", "fpn": "FPN", "resnet": "ResNet",
        "vgg": "VGG", "yolo": "YOLO", "maskrcnn": "Mask R-CNN",
        "densenet": "DenseNet", "inception": "Inception", "segnet": "SegNet"
    }
    return mapping.get(model, model)

def standardize_architecture(arch):
    return arch.upper() if arch.lower() in ["cnn", "rnn", "lstm", "gru", "dnn", "gan"] else arch.capitalize()

def standardize_optimizer(opt):
    return opt.upper() if opt.lower() in ["adam", "sgd"] else opt

def standardize_loss(loss):
    loss = loss.lower().replace(" ", "").replace("-", "")
    mapping = {
        "diceloss": "Dice Loss", "iouloss": "IoU Loss",
        "binarycrossentropy": "Binary Crossentropy",
        "categoricalcrossentropy": "Categorical Crossentropy",
        "mse": "MSE", "mae": "MAE", "huber": "Huber", "hinge": "Hinge"
    }
    return mapping.get(loss, loss)

def standardize_metric(metric):
    return metric.capitalize()

def standardize_augmentation(aug):
    return "Albumentations" if aug.lower() == "albumentations" else aug
