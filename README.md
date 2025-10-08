[![Mailing list : test](http://img.shields.io/badge/Email-gray.svg?style=for-the-badge&logo=gmail)](mailto:hello@silero.ai) [![Mailing list : test](http://img.shields.io/badge/Telegram-blue.svg?style=for-the-badge&logo=telegram)](https://t.me/silero_speech) [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=for-the-badge)](https://github.com/snakers4/silero-stress/blob/master/LICENSE) [![downloads](https://img.shields.io/pypi/dm/silero-vad?style=for-the-badge)](https://pypi.org/project/silero-stress/) 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/snakers4/silero-stress/blob/master/silero-stress.ipynb) [![Test Package](https://github.com/snakers4/silero-stress/actions/workflows/test.yml/badge.svg)](https://github.com/snakers4/silero-stress/actions/workflows/test.yml)

![header](https://user-images.githubusercontent.com/12515440/89997349-b3523080-dc94-11ea-9906-ca2e8bc50535.png)

<br/>
<h1 align="center">Silero Stress</h1>
<br/>

**Silero Stress** — pre-trained enterprise-grade automated stress and homograph disambiguation for the Russian language.

<br/>

<p align="center">
  <img src="https://github.com/user-attachments/assets/f2940867-0a51-4bdb-8c14-1129d3c44e64" />
</p>


<br/>

<h2 align="center">Fast start</h2>
<br/>

<details>
<summary>Dependencies</summary>

  System requirements to run python examples on `x86-64` systems:
  
  - `python 3.8+`;
  - 1G+ RAM;
  - A modern CPU with AVX, AVX2, AVX-512 or AMX instruction sets.

  Dependencies:
  
  - `torch>=1.12.0`;

</details>

**Using pip**:
`pip install silero-stress`

```python3
from silero_stress import load_accentor
accentor = load_accentor()
sample_sent = "В недрах тундры выдры в гетрах тырят в ведра ядра кедров."
print(accentor(sample_sent))
```

**Using torch.hub**:
```python3
import torch
torch.set_num_threads(1)

accentor = torch.hub.load(repo_or_dir='snakers4/silero-stress)
sample_sent = "В недрах тундры выдры в гетрах тырят в ведра ядра кедров."
print(accentor(sample_sent))
```

<br/>

<h2 align="center">Key Features</h2>
<br/>

- **Wide coverage**

    Silero Stress covers ~4M Russian known words and word forms with 100% accuracy. It also covers ~2K homographs with F1 score of 0.83, weighted per-word accuracy of 90% and total dataset accuracy of 90%.

- **Fast**

  One ordinary word takes ~1ms to process, one sentence with one homograph takes ~20ms to process.  

- **Lightweight**

  Total package is about 50BM in size, which is ~500x compression ratio, comparing total dictionary and train data size.

- **General**

  Silero Stress was trained on a large dataset, containing ~4M known words and word-forms and ~120M annotated sentences with homographs.

- **Highly Portable**

  Silero Stress reaps benefits from the rich ecosystem built around **PyTorch**.

- **No Strings Attached**

   Published under permissive license (MIT) Silero Stress has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock.

<br/>

<h2 align="center">Typical Use Cases</h2>
<br/>

- Academic research
- Text-to-speech applications
- Telephony and call-center automation, voice bots

<br/>
<h2 align="center">Links</h2>
<br/>


- [Examples and Dependencies](https://github.com/snakers4/silero-vad/wiki/Examples-and-Dependencies#dependencies)
- [Quality Metrics](https://github.com/snakers4/silero-vad/wiki/Quality-Metrics)
- [Performance Metrics](https://github.com/snakers4/silero-vad/wiki/Performance-Metrics)
- [Versions and Available Models](https://github.com/snakers4/silero-vad/wiki/Version-history-and-Available-Models)
- [Further reading](https://github.com/snakers4/silero-models#further-reading)
- [FAQ](https://github.com/snakers4/silero-vad/wiki/FAQ)

<br/>
<h2 align="center">Get In Touch</h2>
<br/>

Try our models, create an [issue](https://github.com/snakers4/silero-stress/issues/new), start a [discussion](https://github.com/snakers4/silero-stress/discussions/new), join our telegram [chat](https://t.me/silero_speech), [email](mailto:hello@silero.ai) us, read our [news](https://t.me/silero_news).

Please see our [wiki](https://github.com/snakers4/silero-models/wiki) for relevant information and [email](mailto:hello@silero.ai) us directly.

**Citations**

```
@misc{Silero Stress,
  author = {Silero Team},
  title = {Silero Stress: pre-trained enterprise-grade automated stress and homograph disambiguation for the Russian language},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/snakers4/silero-stress}},
  commit = {insert_some_commit_here},
  email = {hello@silero.ai}
}
```

**Vocabulary issues**

If you seen any problems with any particular words, please send your examples as an [issue](https://github.com/snakers4/silero-stress/issues/new) or a  [discussion](https://github.com/snakers4/silero-stress/discussions/new).