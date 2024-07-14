import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
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

root = tk.Tk()
root.geometry("800x600")
root.title("Manajemen Hotel")

color1 = "#ADB5BD"
color2 = "#DEE2E6"
color3 = "white"

option_frame = tk.Frame(root, bg=color1)
option_frame.pack(side=tk.LEFT, fill="y")
option_frame.pack_propagate(False)
option_frame.configure(width=160, height=600)

list_frame = tk.Frame(root, bg=color3)
list_frame.pack(side=tk.LEFT, fill="y")
list_frame.configure(width=3)

main_frame = tk.Frame(root, bg=color2)
main_frame.pack(side=tk.LEFT, fill="both", expand=True)

style = ttk.Style(main_frame)
style.theme_use('default')
style.configure("Treeview", background=color2, fieldbackground=color2, font=("Arial", 11))
style.configure("Treeview.Heading", background=color1, font=("Arial", 11, "bold"))

def reset():
    for widget in main_frame_child.winfo_children():
        if isinstance(widget, tk.Entry): # If this is an Entry widget class
            widget.delete(0,'end')   # delete all entries 
        if isinstance(widget,ttk.Combobox):
            widget.delete(0,'end') 
        if isinstance(widget,tk.Text):
            widget.delete('1.0','end') # Delete from position 0 till end 
        if isinstance(widget,tk.Checkbutton):
            widget.deselect()
        if isinstance(widget,tk.Radiobutton):
            gender.set(None)
            payment.set(None)

def submit_data():
    name = entry_name.get()
    phone_number = entry_phone_number.get()
    room_type = combobox_room_type.get()
    room_number = combobox_room_number.get()
    checkin = cal_checkin.get()
    checkout = cal_checkout.get()
    
    tamu = "INSERT INTO tbl_tamu (id_tamu,nama_tamu,jenis_kelamin,no_tlp) VALUES (NULL,%s,%s,%s)"
    tamu_values = (name, gendervalue(), phone_number)
    mycursor.execute(tamu, tamu_values)

    reservasi = "INSERT INTO tbl_reservasi (id_reservasi,id_tamu,id_no_kamar,tgl_checkin,tgl_checkout) VALUES (NULL,%s,%s,%s,%s)"
    mycursor.execute(f"SELECT id_tamu FROM tbl_tamu WHERE nama_tamu='{name}'")
    tamu_id_all = mycursor.fetchall()
    tamu_id = tamu_id_all[len(tamu_id_all)-1][0]
    mycursor.execute(f"SELECT id_no_kamar FROM tbl_no_kamar WHERE no_kamar='{room_number}'")
    no_kamar_id = mycursor.fetchone()[0]
    reservasi_values = (tamu_id, no_kamar_id, checkin, checkout)    
    mycursor.execute(reservasi, reservasi_values)
    mycursor.execute(f"UPDATE tbl_no_kamar SET ketersediaan_kamar = 'Tidak Tersedia' WHERE id_no_kamar='{no_kamar_id}'")

    pembayaran = "INSERT INTO tbl_pembayaran (id_pembayaran,id_reservasi,metode_pembayaran,total_tagihan,tgl_pembayaran) VALUES (NULL,%s,%s,%s,current_timestamp())"
    format = "%Y-%m-%d"
    tgl1 = datetime.strptime(checkin, format)
    tgl2 = datetime.strptime(checkout, format)
    hari = tgl2.date()-tgl1.date()
    mycursor.execute(f"SELECT id_reservasi FROM tbl_reservasi WHERE id_tamu='{tamu_id}'")
    reservasi_id = mycursor.fetchone()[0]
    mycursor.execute(f"SELECT harga_per_malam FROM tbl_kamar WHERE tipe_kamar='{room_type}'")
    harga_kamar = mycursor.fetchone()[0]
    total = str(int(hari.days) * int(harga_kamar))
    pembayaran_values = (reservasi_id, payment_value(), total)
    mycursor.execute(pembayaran, pembayaran_values)

    connection.commit()
    reset()
    
    messagebox.showinfo("Status", "Data berhasil di input")

def pesan_kamar_page():
    global entry_name
    global entry_phone_number
    global combobox_room_number
    global combobox_room_type
    global cal_checkin
    global cal_checkout
    global gendervalue
    global payment_value
    global gender
    global payment
    global main_frame_child

    main_frame_child = tk.LabelFrame(main_frame,
                                 text=" Pesan Kamar ",
                                 font=("Montserrat", 12, "bold"),
                                 labelanchor="n",
                                 bg=color2)
    main_frame_child.pack()
    main_frame_child.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    main_frame_child.configure(height=500, width=400)
    main_frame_child.pack_propagate(False)

    label_name = tk.Label(main_frame_child, text="Nama: ", font=("Arial", 11), bg=color2)
    entry_name = tk.Entry(main_frame_child, width=35)
    label_name.pack()
    entry_name.pack()
    label_name.place(x=30, y=27)
    entry_name.place(x=140, y=30)

    label_phone_number = tk.Label(main_frame_child, text="No. Telepon: ", font=("Arial", 11), bg=color2)
    entry_phone_number = tk.Entry(main_frame_child, width=35)
    label_phone_number.pack()
    entry_phone_number.pack()
    label_phone_number.place(x=30, y=67)
    entry_phone_number.place(x=140, y=70)

    def gendervalue():
        return gender.get()
    gender = tk.StringVar(value="1")
    label_gender = tk.Label(main_frame_child, text="Jenis Kelamin: ", font=("Arial", 11), bg=color2)
    rb_gender_lk = tk.Radiobutton(main_frame_child, text="Laki-Laki", variable=gender, value="Laki-Laki", font=("Arial", 11), bg=color2, command=gendervalue)
    rb_gender_pr = tk.Radiobutton(main_frame_child, text="Perempuan", variable=gender, value="Perempuan", font=("Arial", 11), bg=color2, command=gendervalue)
    rb_gender_pr.pack()
    label_gender.pack()
    rb_gender_lk.pack()
    label_gender.place(relx=0.5, y=110, anchor=tk.CENTER)
    rb_gender_lk.place(x=100, y=125)
    rb_gender_pr.place(x=200, y=125)

    mycursor.execute("SELECT tipe_kamar FROM tbl_kamar")
    room_type = mycursor.fetchall()
    room_type_options = [i[0] for i in room_type]
    room_type_selected = tk.StringVar(main_frame_child)
    room_type_selected.set(room_type_options[0])

    label_room_type = tk.Label(main_frame_child, text="Tipe Kamar: ", font=("Arial", 11), bg=color2)
    combobox_room_type = ttk.Combobox(main_frame_child, values=room_type_options, font=("Arial", 10))
    label_room_type.pack()
    combobox_room_type.pack()
    label_room_type.place(x=30, y=162)
    combobox_room_type.place(x=140, y=165)

    def id_kamar_value():
        if combobox_room_type.get() != "":
            mycursor.execute(f"SELECT id_kamar FROM tbl_kamar WHERE tipe_kamar='{combobox_room_type.get()}'")
            result = mycursor.fetchone()[0]
            return result

    button_room_type = tk.Button(main_frame_child, text="Pilih", font=("Arial", 11), bg=color1, command=id_kamar_value)
    button_room_type.pack()
    button_room_type.place(x=140, y =190)

    def no_kamar_values():
        mycursor.execute(f"SELECT no_kamar FROM tbl_no_kamar WHERE id_kamar='{id_kamar_value()}' AND ketersediaan_kamar='Tersedia'")
        number_room = mycursor.fetchall()
        number_room_options = [i[0] for i in number_room]
        combobox_room_number["values"] = number_room_options

    label_room_number = tk.Label(main_frame_child, text="Nomor Kamar: ", font=("Arial", 11), bg=color2)
    combobox_room_number = ttk.Combobox(main_frame_child, font=("Arial", 10), postcommand=no_kamar_values)
    label_room_number.pack()
    combobox_room_number.pack()
    label_room_number.place(x=30, y=232)
    combobox_room_number.place(x=140, y=235)

    label_checkin = tk.Label(main_frame_child, text="Check-in: ", font=("Arial", 11), bg=color2)
    label_checkout = tk.Label(main_frame_child, text="Check-out: ", font=("Arial", 11), bg=color2)
    cal_checkin = DateEntry(main_frame_child, date_pattern="yyyy-mm-dd")
    cal_checkout = DateEntry(main_frame_child, date_pattern="yyyy-mm-dd")
    label_checkin.pack()
    label_checkout.pack()
    cal_checkin.pack()
    cal_checkout.pack()
    label_checkin.place(x=30, y=272)
    cal_checkin.place(x=140, y=275)
    label_checkout.place(x=30, y=312)
    cal_checkout.place(x=140, y=315)

    button_submit = tk.Button(main_frame_child, text="Submit", font=("Arial", 11), bg=color1, command=submit_data)
    button_submit.pack()
    button_submit.place(relx=0.5, y=420, anchor=tk.CENTER)

    def payment_value():
        return payment.get()
    payment = tk.StringVar(value="1")
    label_payment = tk.Label(main_frame_child, text="Metode Pembayaran: ", font=("Arial", 11), bg=color2)
    rb_cash = tk.Radiobutton(main_frame_child, text="Cash", variable=payment, value="Laki-Laki", font=("Arial", 11), bg=color2, command=payment_value)
    rb_transfer = tk.Radiobutton(main_frame_child, text="Transfer", variable=payment, value="Perempuan", font=("Arial", 11), bg=color2, command=payment_value)
    label_payment.pack()
    rb_cash.pack()
    rb_transfer.pack()
    label_payment.place(relx=0.5, y=355, anchor=tk.CENTER)
    rb_cash.place(x=100, y=370)
    rb_transfer.place(x=200, y=370)

def lht_dftr_kmr_page():
    dftr_kmr = ttk.Treeview(main_frame, columns=(1,2,3,4), height=15, show="headings")

    dftr_kmr.column(1, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_kmr.column(2, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_kmr.column(3, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_kmr.column(4, anchor=tk.CENTER, stretch=tk.YES, width=100)

    dftr_kmr.heading(1, text="Tipe Kamar")
    dftr_kmr.heading(2, text="No. Kamar")
    dftr_kmr.heading(3, text="Harga per Malam")
    dftr_kmr.heading(4, text="Ketersediaan Kamar")

    dftr_kmr.pack(fill="both", expand=True)

    def display_dftr_kmr():
        mycursor.execute("SELECT * FROM tbl_no_kamar INNER JOIN tbl_kamar ON tbl_no_kamar.id_kamar = tbl_kamar.id_kamar")
        hasil = mycursor.fetchall()
        kolom = [kolom[0] for kolom in mycursor.description]

        for data in range(len(hasil)):
            mata_uang = f"Rp. {(hasil[data][kolom.index('harga_per_malam')]):,}"
            dftr_kmr.insert("", 'end', value=(hasil[data][kolom.index("tipe_kamar")],hasil[data][kolom.index("no_kamar")],mata_uang.replace(",", "."),hasil[data][kolom.index("ketersediaan_kamar")]))
        
    display_dftr_kmr()

def lht_dftr_tm_page():
    dftr_tm = ttk.Treeview(main_frame, columns=(1,2,3), height=15, show="headings")

    dftr_tm.column(1, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_tm.column(2, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_tm.column(3, anchor=tk.CENTER, stretch=tk.YES, width=100)

    dftr_tm.heading(1, text="Nama Tamu")
    dftr_tm.heading(2, text="Jenis Kelamin")
    dftr_tm.heading(3, text="Nomor Telepon")

    dftr_tm.pack(fill="both", expand=True)

    def display_dftr_tm():
        mycursor.execute("SELECT * FROM tbl_tamu")
        hasil = mycursor.fetchall()

        for data in range(len(hasil)):
            dftr_tm.insert("", 'end', value=(hasil[data][1], hasil[data][2], hasil[data][3]))

    display_dftr_tm()

def lht_dftr_rsrvsi_page():
    dftr_rsrvsi = ttk.Treeview(main_frame, columns=(1,2,3,4,5), height=15, show="headings")

    dftr_rsrvsi.column(1, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_rsrvsi.column(2, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_rsrvsi.column(3, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_rsrvsi.column(4, anchor=tk.CENTER, stretch=tk.YES, width=100)
    dftr_rsrvsi.column(5, anchor=tk.CENTER, stretch=tk.YES, width=100)

    dftr_rsrvsi.heading(1, text="ID Reservasi")
    dftr_rsrvsi.heading(2, text="Nama Tamu")
    dftr_rsrvsi.heading(3, text="Nomor Kamar")
    dftr_rsrvsi.heading(4, text="Tanggal Check-in")
    dftr_rsrvsi.heading(5, text="Tanggal Check-out")

    dftr_rsrvsi.pack(fill="both", expand=True)

    def display_dftr_rsrvsi():
        mycursor.execute(
            '''SELECT * FROM tbl_reservasi
            INNER JOIN tbl_tamu ON tbl_reservasi.id_tamu = tbl_tamu.id_tamu
            INNER JOIN tbl_no_kamar ON tbl_reservasi.id_no_kamar = tbl_no_kamar.id_no_kamar'''
            )
        hasil = mycursor.fetchall()
        kolom = [kolom[0] for kolom in mycursor.description]

        for data in range(len(hasil)):
            dftr_rsrvsi.insert("", 'end', value=(
                hasil[data][kolom.index("id_reservasi")],
                hasil[data][kolom.index("nama_tamu")],
                hasil[data][kolom.index("no_kamar")],
                hasil[data][kolom.index("tgl_checkin")],
                hasil[data][kolom.index("tgl_checkout")]
                ))

    display_dftr_rsrvsi()

def lht_rwyt_pmbyrn_page():
    rwyt_pmbyrn = ttk.Treeview(main_frame, columns=(1,2,3,4), height=15, show="headings")

    rwyt_pmbyrn.column(1, anchor=tk.CENTER, stretch=tk.YES, width=100)
    rwyt_pmbyrn.column(2, anchor=tk.CENTER, stretch=tk.YES, width=100)
    rwyt_pmbyrn.column(3, anchor=tk.CENTER, stretch=tk.YES, width=100)
    rwyt_pmbyrn.column(4, anchor=tk.CENTER, stretch=tk.YES, width=100)

    rwyt_pmbyrn.heading(1, text="ID Reservasi")
    rwyt_pmbyrn.heading(2, text="Metode Pembayaran")
    rwyt_pmbyrn.heading(3, text="Total Tagihan")
    rwyt_pmbyrn.heading(4, text="Tanggal Pembayaran")

    rwyt_pmbyrn.pack(fill="both", expand=True)

    def display_rwyt_pmbyrn():
        mycursor.execute("SELECT * FROM tbl_pembayaran INNER JOIN tbl_reservasi ON tbl_pembayaran.id_reservasi = tbl_reservasi.id_reservasi")
        hasil = mycursor.fetchall()
        kolom = [kolom[0] for kolom in mycursor.description]

        for data in range(len(hasil)):
            mata_uang = f"Rp. {(hasil[data][kolom.index('total_tagihan')]):,}"
            rwyt_pmbyrn.insert("", 'end', value=(
                hasil[data][kolom.index("id_reservasi")],
                hasil[data][kolom.index("metode_pembayaran")],
                mata_uang.replace(",", "."),
                hasil[data][kolom.index("tgl_pembayaran")]
                ))

    display_rwyt_pmbyrn()

#Options Frame

def hide_indecate():
    psn_kmr_indicate.config(bg=color1)
    lht_kmr_indicate.config(bg=color1)
    lht_tm_indicate.config(bg=color1)
    lht_rsrvsi_indicate.config(bg=color1)
    lht_byr_indicate.config(bg=color1)

def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(slct, page):
    hide_indecate()
    slct.config(bg=color3)
    delete_page()
    page()


psn_kmr_btn = tk.Button(option_frame,
                     text='Pesan Kamar',
                     font=("Montserrat", 14, "bold"),
                     fg=color3,
                     activeforeground=color1,
                     activebackground=color3,
                     bd=0,
                     bg=color1,
                     command=lambda: indicate(psn_kmr_indicate, pesan_kamar_page),
                     )

psn_kmr_btn.place(x=10, y=30)

psn_kmr_indicate = tk.Label(option_frame, text=" ", bg=color1)
psn_kmr_indicate.place(x=3, y=30, width=5, height=35)

lht_kmr_btn = tk.Button(option_frame,
                     text='Lihat Daftar Kamar',
                     font=("Montserrat", 14, "bold"),
                     fg=color3,
                     activeforeground=color1,
                     activebackground=color3,
                     bd=0,
                     bg=color1,
                     wraplength=120,
                     justify=tk.LEFT,
                     command=lambda: indicate(lht_kmr_indicate, lht_dftr_kmr_page)
                     )

lht_kmr_btn.place(x=10, y=100)

lht_kmr_indicate = tk.Label(option_frame, text=" ", bg=color1)
lht_kmr_indicate.place(x=3, y=100, width=5, height=58)

lht_tm_btn = tk.Button(option_frame,
                     text='Lihat Daftar Tamu',
                     font=("Montserrat", 14, "bold"),
                     fg=color3,
                     activeforeground=color1,
                     activebackground=color3,
                     bd=0,
                     bg=color1,
                     wraplength=120,
                     justify=tk.LEFT,
                     command=lambda: indicate(lht_tm_indicate, lht_dftr_tm_page)
                     )

lht_tm_btn.place(x=10, y=190)

lht_tm_indicate = tk.Label(option_frame, text=" ", bg=color1)
lht_tm_indicate.place(x=3, y=190, width=5, height=58)

lht_rsrvsi_btn = tk.Button(option_frame,
                     text='Lihat Daftar Reservasi',
                     font=("Montserrat", 14, "bold"),
                     fg=color3,
                     activeforeground=color1,
                     activebackground=color3,
                     bd=0,
                     bg=color1,
                     wraplength=120,
                     justify=tk.LEFT,
                     command=lambda: indicate(lht_rsrvsi_indicate, lht_dftr_rsrvsi_page)
                     )

lht_rsrvsi_btn.place(x=10, y=280)

lht_rsrvsi_indicate = tk.Label(option_frame, text=" ", bg=color1)
lht_rsrvsi_indicate.place(x=3, y=280, width=5, height=58)

lht_byr_btn = tk.Button(option_frame,
                     text='Lihat Riwayat Pembayaran',
                     font=("Montserrat", 14, "bold"),
                     fg=color3,
                     bd=0,
                     bg=color1,
                     wraplength=130,
                     justify=tk.LEFT,
                     command=lambda: indicate(lht_byr_indicate, lht_rwyt_pmbyrn_page)
                     )

lht_byr_btn.place(x=10, y=370)

lht_byr_indicate = tk.Label(option_frame, text=" ", bg=color1)
lht_byr_indicate.place(x=3, y=370, width=5, height=58)


root.mainloop()