-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2024 at 01:29 PM
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
(101, 'Standart', 300000),
(102, 'Superior', 500000),
(103, 'Deluxe', 750000),
(104, 'Suite', 1000000),
(105, 'Presidential Suite', 5000000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_no_kamar`
--

CREATE TABLE `tbl_no_kamar` (
  `id_no_kamar` int(11) NOT NULL,
  `id_kamar` int(11) DEFAULT NULL,
  `no_kamar` char(3) DEFAULT NULL,
  `ketersediaan_kamar` varchar(30) DEFAULT 'Tersedia'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_no_kamar`
--

INSERT INTO `tbl_no_kamar` (`id_no_kamar`, `id_kamar`, `no_kamar`, `ketersediaan_kamar`) VALUES
(201, 101, 'K01', 'Tersedia'),
(202, 101, 'K02', 'Tersedia'),
(203, 101, 'K03', 'Tersedia'),
(204, 102, 'K04', 'Tersedia'),
(205, 102, 'K05', 'Tersedia'),
(206, 102, 'K06', 'Tersedia'),
(207, 103, 'K07', 'Tersedia'),
(208, 103, 'K08', 'Tersedia'),
(209, 103, 'K09', 'Tersedia'),
(210, 104, 'K10', 'Tersedia'),
(211, 104, 'K11', 'Tersedia'),
(212, 104, 'K12', 'Tersedia'),
(213, 105, 'K13', 'Tersedia'),
(214, 105, 'K14', 'Tersedia'),
(215, 105, 'K15', 'Tersedia');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_pembayaran`
--

CREATE TABLE `tbl_pembayaran` (
  `id_pembayaran` int(11) NOT NULL,
  `id_reservasi` int(11) DEFAULT NULL,
  `metode_pembayaran` varchar(30) DEFAULT NULL,
  `total_tagihan` int(11) DEFAULT NULL,
  `tgl_pembayaran` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_reservasi`
--

CREATE TABLE `tbl_reservasi` (
  `id_reservasi` int(11) NOT NULL,
  `id_tamu` int(11) DEFAULT NULL,
  `id_no_kamar` int(11) DEFAULT NULL,
  `tgl_checkin` date DEFAULT NULL,
  `tgl_checkout` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_tamu`
--

CREATE TABLE `tbl_tamu` (
  `id_tamu` int(11) NOT NULL,
  `nama_tamu` varchar(50) DEFAULT NULL,
  `jenis_kelamin` varchar(10) DEFAULT NULL,
  `no_tlp` char(13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

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
  ADD KEY `id_reservasi` (`id_reservasi`);

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
-- AUTO_INCREMENT for table `tbl_kamar`
--
ALTER TABLE `tbl_kamar`
  MODIFY `id_kamar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=301;

--
-- AUTO_INCREMENT for table `tbl_no_kamar`
--
ALTER TABLE `tbl_no_kamar`
  MODIFY `id_no_kamar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=216;

--
-- AUTO_INCREMENT for table `tbl_pembayaran`
--
ALTER TABLE `tbl_pembayaran`
  MODIFY `id_pembayaran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=501;

--
-- AUTO_INCREMENT for table `tbl_reservasi`
--
ALTER TABLE `tbl_reservasi`
  MODIFY `id_reservasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=401;

--
-- AUTO_INCREMENT for table `tbl_tamu`
--
ALTER TABLE `tbl_tamu`
  MODIFY `id_tamu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=301;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_no_kamar`
--
ALTER TABLE `tbl_no_kamar`
  ADD CONSTRAINT `tbl_no_kamar_ibfk_1` FOREIGN KEY (`id_kamar`) REFERENCES `tbl_kamar` (`id_kamar`);

--
-- Constraints for table `tbl_pembayaran`
--
ALTER TABLE `tbl_pembayaran`
  ADD CONSTRAINT `tbl_pembayaran_ibfk_1` FOREIGN KEY (`id_reservasi`) REFERENCES `tbl_reservasi` (`id_reservasi`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tbl_reservasi`
--
ALTER TABLE `tbl_reservasi`
  ADD CONSTRAINT `tbl_reservasi_ibfk_1` FOREIGN KEY (`id_no_kamar`) REFERENCES `tbl_no_kamar` (`id_no_kamar`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_reservasi_ibfk_2` FOREIGN KEY (`id_tamu`) REFERENCES `tbl_tamu` (`id_tamu`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
