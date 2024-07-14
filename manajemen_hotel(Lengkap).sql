-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2024 at 07:40 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `manajemen_hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_fasilitas`
--

CREATE TABLE `tbl_fasilitas` (
  `id_fasilitas` int(11) NOT NULL,
  `nama_fasilitas` varchar(30) DEFAULT NULL,
  `biaya_tambahan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_fasilitas`
--

INSERT INTO `tbl_fasilitas` (`id_fasilitas`, `nama_fasilitas`, `biaya_tambahan`) VALUES
(104001, 'Kolam Renang', 100000),
(104002, 'Ruang Olahraga', 150000),
(104003, 'SPA', 100000),
(104004, 'Ruang Theater', 50000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_kamar`
--

CREATE TABLE `tbl_kamar` (
  `id_kamar` int(11) NOT NULL,
  `tipe_kamar` varchar(50) DEFAULT NULL,
  `harga_per_malam` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_kamar`
--

INSERT INTO `tbl_kamar` (`id_kamar`, `tipe_kamar`, `harga_per_malam`) VALUES
(102001, 'Standart', 300000),
(102002, 'Superior', 500000),
(102003, 'Deluxe', 750000),
(102004, 'Suite', 1000000),
(102005, 'Presidential Suite', 5000000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_no_kamar`
--

CREATE TABLE `tbl_no_kamar` (
  `id_no_kamar` int(11) NOT NULL,
  `id_kamar` int(11) DEFAULT NULL,
  `no_kamar` int(11) DEFAULT NULL,
  `ketersediaan_kamar` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_no_kamar`
--

INSERT INTO `tbl_no_kamar` (`id_no_kamar`, `id_kamar`, `no_kamar`, `ketersediaan_kamar`) VALUES
(107001, 102001, 201, NULL),
(107002, 102001, 202, NULL),
(107003, 102001, 203, NULL),
(107004, 102002, 204, NULL),
(107005, 102002, 205, NULL),
(107006, 102002, 206, NULL),
(107007, 102003, 207, NULL),
(107008, 102003, 208, NULL),
(107009, 102003, 209, NULL),
(107010, 102004, 210, NULL),
(107011, 102004, 211, NULL),
(107012, 102004, 212, NULL),
(107013, 102005, 213, NULL),
(107014, 102005, 214, NULL),
(107015, 102005, 215, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pembayaran`
--

CREATE TABLE `tbl_pembayaran` (
  `id_pembayaran` int(11) NOT NULL,
  `id_reservasi` int(11) DEFAULT NULL,
  `id_pemesanan_fasilitas` int(11) DEFAULT NULL,
  `id_tamu` int(11) DEFAULT NULL,
  `metode_pembayaran` varchar(30) DEFAULT NULL,
  `total_tagihan` int(11) DEFAULT NULL,
  `status_pembayaran` varchar(30) DEFAULT NULL,
  `tgl_pembayaran` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_pembayaran`
--

INSERT INTO `tbl_pembayaran` (`id_pembayaran`, `id_reservasi`, `id_pemesanan_fasilitas`, `id_tamu`, `metode_pembayaran`, `total_tagihan`, `status_pembayaran`, `tgl_pembayaran`) VALUES
(103001, 105001, 109001, 106001, 'Cash', 1100000, 'Lunas', '2024-05-16');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pemesanan_fasilitas`
--

CREATE TABLE `tbl_pemesanan_fasilitas` (
  `id_pemesanan_fasilitas` int(11) NOT NULL,
  `id_tamu` int(11) DEFAULT NULL,
  `id_fasilitas` int(11) DEFAULT NULL,
  `tgl_pemesanan` date DEFAULT NULL,
  `total_biaya` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_pemesanan_fasilitas`
--

INSERT INTO `tbl_pemesanan_fasilitas` (`id_pemesanan_fasilitas`, `id_tamu`, `id_fasilitas`, `tgl_pemesanan`, `total_biaya`) VALUES
(109001, 106001, 104001, '2024-05-16', 100000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_reservasi`
--

CREATE TABLE `tbl_reservasi` (
  `id_reservasi` int(11) NOT NULL,
  `id_tamu` int(11) DEFAULT NULL,
  `id_no_kamar` int(11) DEFAULT NULL,
  `tgl_reservasi` date DEFAULT NULL,
  `durasi_hari_menginap` int(11) DEFAULT NULL,
  `total_harga` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_reservasi`
--

INSERT INTO `tbl_reservasi` (`id_reservasi`, `id_tamu`, `id_no_kamar`, `tgl_reservasi`, `durasi_hari_menginap`, `total_harga`) VALUES
(105001, 106001, 107006, '2024-05-15', 3, 1000000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_tamu`
--

CREATE TABLE `tbl_tamu` (
  `id_tamu` int(11) NOT NULL,
  `nama_tamu` varchar(50) DEFAULT NULL,
  `no_tlp` char(13) DEFAULT NULL,
  `no_ktp` char(16) DEFAULT NULL,
  `tgl_checkin` date DEFAULT NULL,
  `tgl_checkout` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_tamu`
--

INSERT INTO `tbl_tamu` (`id_tamu`, `nama_tamu`, `no_tlp`, `no_ktp`, `tgl_checkin`, `tgl_checkout`) VALUES
(106001, 'Abdan Marzuki', '082284777073', '1234567890654321', '2024-05-13', '2024-05-15');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_fasilitas`
--
ALTER TABLE `tbl_fasilitas`
  ADD PRIMARY KEY (`id_fasilitas`);

--
-- Indexes for table `tbl_kamar`
--
ALTER TABLE `tbl_kamar`
  ADD PRIMARY KEY (`id_kamar`);

--
-- Indexes for table `tbl_no_kamar`
--
ALTER TABLE `tbl_no_kamar`
  ADD PRIMARY KEY (`id_no_kamar`),
  ADD KEY `id_kamar` (`id_kamar`);

--
-- Indexes for table `tbl_pembayaran`
--
ALTER TABLE `tbl_pembayaran`
  ADD PRIMARY KEY (`id_pembayaran`),
  ADD KEY `id_reservasi` (`id_reservasi`,`id_pemesanan_fasilitas`),
  ADD KEY `id_pemesanan_fasilitas` (`id_pemesanan_fasilitas`),
  ADD KEY `id_tamu` (`id_tamu`);

--
-- Indexes for table `tbl_pemesanan_fasilitas`
--
ALTER TABLE `tbl_pemesanan_fasilitas`
  ADD PRIMARY KEY (`id_pemesanan_fasilitas`),
  ADD KEY `id_tamu` (`id_tamu`,`id_fasilitas`),
  ADD KEY `id_fasilitas` (`id_fasilitas`);

--
-- Indexes for table `tbl_reservasi`
--
ALTER TABLE `tbl_reservasi`
  ADD PRIMARY KEY (`id_reservasi`),
  ADD KEY `id_tamu` (`id_tamu`,`id_no_kamar`),
  ADD KEY `id_no_kamar` (`id_no_kamar`);

--
-- Indexes for table `tbl_tamu`
--
ALTER TABLE `tbl_tamu`
  ADD PRIMARY KEY (`id_tamu`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_fasilitas`
--
ALTER TABLE `tbl_fasilitas`
  MODIFY `id_fasilitas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104005;

--
-- AUTO_INCREMENT for table `tbl_kamar`
--
ALTER TABLE `tbl_kamar`
  MODIFY `id_kamar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102020;

--
-- AUTO_INCREMENT for table `tbl_no_kamar`
--
ALTER TABLE `tbl_no_kamar`
  MODIFY `id_no_kamar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107016;

--
-- AUTO_INCREMENT for table `tbl_pembayaran`
--
ALTER TABLE `tbl_pembayaran`
  MODIFY `id_pembayaran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103002;

--
-- AUTO_INCREMENT for table `tbl_pemesanan_fasilitas`
--
ALTER TABLE `tbl_pemesanan_fasilitas`
  MODIFY `id_pemesanan_fasilitas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109002;

--
-- AUTO_INCREMENT for table `tbl_reservasi`
--
ALTER TABLE `tbl_reservasi`
  MODIFY `id_reservasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105002;

--
-- AUTO_INCREMENT for table `tbl_tamu`
--
ALTER TABLE `tbl_tamu`
  MODIFY `id_tamu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106002;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_no_kamar`
--
ALTER TABLE `tbl_no_kamar`
  ADD CONSTRAINT `tbl_no_kamar_ibfk_1` FOREIGN KEY (`id_kamar`) REFERENCES `tbl_kamar` (`id_kamar`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_pembayaran`
--
ALTER TABLE `tbl_pembayaran`
  ADD CONSTRAINT `tbl_pembayaran_ibfk_1` FOREIGN KEY (`id_reservasi`) REFERENCES `tbl_reservasi` (`id_reservasi`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_pembayaran_ibfk_2` FOREIGN KEY (`id_pemesanan_fasilitas`) REFERENCES `tbl_pemesanan_fasilitas` (`id_pemesanan_fasilitas`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_pembayaran_ibfk_3` FOREIGN KEY (`id_tamu`) REFERENCES `tbl_tamu` (`id_tamu`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_pemesanan_fasilitas`
--
ALTER TABLE `tbl_pemesanan_fasilitas`
  ADD CONSTRAINT `tbl_pemesanan_fasilitas_ibfk_1` FOREIGN KEY (`id_fasilitas`) REFERENCES `tbl_fasilitas` (`id_fasilitas`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_pemesanan_fasilitas_ibfk_2` FOREIGN KEY (`id_tamu`) REFERENCES `tbl_tamu` (`id_tamu`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_reservasi`
--
ALTER TABLE `tbl_reservasi`
  ADD CONSTRAINT `tbl_reservasi_ibfk_1` FOREIGN KEY (`id_tamu`) REFERENCES `tbl_tamu` (`id_tamu`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_reservasi_ibfk_3` FOREIGN KEY (`id_no_kamar`) REFERENCES `tbl_no_kamar` (`id_no_kamar`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
