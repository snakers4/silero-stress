dependencies = ['torch']
import os
import sys
import torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from silero_stress.accentor import load_accentor


def silero_stress():
    """Silero Stress: automated stress and homograph disambiguation
    Returns a package with pre-built utils
    Please see https://github.com/snakers4/silero-stress for usage examples
    """

    package_path = os.path.join(os.path.dirname(__file__), 'src', 'silero_stress', 'data', 'accentor.pt')
    accentor = torch.package.PackageImporter(package_path).load_pickle("accentor_models", "accentor")
    quantized_weight = accentor.homosolver.model.bert.embeddings.word_embeddings.weight.data.clone()
    restored_weights = accentor.homosolver.model.bert.scale * (quantized_weight - accentor.homosolver.model.bert.zero_point)
    accentor.homosolver.model.bert.embeddings.word_embeddings.weight.data = restored_weights
    return accentor