import torch
torch.set_num_threads(1)


def load_accentor():
    model_name = 'accentor.pt'
    package_path = "silero_stress.data"

    try:
        import importlib_resources as impresources
    except ImportError:
        from importlib import resources as impresources

    if hasattr(impresources, 'files'):
        # Python 3.9+
        model_file_path = str(impresources.files(package_path).joinpath(model_name))
    else:
        # Python 3.7-3.8
        with impresources.path(package_path, model_name) as f:
            model_file_path = str(f)

    accentor = torch.package.PackageImporter(model_file_path).load_pickle("accentor_models", "accentor")
    quantized_weight = accentor.homosolver.model.bert.embeddings.word_embeddings.weight.data.clone()
    restored_weights = accentor.homosolver.model.bert.scale * (quantized_weight - accentor.homosolver.model.bert.zero_point)
    accentor.homosolver.model.bert.embeddings.word_embeddings.weight.data = restored_weights

    return accentor
