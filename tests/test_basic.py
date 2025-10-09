from silero_stress import load_accentor
import torch
torch.set_num_threads(1)

def test_accentor():
    accentor = load_accentor()
    for text in ['Привет, я текст без омографов.',
                 'Меня зовут Лева Королев. Я из готов. И я уже готов открыть все ваши замки любой сложности!']:
        accented_text = accentor(text)
        assert '+' in accented_text
