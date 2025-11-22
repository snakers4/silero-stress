import re
import gzip


supported_langs = ['aze_cyr', 'aze_lat',
                   'uzb_cyr', 'uzb_lat',
                   'bak', 'bel', 'chv',
                   'erz', 'hye', 'kat',
                   'kaz', 'kbd', 'kir',
                   'kjh', 'mdf', 'sah',
                   'tat', 'tgk', 'udm',
                   'xal']


class SimpleAccentor():
    def __init__(self, lang=None):
        
        if lang not in supported_langs:
            raise ValueError(f'Unsupported language "{lang}". Must be in {supported_langs}')

        package_path = "silero_stress.data.vocabularies"

        try:
            import importlib_resources as impresources
        except ImportError:
            from importlib import resources as impresources

        if hasattr(impresources, 'files'):
            # Python 3.9+
            path_to_vocab = str(impresources.files(package_path).joinpath(f'vocab-{lang}.gz'))
        else:
            # Python 3.7-3.8
            with impresources.path(package_path, f'vocab-{lang}.gz') as f:
                path_to_vocab = str(f)

        self.vocab = self._loadvocab(path_to_vocab)
        self.stress_token = '+'
        self.lang = lang

        if lang == "bel":
            alpha = "абвгдежзйклмнопрстуфхцчшыьэюяёіў’"
            vowels = "аоуіэыяеёю"
        if lang == "kir":
            alpha = "абвгдежзийклмнопрстуфхцчшыьэюяёңүө"
            vowels = "аеиоуыэюяёүө"
        if lang == 'aze_cyr':
            alpha = "абвгғдеәжзиыјкҝлмноөпрстуүфхһчҹш'"
            vowels = 'аеәиыоөуү'
        if lang == 'aze_lat':
            alpha = "abcçdeәfgğhxıijkqlmnoöprsştuüvyz'"
            vowels = 'aeәıioöuü'
        if lang == "chv":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяёҫӑӗӳ"
            vowels = "аеиоуыэюяёӑӗӳ"
        if lang == "tat":
            alpha = "абвгдежзийклмнопрстуфхцчшъыьэюяҗңүһәө"
            vowels = "аеиоуыэюяүәө"
        if lang == "bak":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяёғҙҡңҫүһәө"
            vowels = "аеиоуыэюяёүәө"
        if lang == "kjh":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяёіғңҷӧӱ"
            vowels = "аеиоуыэюяёіӧӱ"
        if lang == "kaz":
            alpha = "абвгдежзийклмнопрстуфхцчшщыьэюяіғқңүұһәө"
            vowels = "аеиоуыэюяіүұәө"
        if lang == "hye":
            alpha = "աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօֆև"
            vowels = "աեէըիուօ"
        if lang == "kat":
            alpha = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
            vowels = "აეიოუ"
        if lang == "kbd":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяёӏ"
            vowels = "аеиоуыэюяё"
        if lang == "sah":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяёҕҥүһө"
            vowels = "аеиоуыэюяёүө"
        if lang == "xal":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяҗңүһәө"
            vowels = "аеиоуыэюяүәө"
        if lang == "mdf":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяё"
            vowels = "аеиоуыэюяё"
        if lang == "tgk":
            alpha = "абвгдежзийклмнопрстуфхчшъэюяёғқҳҷӣӯ"
            vowels = "аеиоуэюяёӣӯ"
        if lang == "udm":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяёӝӟӥӧӵ"
            vowels = "аеиоуыэюяёӥӧ"
        if lang == "uzb_cyr":
            alpha = "абдеэфгҳижклмнопқрстувхйзўғшчнгъ"
            vowels = "аеиоуў"
        if lang == "uzb_lat":
            alpha = "abcdefghijklmnopqrstuvxyz'"
            vowels = "aeiou"
        if lang == "chv":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяёҫӑӗӳ"
            vowels = "аеиоуыэюяёӑӗӳ"
        if lang == "erz":
            alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюяё"
            vowels = "аеиоуыэюяё"
                
        alpha = sorted(set(alpha + alpha.upper()))
        self.re_cond =  fr'[^{alpha}]'
        self.vowels = vowels

    def __call__(self, sentence):
        # We are restoring stress in entire sentence, so there is some ugly processing.
        # If you need only vocab, refer to _accentuate_vocab() function
        # If you want to check rules, refer to _accentuate_oov() function
        raw_tokens, clean_tokens, prediction_mask = self._tokenize(sentence)

        accented_sentence = []
        for raw_word, clean_word, need_processing in zip(raw_tokens, clean_tokens, prediction_mask):
            raw_word_lower = raw_word.lower()

            if not need_processing:
                accented_sentence.append(raw_word)
                continue

            have_stress = self.stress_token in raw_word_lower
            if have_stress is True:
                accented_sentence.append(raw_word)
                continue

            if clean_word in self.vocab:
                accented_sentence.append(self._accentuate_vocab(clean_word=clean_word, raw_word=raw_word))
                continue
            else:
                accented_sentence.append(self._accentuate_oov(clean_word=clean_word, raw_word=raw_word))

        return ''.join(accented_sentence)

    def _accentuate_vocab(self, clean_word, raw_word):
        exc_stress = self.vocab[clean_word]
        accentuated_word = raw_word[:exc_stress] + self.stress_token + raw_word[exc_stress:]
        return accentuated_word

    def _accentuate_oov(self, clean_word, raw_word):
        vowel_ids = [i for i, c in enumerate(clean_word) if c in self.vowels]
        if len(vowel_ids) == 0:
            return raw_word

        if len(vowel_ids) == 1:                                 # Single-vowel words - always put stress
            stress_idx = vowel_ids[0]
        elif self.lang == 'kat':                                # "kat" language - algorithm
            if len(vowel_ids) <= 3:
                stress_idx = vowel_ids[0]
            else:
                stress_idx = vowel_ids[len(vowel_ids) - 2]
        elif self.lang in ['mdf', 'erz']:                       # "mdf" / "erz" languages - stress first syllable
            stress_idx = vowel_ids[0]
        elif self.lang == 'bel':                                # "bel" language - stress could be anywhere, we don't know anything about it
            stress_idx = None
        else:                                                   # Stress last syllable for other languages
            stress_idx = vowel_ids[-1] 

        if stress_idx is None:
            return raw_word
        else:
            return raw_word[:stress_idx] + self.stress_token + raw_word[stress_idx:]

    def _tokenize(self, sentence):
        tokens = []
        model_inputs = []
        prediction_mask = []

        for word in re.split(r'(\s+)', sentence):
            parts = word.split('-')

            if len(parts) == 1:
                cur_tokens = parts
                cur_prediction_mask = [True]
            else:
                cur_tokens = [part + '-' for part in parts[:-1]] + [parts[-1]]
                cur_prediction_mask = [True for p in parts[:-1]]

            cur_model_inputs = [re.sub(self.re_cond, '', token.lower()) for token in cur_tokens]
            cur_prediction_mask = [(len(x) > 0) & mask for x, mask in zip(cur_model_inputs, cur_prediction_mask)]

            tokens.extend(cur_tokens)
            model_inputs.extend(cur_model_inputs)
            prediction_mask.extend(cur_prediction_mask)
        return tokens, model_inputs, prediction_mask

    def _loadvocab(self, path_to_vocab):
        with gzip.open(path_to_vocab, 'rb') as f:
            vocab = [x.decode().strip() for x in f.readlines()]
        vocab = {x.rsplit(maxsplit=1)[0]: int(x.rsplit(maxsplit=1)[1]) for x in vocab}
        return vocab
