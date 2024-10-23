import hashlib

def hash_password(password):
    # SHA-256 hash fonksiyonunu kullanarak parolayı şifreliyoruz
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def save_user(username, hashed_password):
    # Kullanıcı adı ve şifreyi bir dosyaya kaydet
    with open("users.txt", "a") as file:   #append mode
        file.write(f"{username}:{hashed_password}\n")
    print("Kullanıcı başarıyla kaydedildi.")

def register():
    # Kullanıcıdan kayıt bilgilerini al
    username = input("Kullanıcı adınızı girin: ")
    password = input("Parolanızı girin: ")

    # Parolayı şifrele ve kullanıcıyı kaydet
    hashed_password = hash_password(password)
    save_user(username, hashed_password)

def login():
    # Kullanıcıdan giriş bilgilerini al
    username = input("Kullanıcı adınızı girin: ")
    password = input("Parolanızı girin: ")

    # Kullanıcı adı ve parolayı kontrol et
    with open("users.txt", "r") as file:          #read mode
        for line in file:
            stored_username, stored_hashed_password = line.strip().split(":")
            if stored_username == username:
                # Kullanıcı adı eşleşti, girdiği parolayı kontrol et
                if hash_password(password) == stored_hashed_password:
                    print("Parola doğru. Giriş başarılı!")
                else:
                    print("Hatalı parola. Lütfen tekrar deneyin.")
                return
        print("Kullanıcı bulunamadı.")

# Kayıt olma veya giriş yapma seçeneklerini sun

while True:
    choice = input("Kayıt olmak için 'k', giriş yapmak için 'g' girin (çıkış için 'q'): ")

    if choice.lower() == 'k':
        register()
    elif choice.lower() == 'g':
        login()
    elif choice.lower() == 'q':
        print("Programdan çıkılıyor.")
        break  # Döngüyü sonlandır
    else:
        print("Geçersiz seçenek. Lütfen 'k', 'g' veya 'q' girin.")