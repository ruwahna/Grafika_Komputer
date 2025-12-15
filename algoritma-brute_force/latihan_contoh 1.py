import matplotlib.pyplot as plt
import math

def draw_line_bruteforce(x1, y1, x2, y2):
    # 1. Pertukaran Titik (Pastikan x1 <= x2)
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        
    # 2A. Kasus Garis Horizontal
    if y1 == y2:
        for x in range(x1, x2 + 1):
            plt.scatter(x, y1, color='blue', s=20)
        return
        
    # 2B. Kasus Garis Vertikal
    if x1 == x2:
        # Pastikan y1 <= y2 sebelum looping
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            plt.scatter(x1, y, color='blue', s=20)
        return

    # 3. Perhitungan Kemiringan (M)
    M = (y2 - y1) / (x2 - x1)
    
    # 4. Iterasi dan Plotting
    for x in range(x1, x2 + 1):
        # Rumus: y = M(x - x1) + y1
        y_float = M * (x - x1) + y1
        y_int = round(y_float)
        
        # Plot piksel yang telah dibulatkan
        plt.scatter(x, y_int, color='blue', s=20)


# PROGRAM UTAMA UNTUK MENJALANKAN FUNGSI

# Pengaturan Plot
plt.figure(figsize=(8, 6))
plt.title("Algoritma Brute Force (Y = MX + C)")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(0, 15) 
plt.ylim(0, 15)
plt.xticks(range(16)) # Tampilkan grid/label integer
plt.yticks(range(16))
plt.grid(True, linestyle='--', alpha=0.6)

# Contoh Pemanggilan
draw_line_bruteforce(2, 2, 12, 7) 

# Tampilkan Plot
plt.show()