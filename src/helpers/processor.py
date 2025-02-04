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
    libs = [match.group(1) or match.group(2) 
            for match in LIBRARY_REGEX.finditer(code) 
            if match.group(1) or match.group(2)]
    libraries.update(libs)
    
    # Extract and update models
    extracted_models = MODEL_REGEX.findall(code)
    standardized_models = [standardize_model(m) for m in extracted_models]
    models.update(standardized_models)
    
    # Extract and update cleaning techniques
    cleaning = CLEANING_REGEX.findall(code)
    cleaning_techniques.update(cleaning)
    
    # Extract and update architectures
    extracted_archs = ARCHITECTURE_REGEX.findall(code)
    standardized_archs = [standardize_architecture(a) for a in extracted_archs]
    architectures.update(standardized_archs)
    
    # Extract and update optimizers
    extracted_opts = OPTIMIZER_REGEX.findall(code)
    standardized_opts = [standardize_optimizer(o) for o in extracted_opts]
    optimizers.update(standardized_opts)
    
    # Extract and update loss functions
    extracted_losses = LOSS_FUNCTION_REGEX.findall(code)
    standardized_losses = [standardize_loss(l) for l in extracted_losses]
    loss_functions.update(standardized_losses)
    
    # Extract and update metrics
    extracted_metrics = METRIC_REGEX.findall(code)
    standardized_metrics = [standardize_metric(m) for m in extracted_metrics]
    metrics.update(standardized_metrics)
    
    # Extract and update augmentations
    extracted_augs = AUGMENTATION_REGEX.findall(code)
    standardized_augs = [standardize_augmentation(a) for a in extracted_augs]
    augmentations.update(standardized_augs)
