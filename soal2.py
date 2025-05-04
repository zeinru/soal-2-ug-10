def tampilkan_soal(nama_file):
    print(f"nama file1: {nama_file}")
    
    try:
        with open(nama_file, 'r') as file:
            for line in file:
                if '||' in line:
                    bagian = line.strip().split('||')
                    soal = bagian[0].strip()
                    jawaban_benar = bagian[1].strip().lower()

                    print(soal)
                    jawaban_user = input("Jawab: ").strip().lower()

                    if jawaban_user == jawaban_benar:
                        print("Jawaban benar!\n")
                    else:
                        print("Jawaban salah!\n")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")

tampilkan_soal('soal.txt')
