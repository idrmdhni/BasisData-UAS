import mysql.connector
from prettytable import PrettyTable
import os
from datetime import datetime


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "manajemen_hotel"
)

if connection.is_connected:
    print("\nBerhasil Konek\n")

mycursor = connection.cursor()

def kamar():
    mycursor.execute("SELECT * FROM tbl_no_kamar INNER JOIN tbl_kamar ON tbl_no_kamar.id_kamar = tbl_kamar.id_kamar")
    hasil = mycursor.fetchall()
    kolom = [kolom[0] for kolom in mycursor.description]
    tabel = PrettyTable(["No.", " "*4 + "Tipe Kamar" + " "*4, "No. Kamar", "Harga per Malam", "Ketersediaan Kamar"])
    tabel.align[" "*4 + "Tipe Kamar" + " "*4] = "l"
    tabel.align["Harga per Malam"] = "l"
    tabel.align["Ketersediaan Kamar"] = "l"

    for data in range(len(hasil)):
        mata_uang = f"Rp. {(hasil[data][kolom.index('harga_per_malam')]):,}"
        tabel.add_row([
            data + 1,
            hasil[data][kolom.index("tipe_kamar")],
            hasil[data][kolom.index("no_kamar")],
            mata_uang.replace(",", "."),
            hasil[data][kolom.index("ketersediaan_kamar")]
            ])

    return tabel

def tamu():
    global nama_tamu

    nama_tamu = input("Masukkan nama: ")
    jenis_kelamin = input ("Masukkan jenis kelamin: ")
    no_tlp = input ("Masukkan nomor telepon: ")

    sql = "INSERT INTO tbl_tamu (id_tamu,nama_tamu,jenis_kelamin,no_tlp) VALUES (NULL,%s,%s,%s)"
    nilai = (nama_tamu, jenis_kelamin, no_tlp)
    mycursor.execute(sql, nilai)
    #connection.commit()

    #print(f"{mycursor.rowcount} Data berhasil ditambahkan")

def reservasi():
    global checkin
    global checkout
    global tamu_id

    checkin = input("\nMasukkan tanggal checkin (format: tahun-bulan-hari): ")
    checkout = input("Masukkan tanggal checkout (format: tahun-bulan-hari): ")

    sql = "INSERT INTO tbl_reservasi (id_reservasi,id_tamu,id_no_kamar,tgl_checkin,tgl_checkout) VALUES (NULL,%s,%s,%s,%s)"

    mycursor.execute(f"SELECT id_tamu FROM tbl_tamu WHERE nama_tamu='{nama_tamu}'")
    tamu_id_all = mycursor.fetchall()
    tamu_id = tamu_id_all[len(tamu_id_all)-1][0]
    mycursor.execute("SELECT id_no_kamar FROM tbl_no_kamar")
    no_kamar_id = mycursor.fetchall()[int(kmr)-1][0]

    nilai = (tamu_id, no_kamar_id, checkin, checkout)    
    mycursor.execute(sql, nilai)
    mycursor.execute(f"UPDATE tbl_no_kamar SET ketersediaan_kamar = 'Tidak Tersedia' WHERE id_no_kamar={no_kamar_id}")
    #connection.commit()


def pembayaran():
    metode = input("\nMasukkan metode pembayaran (Cash/Transfer): ")

    sql = "INSERT INTO tbl_pembayaran (id_pembayaran,id_reservasi,metode_pembayaran,total_tagihan,tgl_pembayaran) VALUES (NULL,%s,%s,%s,current_timestamp())"

    format = "%Y-%m-%d"
    tgl1 = datetime.strptime(checkin, format)
    tgl2 = datetime.strptime(checkout, format)
    hari = tgl2.date()-tgl1.date()

    mycursor.execute(f"SELECT id_reservasi FROM tbl_reservasi WHERE id_tamu='{tamu_id}'")
    reservasi_id = mycursor.fetchone()[0]
    mycursor.execute("SELECT tbl_kamar.harga_per_malam FROM tbl_no_kamar INNER JOIN tbl_kamar ON tbl_no_kamar.id_kamar = tbl_kamar.id_kamar")
    harga_kamar = mycursor.fetchall()[int(kmr)-1][0]

    total = str(int(hari.days) * int(harga_kamar))
    nilai = (reservasi_id, metode, total)
    mycursor.execute(sql, nilai)
    #connection.commit()

def lihattamu():
    mycursor.execute("SELECT * FROM tbl_tamu")
    hasil = mycursor.fetchall()
    tabel = PrettyTable(["No", " "*4 + "Nama Tamu" + " "*4, "Jenis Kelamin",  " "*2 + "Nomor Telepon" + " "*2])
    tabel.align[" "*4 + "Nama Tamu" + " "*4] = "l"

    for data in range(len(hasil)):
        tabel.add_row([data + 1, hasil[data][1], hasil[data][2], hasil[data][3]])

    return tabel

def lihatresevasi():
    mycursor.execute(
        '''SELECT * FROM tbl_reservasi
        INNER JOIN tbl_tamu ON tbl_reservasi.id_tamu = tbl_tamu.id_tamu
        INNER JOIN tbl_no_kamar ON tbl_reservasi.id_no_kamar = tbl_no_kamar.id_no_kamar'''
                     )
    hasil = mycursor.fetchall()
    kolom = [kolom[0] for kolom in mycursor.description]
    tabel = PrettyTable(["No.", "ID Reservasi", " "*4 + "Nama Tamu" + " "*4, "No. Kamar", "Tanggal Checkin", "Tanggal Checkout"])
    tabel.align[" "*4 + "Nama Tamu" + " "*4] = "l"

    for data in range(len(hasil)):
        tabel.add_row([
            data + 1,
            hasil[data][kolom.index("id_reservasi")],
            hasil[data][kolom.index("nama_tamu")],
            hasil[data][kolom.index("no_kamar")], 
            hasil[data][kolom.index("tgl_checkin")],
            hasil[data][kolom.index("tgl_checkout")]
            ])
    
    return tabel

def lihatpembayaran():
    mycursor.execute("SELECT * FROM tbl_pembayaran INNER JOIN tbl_reservasi ON tbl_pembayaran.id_reservasi = tbl_reservasi.id_reservasi")
    hasil = mycursor.fetchall()
    kolom = [kolom[0] for kolom in mycursor.description]
    tabel = PrettyTable(["No.", "ID Reservasi", "Metode Pembayaran", " "*3 + "Total Tagihan" + " "*3, " Tanggal Pembayaran "])
    tabel.align[" "*3 + "Total Tagihan" + " "*3] = "l"
    tabel.align["Metode Pembayaran"] = "l"

    for data in range(len(hasil)):
        mata_uang = f"Rp. {(hasil[data][kolom.index('total_tagihan')]):,}"
        tabel.add_row([
            data + 1,
            hasil[data][kolom.index("id_reservasi")],
            hasil[data][kolom.index("metode_pembayaran")],
            mata_uang.replace(",", "."),
            hasil[data][kolom.index("tgl_pembayaran")]
            ])
    
    return tabel

while True:
    print("="*30, "Reservasi", "="*30)
    print('''
1. Pesan kamar
2. Lihat kamar yang tersedia
3. Lihat daftar tamu
4. Lihar daftar reservasi
5. Lihat riwayat transaksi
''')
    menu = input("Masukkan Pilihan: ")
    
    if menu == '1':
        os.system('cls')

        tamu()

        print("\nDaftar kamar:")
        print(kamar())
        kmr = input("Masukkan pilihan kamar: ")

        reservasi()
        pembayaran()
        connection.commit()

        input("\nTekan enter untuk melanjutkan")
        os.system('cls')

    elif menu == '2':
        os.system('cls')
        print(kamar())
        input("\nTekan enter untuk melanjutkan")
        os.system('cls')
    
    elif menu == '3':
        os.system('cls')
        print(lihattamu())
        input("\nTekan enter untuk melanjutkan")
        os.system('cls')
    
    elif menu == '4':
        os.system('cls')
        print(lihatresevasi())
        input("\nTekan enter untuk melanjutkan")
        os.system('cls')

    elif menu == '5':
        os.system('cls')
        print(lihatpembayaran())
        input("\nTekan enter untuk melanjutkan")
        os.system('cls')

    elif menu == '6':
        os.system('cls')

        mycursor.execute("SELECT * FROM tbl_tamu")
        hasil = mycursor.fetchall()
        
        for data in range(len(hasil)):
            print(hasil)

        input("\nTekan enter untuk melanjutkan")
        os.system('cls')

    else:
        print("Input tidak valid\n")
        input("Tekan enter untuk melanjutkan")
        os.system('cls')
