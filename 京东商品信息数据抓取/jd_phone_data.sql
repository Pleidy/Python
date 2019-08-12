/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : jd

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2019-04-01 17:10:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jd_phone_data_copy
-- ----------------------------
DROP TABLE IF EXISTS `jd_phone_data_copy`;
CREATE TABLE `jd_phone_data_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `phone_info` varchar(255) DEFAULT NULL COMMENT '手机信息',
  `price` int(11) DEFAULT NULL,
  `volum` varchar(255) DEFAULT NULL,
  `phone_brand` varchar(255) DEFAULT NULL COMMENT '手机品牌',
  `phone_model` varchar(255) DEFAULT NULL COMMENT '手机型号',
  `phone_net_model` varchar(255) DEFAULT NULL COMMENT '入网型号',
  `list_time` varchar(255) DEFAULT NULL COMMENT '上市时间',
  `phone_system` varchar(255) DEFAULT NULL COMMENT '操作系统',
  `cpu_kernel` varchar(255) DEFAULT NULL COMMENT '处理器：核数',
  `cpu_model` varchar(255) DEFAULT NULL COMMENT '处理器：型号',
  `screen_size` varchar(255) DEFAULT NULL COMMENT '屏幕大小',
  `screen_resolution` varchar(255) DEFAULT NULL COMMENT '分辨率',
  `capacity` varchar(255) DEFAULT NULL COMMENT '电池容量',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jd_phone_data_copy
-- ----------------------------
SET FOREIGN_KEY_CHECKS=1;
