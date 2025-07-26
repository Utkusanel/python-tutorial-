#decarotr bir fonksiyonu baska bir fonksiuona arguman olarak verip ciktisini degistiren bu yapidir
def log_decorator(fonksiyon):
    def wrapper():
        print("Fonksiyon çağrılıyor...")
        fonksiyon()
        print("Fonksiyon bitti.")
    return wrapper

@log_decorator
def selamla():
    print("Merhaba!")

selamla()
