dependencies = ['torch']
import os
import torch


def silero_stress(lang='ru'):
    """Silero Stress: automated stress and homograph disambiguation
    Returns a package with pre-built utils
    Please see https://github.com/snakers4/silero-stress for usage examples

    Params  
    lang: str - accentor language ('ru' or 'ukr' or 'bel')
    """
    if lang not in ['ru', 'ukr', 'bel']:
        print(f'Wrong language {lang}. Must be in ["ru", "ukr", "bel"].')
    model_name = 'accentor.pt' if lang == 'ru' else f'accentor-{lang}.pt'
    package_path = os.path.join(os.path.dirname(__file__), 'src', 'silero_stress', 'data', model_name)
    accentor = torch.package.PackageImporter(package_path).load_pickle("accentor_models", "accentor")
    if lang == 'ru':
        quantized_weight = accentor.homosolver.model.bert.embeddings.word_embeddings.weight.data.clone()
        restored_weights = accentor.homosolver.model.bert.scale * (quantized_weight - accentor.homosolver.model.bert.zero_point)
        accentor.homosolver.model.bert.embeddings.word_embeddings.weight.data = restored_weights
    else:
        quantized_weight = accentor.accentor.model.embedding.weight.data.clone()
        restored_weights = accentor.accentor.model.scale * (quantized_weight - accentor.accentor.model.zero_point)
        accentor.accentor.model.embedding.weight.data = restored_weights
    return accentor