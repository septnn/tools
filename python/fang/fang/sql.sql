CREATE TABLE `fang_detail` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fkey` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '关键词',
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '名字',
  `total` int(10) DEFAULT 0 COMMENT '总价',
  `unit` int(10) DEFAULT 0 COMMENT '单价',
  `house_area` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '房子面积',
  `house_loyout` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '房型/户型',
  `house_turn` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '朝向',
  `house_build` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '楼型',
  `community` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '小区/社区',
  `area` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '所在区域',
  `base_detail` text COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '基本详情',
  `transaction` text COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '交易属性',
  `special` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '特点',
  `house_img` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '户型图',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci