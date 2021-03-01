from collections import defaultdict

#Menghapus tanda . , \n menjadi kosong
def extract_line(line: str) ->list:
    return line.strip().replace(".", "").replace(" ", "").split(",")

#Menghapus Node jika sudah dikunjungi
def remove_node(prasyarat, node):
    for k in prasyarat.keys():
        if node in prasyarat[k]:
            prasyarat[k].remove(node)
    prasyarat.pop(node, None)
    return prasyarat

#Print dimulai dari kode kuliah yang memiliki in degree 0
def t_sort(prasyarat,smst):
    all_zero = True

    for k, v in prasyarat.items():
        all_zero = all_zero and (len(v) == 0)

    if all_zero:
        # saat ini, prasyarat hanya memiliki 1 key terakhir
        for k in prasyarat.keys():
            print("Semester ", smst+1,k)
        return

    for k, v in prasyarat.items():
        if len(v) == 0:
            smst += 1
            print("Semester " ,smst, k)
            prasyarat = remove_node(prasyarat, k)
            break
    t_sort(prasyarat,smst)

#Fungsi main untuk menjalankan program. 
def main():
    #Membuka dan membaca teks dari txt.
    file1 = open('test8.txt', 'r')
    Lines = file1.readlines()
    smst = 0
    prasyarat = defaultdict()
    #dengan menggunakan fungsi extract_line, karakter , . \n telah dihapus

    for line in Lines:
        kuliah = extract_line(line)

        prasyarat[kuliah[0]] = kuliah[1:]
    
    t_sort(prasyarat,smst)



if __name__ == "__main__":
    main()
