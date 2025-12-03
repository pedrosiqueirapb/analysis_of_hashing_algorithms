import pandas as pd
import random
import string
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
data_dir = repo_root / "data"
data_dir.mkdir(exist_ok=True)

output_file = data_dir / "passwords.xlsx"

# -------------------------
# Funções auxiliares
# -------------------------

def weak_password():
    # senhas fracas comuns
    common_list = [
        "123456", "password", "qwerty", "abc123", "111111", "123123",
        "admin", "welcome", "monkey", "letmein", "senha123", "iloveyou"
    ]
    return random.choice(common_list)

def medium_password():
    # senhas médias com padrão palavra+número+símbolo
    words = [
        "House", "Friend", "Brazil", "Nature", "Summer", "Coffee", "Gamer",
        "Work", "Study", "Happy", "Flower", "Shadow"
    ]
    symbols = "!@#$%&*"
    return (
        random.choice(words)
        + str(random.randint(10, 9999))
        + random.choice(symbols)
    )

def strong_password():
    # senhas fortes totalmente aleatórias
    length = random.randint(10, 18)
    chars = (
        string.ascii_letters
        + string.digits
        + "!@#$%&*_-+"
    )
    return "".join(random.choice(chars) for _ in range(length))

# -------------------------
# Gerar 1000 senhas únicas
# -------------------------

passwords = set()

while len(passwords) < 1000:
    r = random.random()
    if r < 0.30:
        pwd = weak_password()
    elif r < 0.70:
        pwd = medium_password()
    else:
        pwd = strong_password()
    
    passwords.add(pwd)

df = pd.DataFrame({"password": list(passwords)})

# remove arquivo anterior
if output_file.exists():
    output_file.unlink()

df.to_excel(output_file, index=False)

print(f"Arquivo '{output_file}' gerado com sucesso!")