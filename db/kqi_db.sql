/*
Navicat MySQL Data Transfer

Source Server         : 本地mysql5.6
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : kqi_db

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2018-06-27 16:03:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for mm_2018
-- ----------------------------
DROP TABLE IF EXISTS `mm_2018`;
CREATE TABLE `mm_2018` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增主键，不用管',
  `product_name` varchar(255) NOT NULL COMMENT '产品名称',
  `client` varchar(255) NOT NULL COMMENT '测试端，android/ios/web/wap',
  `bussiness` varchar(255) NOT NULL COMMENT '测试业务的具体场景，用来做权重区分',
  `data_type` varchar(255) NOT NULL COMMENT '数据类型，参见test_type表',
  `data_value` varchar(255) NOT NULL COMMENT '测试值',
  `network` varchar(255) NOT NULL DEFAULT '' COMMENT '4G/Wifi/固网',
  `remark` varchar(255) DEFAULT NULL COMMENT '用于备注',
  `test_time` datetime NOT NULL COMMENT '测试时间',
  `modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据最后一次修改时间',
  `id_delete` varchar(255) DEFAULT '0' COMMENT '未删除：0/已删除：1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mm_2018
-- ----------------------------

-- ----------------------------
-- Table structure for test_type
-- ----------------------------
DROP TABLE IF EXISTS `test_type`;
CREATE TABLE `test_type` (
  `id` int(100) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `type` varchar(255) DEFAULT NULL COMMENT '类型',
  `type_name` varchar(255) DEFAULT NULL COMMENT '类型名称',
  `mathematical_unit` varchar(255) DEFAULT NULL COMMENT '单位',
  `modify_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次修改时间',
  `id_delete` varchar(255) DEFAULT '0' COMMENT '已删除:1/未删除:0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test_type
-- ----------------------------
INSERT INTO `test_type` VALUES ('1', 'time_delay', '时延', 's', '2018-06-19 14:48:22', '0');
INSERT INTO `test_type` VALUES ('2', 'success_rate', '成功率', '%', '2018-06-19 14:48:28', '0');
INSERT INTO `test_type` VALUES ('3', 'upload_rate', '上传速率', 'Mbps', '2018-06-19 14:48:16', '0');
INSERT INTO `test_type` VALUES ('4', 'download_rate', '下载速率', 'Mbps', '2018-06-19 14:48:17', '0');
INSERT INTO `test_type` VALUES ('6', 'charge', '电量消耗', '待定', '2018-06-19 14:52:57', '0');
INSERT INTO `test_type` VALUES ('7', 'flow', '流量消耗', 'KB', '2018-06-19 15:20:45', '0');
