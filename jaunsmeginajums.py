# Atver failu pievienošanas režīmā
file = open("data.txt", "a", encoding="UTF-8")

# Nosaka, kur beidzas esošais teksts failā
# Lasām failu, lai iegūtu kopējo rindu skaitu
with open("data.txt", "r", encoding="UTF-8") as read_file:
    lines = read_file.readlines()
    line_count = len(lines) + 1  # Pievieno 1, lai sāktu no nākamās rindas numura

# Sagatavo tekstu ar rindas numuru
text = f'Rinda {line_count}\n'

# Pievieno tekstu failam
file.write(text)

# Aizver failu
file.close()