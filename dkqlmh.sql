-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 12, 2020 lúc 04:34 AM
-- Phiên bản máy phục vụ: 10.4.8-MariaDB
-- Phiên bản PHP: 7.2.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `dkqlmh`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `mon_hoc`
--

CREATE TABLE `mon_hoc` (
  `maMH` varchar(10) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `tenMH` varchar(20) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `soLuongToiDa` int(100) NOT NULL,
  `soTin` int(10) NOT NULL,
  `lop` varchar(10) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `khoa` varchar(20) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `thoiGian` varchar(30) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `soLuongdkHienTai` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `mon_hoc`
--

INSERT INTO `mon_hoc` (`maMH`, `tenMH`, `soLuongToiDa`, `soTin`, `lop`, `khoa`, `thoiGian`, `soLuongdkHienTai`) VALUES
('123456', 'Lập trình Python', 50, 2, '501T5', 'Toán', 'T6(1-2)', 0),
('123457', 'Lập trình Python', 50, 2, '504T5', 'Toán', 'T4(6-8)', 0),
('123458', 'Lập trình C/C++', 10, 2, '305T5', 'Toán', 'T2(6-8)', 0),
('123459', 'Lập trình C/C++', 10, 2, '105T5', 'Toán', 'T3(3-5)', 0),
('123460', 'Hóa học', 50, 3, '105T5', 'Hóa', 'T6(1-2)', 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sinh_vien`
--

CREATE TABLE `sinh_vien` (
  `maSV` int(10) NOT NULL,
  `hoTen` varchar(30) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `lop` varchar(15) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `khoa` varchar(20) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `gioiTinh` varchar(5) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `email` varchar(20) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `diaChi` varchar(30) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `tenDangNhap` varchar(10) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `matKhau` varchar(10) COLLATE utf8mb4_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `sinh_vien`
--

INSERT INTO `sinh_vien` (`maSV`, `hoTen`, `lop`, `khoa`, `gioiTinh`, `email`, `diaChi`, `tenDangNhap`, `matKhau`) VALUES
(17000358, 'Nguyễn Đăng Quân', 'K62-A4-Mt&khtt', 'Toán', 'Nam', 'quan@gmail.com', 'Hà Nội', '17000358', '123'),
(17000775, 'Nguyễn Ngọc Hiền', 'K62-A4-Mt&khtt', 'Toán', 'Nữ', 'hien@gmai.com', 'Hà Nội', '17000775', '123'),
(17001342, 'Nguyễn Thị Phương', 'K62-A4-Mt&khtt', 'Toán', 'Nữ', 'phuong@gmai.com', 'Hà Nội', '17001342', '123');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sv_kyhoc`
--

CREATE TABLE `sv_kyhoc` (
  `maSV` int(10) NOT NULL,
  `kyHoc` varchar(20) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `diemTB` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `sv_kyhoc`
--

INSERT INTO `sv_kyhoc` (`maSV`, `kyHoc`, `diemTB`) VALUES
(17000358, 'Kì I 2017-2018', 3);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sv_monhoc`
--

CREATE TABLE `sv_monhoc` (
  `maSV` int(10) NOT NULL,
  `tenMH` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `diemMH` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `kyhoc` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `sv_monhoc`
--

INSERT INTO `sv_monhoc` (`maSV`, `tenMH`, `diemMH`, `kyhoc`) VALUES
(17000358, 'Lập trình C/C++', 'C+', 'Kì I 2017-2018');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `tenDangNhap` varchar(10) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `matKhau` varchar(10) COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `phanquyen` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`tenDangNhap`, `matKhau`, `phanquyen`) VALUES
('17000358', '123', 2),
('17000775', '123', 2),
('17001342', '123', 2),
('admin', '123', 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `mon_hoc`
--
ALTER TABLE `mon_hoc`
  ADD PRIMARY KEY (`maMH`);

--
-- Chỉ mục cho bảng `sinh_vien`
--
ALTER TABLE `sinh_vien`
  ADD PRIMARY KEY (`maSV`,`email`,`tenDangNhap`) USING BTREE,
  ADD KEY `tenDangNhap` (`tenDangNhap`);

--
-- Chỉ mục cho bảng `sv_kyhoc`
--
ALTER TABLE `sv_kyhoc`
  ADD PRIMARY KEY (`maSV`,`kyHoc`);

--
-- Chỉ mục cho bảng `sv_monhoc`
--
ALTER TABLE `sv_monhoc`
  ADD PRIMARY KEY (`maSV`);

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`tenDangNhap`);

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sinh_vien`
--
ALTER TABLE `sinh_vien`
  ADD CONSTRAINT `sinh_vien_ibfk_1` FOREIGN KEY (`tenDangNhap`) REFERENCES `user` (`tenDangNhap`);

--
-- Các ràng buộc cho bảng `sv_kyhoc`
--
ALTER TABLE `sv_kyhoc`
  ADD CONSTRAINT `sv_kyhoc_ibfk_1` FOREIGN KEY (`maSV`) REFERENCES `sinh_vien` (`maSV`);

--
-- Các ràng buộc cho bảng `sv_monhoc`
--
ALTER TABLE `sv_monhoc`
  ADD CONSTRAINT `sv_mh` FOREIGN KEY (`maSV`) REFERENCES `sinh_vien` (`maSV`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
