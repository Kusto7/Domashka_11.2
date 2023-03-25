def func_upp_text(text: str):
    """Возвращает текст заглавными буквами"""
    return text.upper()


def func_upp_first_letter(text: str):
    """Возвращает заглавные буквы каждого слова"""
    return text.title()

if __name__ == "__main__":
    func_upp_text("YES, I'm")
    func_upp_first_letter("Yes Yes Yes")
