from collections import Counter
from .regex_patterns import (
    LIBRARY_REGEX, MODEL_REGEX, CLEANING_REGEX, ARCHITECTURE_REGEX, 
    OPTIMIZER_REGEX, LOSS_FUNCTION_REGEX, METRIC_REGEX, AUGMENTATION_REGEX
)
from .standardization import (
    standardize_model, standardize_architecture, standardize_optimizer, 
    standardize_loss, standardize_metric, standardize_augmentation
)

# Initialize counters
libraries = Counter()
models = Counter()
cleaning_techniques = Counter()
architectures = Counter()
optimizers = Counter()
loss_functions = Counter()
metrics = Counter()
augmentations = Counter()

def process_code(code):
    # Extract and update libraries
    libs = set(match.group(1) or match.group(2) 
                for match in LIBRARY_REGEX.finditer(code) 
                if match.group(1) or match.group(2))
    libraries.update(lib.lower() for lib in libs)

    # Extract and update models
    extracted_models = set(standardize_model(m) for m in MODEL_REGEX.findall(code))
    models.update(model.lower() for model in extracted_models)

    # Extract and update cleaning techniques
    cleaning = set(clean.lower() for clean in CLEANING_REGEX.findall(code))
    cleaning_techniques.update(cleaning)

    # Extract and update architectures
    extracted_archs = set(standardize_architecture(a) for a in ARCHITECTURE_REGEX.findall(code))
    architectures.update(arch.lower() for arch in extracted_archs)

    # Extract and update optimizers
    extracted_opts = set(standardize_optimizer(o) for o in OPTIMIZER_REGEX.findall(code))
    optimizers.update(opt.lower() for opt in extracted_opts)

    # Extract and update loss functions
    extracted_losses = set(standardize_loss(l) for l in LOSS_FUNCTION_REGEX.findall(code))
    loss_functions.update(loss.lower() for loss in extracted_losses)

    # Extract and update metrics
    extracted_metrics = set(standardize_metric(m) for m in METRIC_REGEX.findall(code))
    metrics.update(metric.lower() for metric in extracted_metrics)

    # Extract and update augmentations
    extracted_augs = set(standardize_augmentation(a) for a in AUGMENTATION_REGEX.findall(code))
    augmentations.update(aug.lower() for aug in extracted_augs)
