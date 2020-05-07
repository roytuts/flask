CREATE TABLE `product` (
	`id` int unsigned NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`code` varchar(255) NOT NULL,
	`price` double NOT NULL,
	`category_id` int unsigned NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

INSERT INTO `product` (`id`, `name`, `code`, `price`) VALUES
(1, 'American Tourist', 'AMTR01', 12000.00),
(2, 'EXP Portable Hard Drive', 'USB02', 5000.00),
(3, 'Shoes', 'SH03', 1000.00),
(4, 'XP 1155 Intel Core Laptop', 'LPN4', 80000.00),
(5, 'FinePix Pro2 3D Camera', '3DCAM01', 150000.00),
(6, 'Simple Mobile', 'MB06', 3000.00),
(7, 'Luxury Ultra thin Wrist Watch', 'WristWear03', 3000.00),
(8, 'Headphone', 'HD08', 400.00);
