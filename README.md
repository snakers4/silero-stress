[![Mailing list : test](http://img.shields.io/badge/Email-gray.svg?style=for-the-badge&logo=gmail)](mailto:hello@silero.ai) [![Mailing list : test](http://img.shields.io/badge/Telegram-blue.svg?style=for-the-badge&logo=telegram)](https://t.me/silero_speech) [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=for-the-badge)](https://github.com/snakers4/silero-stress/blob/master/LICENSE)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/snakers4/silero-stress/blob/master/silero-stress.ipynb) [![Open In Colab](https://img.shields.io/github/repo-size/snakers4/silero-stress)](https://github.com/snakers4/silero-stress) 

![header](https://user-images.githubusercontent.com/12515440/89997349-b3523080-dc94-11ea-9906-ca2e8bc50535.png)

<br/>
<h1 align="center">Silero Stress</h1>
<br/>

**Silero Stress** — pre-trained enterprise-grade automated stress and homograph disambiguation for the Russian language.

For 19 other languages please refer [here](https://github.com/snakers4/silero-stress/wiki/Other-Languages).

<br/>

<p align="center">
  <img alt="metrics_histogram" src="https://github.com/user-attachments/assets/a9f7f5ea-e322-4028-93d8-160714d568be" />
</p>


<br/>

<h2 align="center">Fast start</h2>
<br/>

<details>
<summary>Dependencies</summary>

  System requirements to run python examples on `x86-64` systems:
  
  - `python 3.10+`;
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
sample_sent = "Меня зовут Лева Королев. Я из готов. И я уже готов открыть все ваши замки любой сложности!"
print(accentor(sample_sent))
# Мен+я зов+ут Л+ёва Корол+ёв. +Я +из г+отов. +И +я уж+е гот+ов откр+ыть вс+е в+аши замк+и люб+ой сл+ожности!
```

**Using torch.hub**:
```python3
import torch
torch.set_num_threads(1)

accentor = torch.hub.load(repo_or_dir='snakers4/silero-stress',
                          model='silero_stress')
sample_sent = "Меня зовут Лева Королев. Я из готов. И я уже готов открыть все ваши замки любой сложности!"
print(accentor(sample_sent))
# Мен+я зов+ут Л+ёва Корол+ёв. +Я +из г+отов. +И +я уж+е гот+ов откр+ыть вс+е в+аши замк+и люб+ой сл+ожности!
```

For some configuration tips refer to [Configuration](https://github.com/snakers4/silero-stress/wiki/Configuration) wiki page.

You can:
- Use CPU/GPU version;
- Use flags to customize word stress / `ё` placements;
- Use common accentor and homosolver independently.

<br/>

<h2 align="center">Key Features</h2>
<br/>

- **Wide coverage**

  Silero Stress covers ~4M known Russian words and word forms with 100% accuracy. It also covers ~2K homographs with F1 score of 0.85, per-word accuracy of 91% and total dataset accuracy of 93%.

- **Fast**

  On 1 CPU thread every ordinary word takes ~0.5ms to process, every 400-char sentence with two homographs (common prod case) takes ~30ms.  

- **Lightweight and portable**

  Total package is about 50MB in size, boasting ~400x compression ratio.

- **General and generalizable**

  Silero Stress was trained on a large dataset, containing ~4M known words and word forms and ~120M annotated sentences with homographs. It also works with unknown (and invented) words with 60-70% accuracy.

- **No Strings Attached**

   Published under permissive license (MIT) Silero Stress has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock.

- **Minimal and minified**

   Code bloat, unnecessary dependencies and libraries are removed. Silero Stress depends only on PyTorch as a neural engine and the Python standard library.

- **Other Languages**

   We also released `ukr` and `bel` accentors (without homographs) and some vocabularies for `another 18 languages`. Check our [wiki](https://github.com/snakers4/silero-stress/wiki/Other-Languages) for details.

<br/>

<h2 align="center">Typical Use Cases</h2>
<br/>

- Academic research
- Text-to-speech applications
- Telephony and call-center automation, voice bots

<br/>
<h2 align="center">Links</h2>
<br/>

- [Quality Metrics](https://github.com/snakers4/silero-stress/wiki/Quality-Metrics)
- [Performance Metrics](https://github.com/snakers4/silero-stress/wiki/Performance-Metrics)
- [Homograph List](https://github.com/snakers4/silero-stress/wiki/Homograph-List)
- [Further reading](https://github.com/snakers4/silero-models#further-reading)

<br/>
<h2 align="center">Get In Touch</h2>
<br/>

Try our models, create an [issue](https://github.com/snakers4/silero-stress/issues/new), start a [discussion](https://github.com/snakers4/silero-stress/discussions/new), join our telegram [chat](https://t.me/silero_speech), [email](mailto:hello@silero.ai) us, read our [news](https://t.me/silero_news).

Please see our [wiki](https://github.com/snakers4/silero-stress/wiki) for relevant information and [email](mailto:hello@silero.ai) us directly.

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

<br/>
<h2 align="center">Vocabulary issues</h2>
<br/>

If you see any problems with any particular words, please send your examples as an [issue](https://github.com/snakers4/silero-stress/issues/new) or a [discussion](https://github.com/snakers4/silero-stress/discussions/new).
