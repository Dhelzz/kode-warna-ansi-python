hitam  = "\033[0;30m" 
merah  = "\033[0;31m" 
hijau  = "\033[0;32m" 
kuning = "\033[0;33m" 
putih  = "\033[0;37m" 
kosong = "\033[0m" # warna defult / tanpa warna 
coklat = "\033[0;33m"
biru   = "\033[0;34m"
ungu   = "\033[0;35m"
CYAN = "\033[0;36m"
ABU-ABU MUDA = "\033[0;37m"
ABU-ABU GELAP = "\033[1;30m"
merah muda = "\033[1;31m"
hijau muda = "\033[1;32m"
KUNING = "\033[1;33m"
BIRU MUDA = "\033[1;34m"
UNGU MUDA = "\033[1;35m"
CYAN MUDA = "\033[1;36m"
# kalo yang di bawah buat gaya font
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"

# contoh

print (merah)
print ("contoh teks merah") # dengan memanggil yang diatas
print (f"{kosong}contoh {merah}warna {kuning}yang {hijau}banyak") #contoh memanggil warna yang banyak
print ("\033[0;33mcontoh langsung pakai")
