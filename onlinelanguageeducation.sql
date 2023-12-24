-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 24 Ara 2023, 14:15:32
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `onlinelanguageeducation`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `classes`
--

CREATE TABLE `classes` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `link` varchar(300) NOT NULL,
  `email` varchar(100) NOT NULL,
  `time` varchar(50) NOT NULL,
  `state` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `classes`
--

INSERT INTO `classes` (`id`, `name`, `link`, `email`, `time`, `state`) VALUES
(2, 'grammer', 'https://www.teams.com/watch?v=kmI_2wCewpUt', 'koray@gmail.com', '14:50 26.12.23', 1);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `clubs`
--

CREATE TABLE `clubs` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `link` varchar(300) NOT NULL,
  `level` varchar(50) NOT NULL DEFAULT '0',
  `time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `clubs`
--

INSERT INTO `clubs` (`id`, `name`, `link`, `level`, `time`) VALUES
(1, 'Speaking', 'https://www.teams.com/watch?v=kmI_2wCewpUt', '4', '14:50 26.12.23');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `exam_results`
--

CREATE TABLE `exam_results` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `score` varchar(16) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `exam_results`
--

INSERT INTO `exam_results` (`id`, `name`, `last_name`, `email`, `score`) VALUES
(1, 'Mark', 'Otto', 'eminesener063@gmail.com', '60'),
(2, 'Mark', 'Otto', 'eminesener063@gmail.com', '90'),
(3, 'Mark', 'Otto', 'eminesener063@gmail.com', '30'),
(4, 'Mark', 'Otto', 'eminesener063@gmail.com', '30'),
(5, 'Mark', 'Otto', 'eminesener063@gmail.com', '20'),
(6, 'Mark', 'Otto', '21360859058@ogrenci.btu.edu.tr', '20'),
(7, 'Mark', 'Otto', 'eminesener063@gmail.com', '30'),
(8, 'Emine', 'Şener', 'eminesener063@gmail.com', '90'),
(9, 'Emine', 'Şener', 'eminesener063@gmail.com', '60'),
(10, 'Emine', 'Şener', 'senereminesnr@gmail.com', '30'),
(11, 'Emine', 'Şener', 'senereminesnr@gmail.com', '30'),
(12, 'Emine', 'Şener', 'senereminesnr@gmail.com', '30'),
(13, 'Emine', 'Şener', 'senereminesnr@gmail.com', '50'),
(14, 'Emine', 'Şener', 'senereminesnr@gmail.com', '0'),
(15, 'Mark', 'Otto', 'yukselsener9@gmail.com', '40'),
(16, 'Mark', 'Otto', 'computer.engineer.166@gmail.com', '20'),
(17, 'Mark', 'Otto', '21360859058@ogrenci.btu.edu.tr', '0'),
(18, 'Mark', 'Otto', '21360859058@ogrenci.btu.edu.tr', '0'),
(19, 'Mark', 'Otto', 'eminesener063@gmail.com', '0'),
(20, 'Mark', 'Otto', 'eminesener063@gmail.com', '0'),
(21, 'Emine ', 'Sener ', 'senereminesnr@gmail.com', '40'),
(22, 'Mark', 'Otto', 'senereminesnr@gmail.com', '0'),
(23, 'Mark', 'Otto', 'senereminesnr@gmail.com', '10'),
(24, 'Mark', 'Otto', '21360859058@ogrenci.btu.edu.tr', '0'),
(25, 'Mark', 'Otto', 'computer.engineer.166@gmail.com', '0'),
(26, 'Mark', 'Otto', 'senereminesnr@gmail.com', '0'),
(27, 'Mark', 'Otto', 'computer.engineer.166@gmail.com', '0'),
(28, 'Mark', 'Otto', '21360859058@ogrenci.btu.edu.tr', '10'),
(29, 'Koray', 'Ormankıran', 'koray@gmail.com', '40'),
(30, 'Koray', 'Ormankıran', 'koray@gmail.com', '100');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `homeworks`
--

CREATE TABLE `homeworks` (
  `id` int(50) NOT NULL,
  `homework` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `from_email` varchar(50) NOT NULL,
  `answer` varchar(50) NOT NULL DEFAULT '0',
  `score` varchar(50) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `homeworks`
--

INSERT INTO `homeworks` (`id`, `homework`, `email`, `from_email`, `answer`, `score`) VALUES
(2, 'Pronouns 5 sentences!', 'koray@gmail.com', '21360859058@ogrenci.btu.edu.tr', 'I..', '78');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `level_and_packages`
--

CREATE TABLE `level_and_packages` (
  `id` int(50) NOT NULL,
  `level` varchar(50) NOT NULL,
  `package` varchar(50) NOT NULL,
  `info` varchar(50) NOT NULL,
  `price` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `level_and_packages`
--

INSERT INTO `level_and_packages` (`id`, `level`, `package`, `info`, `price`) VALUES
(1, '10', 'A1', 'Temel Seviye', '$300'),
(4, '60', 'B1', 'Orta Seviye', '$350'),
(5, '90', 'C1', 'İleri Seviye', '$370'),
(7, '0', 'A1', 'Temel Seviye', '$300'),
(8, '20', 'A1', 'Temel Seviye', '$300'),
(9, '30', 'A1', 'Temel Seviye', '$300'),
(10, '40', 'B1', 'Orta Seviye', '$350'),
(11, '50', 'B1', 'Orta Seviye', '$350'),
(12, '70', 'B1', 'Orta Seviye', '$350'),
(13, '80', 'C1', 'İleri Seviye', '$370'),
(14, '100', 'C1', 'İleri Seviye', '$370');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `message` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `from_email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `messages`
--

INSERT INTO `messages` (`id`, `message`, `email`, `from_email`) VALUES
(4, 'odevleri tamamladım', '21360859058@ogrenci.btu.edu.tr', 'koray@gmail.com'),
(5, 'odevleri tamamladım', '21360859058@ogrenci.btu.edu.tr', 'koray@gmail.com'),
(6, 'odevleri tamamladım', '21360859058@ogrenci.btu.edu.tr', 'koray@gmail.com');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sources`
--

CREATE TABLE `sources` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `link` varchar(50) NOT NULL,
  `level` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `sources`
--

INSERT INTO `sources` (`id`, `name`, `link`, `level`) VALUES
(1, 'ENGLISH GRAMMAR IN USE', 'https://canadadotnet.files.wordpress.com/2020/05/e', '2'),
(2, 'ENGLISH GRAMMAR IN USE', 'https://canadadotnet.files.wordpress.com/2020/05/e', '4'),
(3, 'ENGLISH GRAMMAR IN USE', 'https://canadadotnet.files.wordpress.com/2020/05/e', '2'),
(4, 'ENGLISH GRAMMAR IN USE', 'https://canadadotnet.files.wordpress.com/2020/05/e', '5'),
(5, 'ENGLISH GRAMMAR IN USE', 'https://canadadotnet.files.wordpress.com/2020/05/e', '6'),
(6, 'ENGLISH GRAMMAR IN USE', 'https://canadadotnet.files.wordpress.com/2020/05/e', '3');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `students`
--

CREATE TABLE `students` (
  `id` int(255) NOT NULL,
  `name` char(1) DEFAULT NULL,
  `last_name` text DEFAULT NULL,
  `email` text NOT NULL,
  `package` varchar(50) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `students`
--

INSERT INTO `students` (`id`, `name`, `last_name`, `email`, `package`, `password`) VALUES
(1, 'M', 'Otto', 'computer.engineer.166@gmail.com', 'B1', '0'),
(7, 'M', 'Otto', 'eminesener063@gmail.com', 'A2', '8068'),
(10, 'E', 'Şener', 'senereminesnr@gmail.com', 'A2', '6072'),
(15, 'M', 'Otto', 'yukselsener9@gmail.com', 'C1', '4650'),
(16, 'M', 'Otto', 'computer.engineer.166@gmail.com', 'B2', '0265'),
(20, 'M', 'Otto', 'eminesener063@gmail.com', 'B1', '7782'),
(25, 'M', 'Otto', 'computer.engineer.166@gmail.com', 'B1', '3156'),
(27, 'M', 'Otto', 'computer.engineer.166@gmail.com', 'A1', '5078'),
(28, 'M', 'Otto', '21360859058@ogrenci.btu.edu.tr', 'A1', '8994'),
(30, 'K', 'Ormankıran', 'koray@gmail.com', 'B1', '5520');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `teachers`
--

CREATE TABLE `teachers` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` text NOT NULL,
  `level` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `teachers`
--

INSERT INTO `teachers` (`id`, `name`, `last_name`, `email`, `level`, `password`) VALUES
(1, 'Mark', 'Otto', '21360859058@ogrenci.btu.edu.tr', 'B', '6729'),
(3, 'Mark', 'Otto', '', 'C', '0354');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `teacher_apply`
--

CREATE TABLE `teacher_apply` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `score` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL DEFAULT 'evaluate'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `teacher_apply`
--

INSERT INTO `teacher_apply` (`id`, `name`, `last_name`, `email`, `score`, `state`) VALUES
(1, 'Mark', 'Otto', '21360859058@ogrenci.btu.edu.tr', '20', '1'),
(2, 'Mark', 'Otto', 'eminesener063@gmail.com', '0', '1'),
(3, 'Mark', 'Otto', 'eminesener063@gmail.com', '0', '1');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `videos`
--

CREATE TABLE `videos` (
  `id` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `link` varchar(50) NOT NULL,
  `level` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `videos`
--

INSERT INTO `videos` (`id`, `name`, `link`, `level`) VALUES
(0, 'Pronouns', 'https://www.youtube.com/watch?v=kmI_2wCewpU', 'A2'),
(0, '[https://www.youtube.com/watch?v=kmI_2wCewpU]', '[Verbs]', '[B2]'),
(2, 'verbs', 'https://www.youtube.com/watch?v=kmI_2wCewpU', 'B2'),
(3, 'verbs', 'https://www.youtube.com/watch?v=kmI_2wCewpU', 'B2'),
(2, 'verbs', 'https://www.youtube.com/watch?v=kmI_2wCewpU', 'B2'),
(3, 'verbs', 'https://www.youtube.com/watch?v=kmI_2wCewpU', 'B2');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `clubs`
--
ALTER TABLE `clubs`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `exam_results`
--
ALTER TABLE `exam_results`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `homeworks`
--
ALTER TABLE `homeworks`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `level_and_packages`
--
ALTER TABLE `level_and_packages`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `sources`
--
ALTER TABLE `sources`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `teacher_apply`
--
ALTER TABLE `teacher_apply`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `classes`
--
ALTER TABLE `classes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `clubs`
--
ALTER TABLE `clubs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `exam_results`
--
ALTER TABLE `exam_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Tablo için AUTO_INCREMENT değeri `homeworks`
--
ALTER TABLE `homeworks`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `level_and_packages`
--
ALTER TABLE `level_and_packages`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Tablo için AUTO_INCREMENT değeri `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `sources`
--
ALTER TABLE `sources`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `teacher_apply`
--
ALTER TABLE `teacher_apply`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
