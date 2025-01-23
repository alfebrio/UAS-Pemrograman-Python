-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 23 Jan 2025 pada 05.33
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_phone`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `phones`
--

CREATE TABLE `phones` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `category` varchar(50) NOT NULL,
  `released` decimal(11,0) NOT NULL,
  `display` varchar(100) NOT NULL,
  `camera` varchar(100) NOT NULL,
  `ram` varchar(50) NOT NULL,
  `chipset` varchar(100) NOT NULL,
  `battery` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `phones`
--

INSERT INTO `phones` (`id`, `name`, `brand`, `category`, `released`, `display`, `camera`, `ram`, `chipset`, `battery`, `price`) VALUES
(1, 'string', 'string', 'string', 0, 'string', 'string', 'string', 'string', 'string', 0.00),
(3, 'Poco F6', 'Xiaomi', 'High-End', 2024, '6.67\" 1220x2712', '50MP OIS + 8MP', '8/12GB', 'Snapdragon 8s Gen 3', '5000mAh', 5400000.00),
(7, 'string', 'string', 'string', 0, 'string', 'string', 'string', 'string', 'string', 0.00);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `phones`
--
ALTER TABLE `phones`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `phones`
--
ALTER TABLE `phones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
