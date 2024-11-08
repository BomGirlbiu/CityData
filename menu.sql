/*
MySQL Data Transfer
Source Host: localhost
Source Database: ry-vue
Target Host: localhost
Target Database: ry-vue
Date: 2024-11-08 12:12:58
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for sys_menu
-- ----------------------------
CREATE TABLE `sys_menu` (
  `menu_id` bigint NOT NULL AUTO_INCREMENT COMMENT '菜单ID',
  `menu_name` varchar(50) NOT NULL COMMENT '菜单名称',
  `parent_id` bigint DEFAULT '0' COMMENT '父菜单ID',
  `order_num` int DEFAULT '0' COMMENT '显示顺序',
  `path` varchar(200) DEFAULT '' COMMENT '路由地址',
  `component` varchar(255) DEFAULT NULL COMMENT '组件路径',
  `query` varchar(255) DEFAULT NULL COMMENT '路由参数',
  `route_name` varchar(50) DEFAULT '' COMMENT '路由名称',
  `is_frame` int DEFAULT '1' COMMENT '是否为外链（0是 1否）',
  `is_cache` int DEFAULT '0' COMMENT '是否缓存（0缓存 1不缓存）',
  `menu_type` char(1) DEFAULT '' COMMENT '菜单类型（M目录 C菜单 F按钮）',
  `visible` char(1) DEFAULT '0' COMMENT '菜单状态（0显示 1隐藏）',
  `status` char(1) DEFAULT '0' COMMENT '菜单状态（0正常 1停用）',
  `perms` varchar(100) DEFAULT NULL COMMENT '权限标识',
  `icon` varchar(100) DEFAULT '#' COMMENT '菜单图标',
  `create_by` varchar(64) DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` varchar(64) DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `remark` varchar(500) DEFAULT '' COMMENT '备注',
  PRIMARY KEY (`menu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2073 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='菜单权限表';

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `sys_menu` VALUES ('1', '系统管理', '0', '4', 'system', null, '', '', '1', '0', 'M', '0', '0', '', 'system', 'admin', '2024-10-20 19:53:20', '', null, '系统管理目录');
INSERT INTO `sys_menu` VALUES ('2', '系统监控', '0', '5', 'monitor', null, '', '', '1', '0', 'M', '0', '0', '', 'monitor', 'admin', '2024-10-20 19:53:20', '', null, '系统监控目录');
INSERT INTO `sys_menu` VALUES ('3', '系统工具', '0', '6', 'tool', null, '', '', '1', '0', 'M', '0', '0', '', 'tool', 'admin', '2024-10-20 19:53:20', '', null, '系统工具目录');
INSERT INTO `sys_menu` VALUES ('5', '讯息管理', '0', '1', 'data', '', null, '', '1', '0', 'M', '0', '0', '', 'user', 'admin', null, 'admin', '2024-11-07 17:47:59', '');
INSERT INTO `sys_menu` VALUES ('6', '用户管理', '0', '3', 'users', null, null, '', '1', '0', 'M', '0', '0', '', 'peoples', 'admin', null, 'admin', '2024-11-04 20:40:33', '');
INSERT INTO `sys_menu` VALUES ('7', '数据监测', '0', '2', 'detect', null, null, '', '1', '0', 'M', '0', '0', null, 'peoples', 'admin', null, 'admin', null, '');
INSERT INTO `sys_menu` VALUES ('101', '角色管理', '1', '2', 'role', 'system/role/index', '', '', '1', '0', 'C', '0', '0', 'system:role:list', 'peoples', 'admin', '2024-10-20 19:53:20', '', null, '角色管理菜单');
INSERT INTO `sys_menu` VALUES ('102', '菜单管理', '1', '3', 'menu', 'system/menu/index', '', '', '1', '0', 'C', '0', '0', 'system:menu:list', 'tree-table', 'admin', '2024-10-20 19:53:20', '', null, '菜单管理菜单');
INSERT INTO `sys_menu` VALUES ('103', '部门管理', '1', '4', 'dept', 'system/dept/index', '', '', '1', '0', 'C', '0', '0', 'system:dept:list', 'tree', 'admin', '2024-10-20 19:53:20', '', null, '部门管理菜单');
INSERT INTO `sys_menu` VALUES ('104', '作品管理', '1', '5', 'post', 'system/post/index', '', '', '1', '0', 'C', '0', '0', 'system:post:list', 'post', 'admin', '2024-10-20 19:53:20', '', null, '岗位管理菜单');
INSERT INTO `sys_menu` VALUES ('105', '字典管理', '1', '6', 'dict', 'system/dict/index', '', '', '1', '0', 'C', '0', '0', 'system:dict:list', 'dict', 'admin', '2024-10-20 19:53:20', '', null, '字典管理菜单');
INSERT INTO `sys_menu` VALUES ('106', '参数设置', '1', '7', 'config', 'system/config/index', '', '', '1', '0', 'C', '0', '0', 'system:config:list', 'edit', 'admin', '2024-10-20 19:53:20', '', null, '参数设置菜单');
INSERT INTO `sys_menu` VALUES ('107', '通知公告', '1', '8', 'notice', 'system/notice/index', '', '', '1', '0', 'C', '0', '0', 'system:notice:list', 'message', 'admin', '2024-10-20 19:53:20', '', null, '通知公告菜单');
INSERT INTO `sys_menu` VALUES ('108', '日志管理', '1', '9', 'log', '', '', '', '1', '0', 'M', '0', '0', '', 'log', 'admin', '2024-10-20 19:53:20', '', null, '日志管理菜单');
INSERT INTO `sys_menu` VALUES ('109', '在线用户', '2', '1', 'online', 'monitor/online/index', '', '', '1', '0', 'C', '0', '0', 'monitor:online:list', 'online', 'admin', '2024-10-20 19:53:20', '', null, '在线用户菜单');
INSERT INTO `sys_menu` VALUES ('110', '定时任务', '2', '2', 'job', 'monitor/job/index', '', '', '1', '0', 'C', '0', '0', 'monitor:job:list', 'job', 'admin', '2024-10-20 19:53:20', '', null, '定时任务菜单');
INSERT INTO `sys_menu` VALUES ('111', '数据监控', '2', '3', 'druid', 'monitor/druid/index', '', '', '1', '0', 'C', '0', '0', 'monitor:druid:list', 'druid', 'admin', '2024-10-20 19:53:20', '', null, '数据监控菜单');
INSERT INTO `sys_menu` VALUES ('112', '服务监控', '2', '4', 'server', 'monitor/server/index', '', '', '1', '0', 'C', '0', '0', 'monitor:server:list', 'server', 'admin', '2024-10-20 19:53:20', '', null, '服务监控菜单');
INSERT INTO `sys_menu` VALUES ('113', '缓存监控', '2', '5', 'cache', 'monitor/cache/index', '', '', '1', '0', 'C', '0', '0', 'monitor:cache:list', 'redis', 'admin', '2024-10-20 19:53:20', '', null, '缓存监控菜单');
INSERT INTO `sys_menu` VALUES ('114', '缓存列表', '2', '6', 'cacheList', 'monitor/cache/list', '', '', '1', '0', 'C', '0', '0', 'monitor:cache:list', 'redis-list', 'admin', '2024-10-20 19:53:20', '', null, '缓存列表菜单');
INSERT INTO `sys_menu` VALUES ('115', '表单构建', '3', '1', 'build', 'tool/build/index', '', '', '1', '0', 'C', '0', '0', 'tool:build:list', 'build', 'admin', '2024-10-20 19:53:20', '', null, '表单构建菜单');
INSERT INTO `sys_menu` VALUES ('116', '代码生成', '3', '2', 'gen', 'tool/gen/index', '', '', '1', '0', 'C', '0', '0', 'tool:gen:list', 'code', 'admin', '2024-10-20 19:53:20', '', null, '代码生成菜单');
INSERT INTO `sys_menu` VALUES ('117', '系统接口', '3', '3', 'swagger', 'tool/swagger/index', '', '', '1', '0', 'C', '0', '0', 'tool:swagger:list', 'swagger', 'admin', '2024-10-20 19:53:20', '', null, '系统接口菜单');
INSERT INTO `sys_menu` VALUES ('500', '操作日志', '108', '1', 'operlog', 'monitor/operlog/index', '', '', '1', '0', 'C', '0', '0', 'monitor:operlog:list', 'form', 'admin', '2024-10-20 19:53:20', '', null, '操作日志菜单');
INSERT INTO `sys_menu` VALUES ('501', '登录日志', '108', '2', 'logininfor', 'monitor/logininfor/index', '', '', '1', '0', 'C', '0', '0', 'monitor:logininfor:list', 'logininfor', 'admin', '2024-10-20 19:53:20', '', null, '登录日志菜单');
INSERT INTO `sys_menu` VALUES ('1000', '用户查询', '100', '1', '', '', '', '', '1', '0', 'F', '0', '0', 'system:user:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1001', '用户新增', '100', '2', '', '', '', '', '1', '0', 'F', '0', '0', 'system:user:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1002', '用户修改', '100', '3', '', '', '', '', '1', '0', 'F', '0', '0', 'system:user:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1003', '用户删除', '100', '4', '', '', '', '', '1', '0', 'F', '0', '0', 'system:user:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1004', '用户导出', '100', '5', '', '', '', '', '1', '0', 'F', '0', '0', 'system:user:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1005', '用户导入', '100', '6', '', '', '', '', '1', '0', 'F', '0', '0', 'system:user:import', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1006', '重置密码', '100', '7', '', '', '', '', '1', '0', 'F', '0', '0', 'system:user:resetPwd', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1007', '角色查询', '101', '1', '', '', '', '', '1', '0', 'F', '0', '0', 'system:role:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1008', '角色新增', '101', '2', '', '', '', '', '1', '0', 'F', '0', '0', 'system:role:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1009', '角色修改', '101', '3', '', '', '', '', '1', '0', 'F', '0', '0', 'system:role:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1010', '角色删除', '101', '4', '', '', '', '', '1', '0', 'F', '0', '0', 'system:role:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1011', '角色导出', '101', '5', '', '', '', '', '1', '0', 'F', '0', '0', 'system:role:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1012', '菜单查询', '102', '1', '', '', '', '', '1', '0', 'F', '0', '0', 'system:menu:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1013', '菜单新增', '102', '2', '', '', '', '', '1', '0', 'F', '0', '0', 'system:menu:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1014', '菜单修改', '102', '3', '', '', '', '', '1', '0', 'F', '0', '0', 'system:menu:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1015', '菜单删除', '102', '4', '', '', '', '', '1', '0', 'F', '0', '0', 'system:menu:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1016', '部门查询', '103', '1', '', '', '', '', '1', '0', 'F', '0', '0', 'system:dept:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1017', '部门新增', '103', '2', '', '', '', '', '1', '0', 'F', '0', '0', 'system:dept:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1018', '部门修改', '103', '3', '', '', '', '', '1', '0', 'F', '0', '0', 'system:dept:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1019', '部门删除', '103', '4', '', '', '', '', '1', '0', 'F', '0', '0', 'system:dept:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1020', '岗位查询', '104', '1', '', '', '', '', '1', '0', 'F', '0', '0', 'system:post:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1021', '岗位新增', '104', '2', '', '', '', '', '1', '0', 'F', '0', '0', 'system:post:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1022', '岗位修改', '104', '3', '', '', '', '', '1', '0', 'F', '0', '0', 'system:post:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1023', '岗位删除', '104', '4', '', '', '', '', '1', '0', 'F', '0', '0', 'system:post:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1024', '岗位导出', '104', '5', '', '', '', '', '1', '0', 'F', '0', '0', 'system:post:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1025', '字典查询', '105', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:dict:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1026', '字典新增', '105', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:dict:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1027', '字典修改', '105', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:dict:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1028', '字典删除', '105', '4', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:dict:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1029', '字典导出', '105', '5', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:dict:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1030', '参数查询', '106', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:config:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1031', '参数新增', '106', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:config:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1032', '参数修改', '106', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:config:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1033', '参数删除', '106', '4', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:config:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1034', '参数导出', '106', '5', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:config:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1035', '公告查询', '107', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:notice:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1036', '公告新增', '107', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:notice:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1037', '公告修改', '107', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:notice:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1038', '公告删除', '107', '4', '#', '', '', '', '1', '0', 'F', '0', '0', 'system:notice:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1039', '操作查询', '500', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:operlog:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1040', '操作删除', '500', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:operlog:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1041', '日志导出', '500', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:operlog:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1042', '登录查询', '501', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:logininfor:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1043', '登录删除', '501', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:logininfor:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1044', '日志导出', '501', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:logininfor:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1045', '账户解锁', '501', '4', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:logininfor:unlock', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1046', '在线查询', '109', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:online:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1047', '批量强退', '109', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:online:batchLogout', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1048', '单条强退', '109', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:online:forceLogout', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1049', '任务查询', '110', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:job:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1050', '任务新增', '110', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:job:add', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1051', '任务修改', '110', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:job:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1052', '任务删除', '110', '4', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:job:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1053', '状态修改', '110', '5', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:job:changeStatus', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1054', '任务导出', '110', '6', '#', '', '', '', '1', '0', 'F', '0', '0', 'monitor:job:export', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1055', '生成查询', '116', '1', '#', '', '', '', '1', '0', 'F', '0', '0', 'tool:gen:query', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1056', '生成修改', '116', '2', '#', '', '', '', '1', '0', 'F', '0', '0', 'tool:gen:edit', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1057', '生成删除', '116', '3', '#', '', '', '', '1', '0', 'F', '0', '0', 'tool:gen:remove', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1058', '导入代码', '116', '4', '#', '', '', '', '1', '0', 'F', '0', '0', 'tool:gen:import', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1059', '预览代码', '116', '5', '#', '', '', '', '1', '0', 'F', '0', '0', 'tool:gen:preview', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('1060', '生成代码', '116', '6', '#', '', '', '', '1', '0', 'F', '0', '0', 'tool:gen:code', '#', 'admin', '2024-10-20 19:53:20', '', null, '');
INSERT INTO `sys_menu` VALUES ('2003', '社区用户', '6', '1', 'comUser', 'system/user/comUser', null, '', '1', '0', 'C', '0', '0', 'system:user:list', 'user', 'admin', null, 'admin', null, '');
INSERT INTO `sys_menu` VALUES ('2004', '系统用户', '6', '2', 'sysUser', 'system/user/index', null, '', '1', '0', 'C', '0', '0', 'system:user:list', 'user', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2015', '信息1', '2021', '1', 'date1', 'system/travel/index', null, '', '1', '0', 'C', '0', '0', 'system:travel:list', '#', 'admin', '2024-11-07 17:28:07', '', null, '城市旅游菜单');
INSERT INTO `sys_menu` VALUES ('2016', '城市旅游查询', '2015', '1', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:travel:query', '#', 'admin', '2024-11-07 17:28:08', '', null, '');
INSERT INTO `sys_menu` VALUES ('2017', '城市旅游新增', '2015', '2', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:travel:add', '#', 'admin', '2024-11-07 17:28:08', '', null, '');
INSERT INTO `sys_menu` VALUES ('2018', '城市旅游修改', '2015', '3', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:travel:edit', '#', 'admin', '2024-11-07 17:28:08', '', null, '');
INSERT INTO `sys_menu` VALUES ('2019', '城市旅游删除', '2015', '4', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:travel:remove', '#', 'admin', '2024-11-07 17:28:08', '', null, '');
INSERT INTO `sys_menu` VALUES ('2020', '城市旅游导出', '2015', '5', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:travel:export', '#', 'admin', '2024-11-07 17:28:08', '', null, '');
INSERT INTO `sys_menu` VALUES ('2021', '旅游信息', '5', '1', 'travel', null, null, '', '1', '0', 'M', '0', '0', null, 'user', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2022', '美食信息', '5', '2', 'food', null, null, '', '1', '0', 'M', '0', '0', null, 'user', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2023', '美食数据', '2022', '1', 'food', 'system/food/index', null, '', '1', '0', 'C', '0', '0', 'system:food:list', '#', 'admin', '2024-11-07 18:31:02', '', null, '美食数据（1）菜单');
INSERT INTO `sys_menu` VALUES ('2024', '美食数据查询', '2023', '1', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:food:query', '#', 'admin', '2024-11-07 18:31:03', '', null, '');
INSERT INTO `sys_menu` VALUES ('2025', '美食数据新增', '2023', '2', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:food:add', '#', 'admin', '2024-11-07 18:31:03', '', null, '');
INSERT INTO `sys_menu` VALUES ('2026', '美食数据修改', '2023', '3', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:food:edit', '#', 'admin', '2024-11-07 18:31:03', '', null, '');
INSERT INTO `sys_menu` VALUES ('2027', '美食数据删除', '2023', '4', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:food:remove', '#', 'admin', '2024-11-07 18:31:03', '', null, '');
INSERT INTO `sys_menu` VALUES ('2028', '美食数据导出', '2023', '5', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:food:export', '#', 'admin', '2024-11-07 18:31:03', '', null, '');
INSERT INTO `sys_menu` VALUES ('2029', '新闻信息', '5', '3', 'news', null, null, '', '1', '0', 'M', '0', '0', null, 'user', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2035', '新闻列表', '2029', '1', 'news', 'system/news/index', null, '', '1', '0', 'C', '0', '0', 'system:news:list', '#', 'admin', '2024-11-07 18:55:31', '', null, '新闻列表菜单');
INSERT INTO `sys_menu` VALUES ('2036', '新闻列表查询', '2035', '1', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:news:query', '#', 'admin', '2024-11-07 18:55:31', '', null, '');
INSERT INTO `sys_menu` VALUES ('2037', '新闻列表新增', '2035', '2', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:news:add', '#', 'admin', '2024-11-07 18:55:31', '', null, '');
INSERT INTO `sys_menu` VALUES ('2038', '新闻列表修改', '2035', '3', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:news:edit', '#', 'admin', '2024-11-07 18:55:31', '', null, '');
INSERT INTO `sys_menu` VALUES ('2039', '新闻列表删除', '2035', '4', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:news:remove', '#', 'admin', '2024-11-07 18:55:31', '', null, '');
INSERT INTO `sys_menu` VALUES ('2040', '新闻列表导出', '2035', '5', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:news:export', '#', 'admin', '2024-11-07 18:55:31', '', null, '');
INSERT INTO `sys_menu` VALUES ('2050', '网络传播影响力', '7', '1', 'network', null, null, '', '1', '0', 'M', '0', '0', null, '#', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2051', '媒体报道影响力', '7', '2', 'media', null, null, '', '1', '0', 'M', '0', '0', null, '#', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2052', '社交媒体影响力', '7', '3', 'social', null, null, '', '1', '0', 'M', '0', '0', null, '#', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2053', '搜索引擎影响力', '7', '4', 'searche', null, null, '', '1', '0', 'M', '0', '0', null, '#', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2054', '国际访客影响力', '7', '4', 'tourism', null, null, '', '1', '0', 'M', '0', '0', null, '#', 'admin', null, '', null, '');
INSERT INTO `sys_menu` VALUES ('2055', '词云', '2050', '1', 'wordcloud', 'system/wordcloud/index', null, '', '1', '0', 'C', '0', '0', 'system:wordcloud:list', '#', 'admin', '2024-11-08 09:49:11', '', null, '词云菜单');
INSERT INTO `sys_menu` VALUES ('2056', '词云查询', '2055', '1', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:wordcloud:query', '#', 'admin', '2024-11-08 09:49:11', '', null, '');
INSERT INTO `sys_menu` VALUES ('2057', '词云新增', '2055', '2', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:wordcloud:add', '#', 'admin', '2024-11-08 09:49:11', '', null, '');
INSERT INTO `sys_menu` VALUES ('2058', '词云修改', '2055', '3', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:wordcloud:edit', '#', 'admin', '2024-11-08 09:49:11', '', null, '');
INSERT INTO `sys_menu` VALUES ('2059', '词云删除', '2055', '4', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:wordcloud:remove', '#', 'admin', '2024-11-08 09:49:11', '', null, '');
INSERT INTO `sys_menu` VALUES ('2060', '词云导出', '2055', '5', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:wordcloud:export', '#', 'admin', '2024-11-08 09:49:11', '', null, '');
INSERT INTO `sys_menu` VALUES ('2061', '纽约时报报道量', '2051', '1', 'counts', 'system/counts/index', null, '', '1', '0', 'C', '0', '0', 'system:counts:list', '#', 'admin', '2024-11-08 10:00:40', '', null, '纽约时报报道量菜单');
INSERT INTO `sys_menu` VALUES ('2062', '纽约时报报道量查询', '2061', '1', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:counts:query', '#', 'admin', '2024-11-08 10:00:40', '', null, '');
INSERT INTO `sys_menu` VALUES ('2063', '纽约时报报道量新增', '2061', '2', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:counts:add', '#', 'admin', '2024-11-08 10:00:40', '', null, '');
INSERT INTO `sys_menu` VALUES ('2064', '纽约时报报道量修改', '2061', '3', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:counts:edit', '#', 'admin', '2024-11-08 10:00:40', '', null, '');
INSERT INTO `sys_menu` VALUES ('2065', '纽约时报报道量删除', '2061', '4', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:counts:remove', '#', 'admin', '2024-11-08 10:00:40', '', null, '');
INSERT INTO `sys_menu` VALUES ('2066', '纽约时报报道量导出', '2061', '5', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:counts:export', '#', 'admin', '2024-11-08 10:00:40', '', null, '');
INSERT INTO `sys_menu` VALUES ('2067', '城市传播指数', '7', '5', 'cityattributes', 'system/cityattributes/index', null, '', '1', '0', 'C', '0', '0', 'system:cityattributes:list', '#', 'admin', '2024-11-08 11:55:09', '', null, '城市传播指数菜单');
INSERT INTO `sys_menu` VALUES ('2068', '城市传播指数查询', '2067', '1', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:cityattributes:query', '#', 'admin', '2024-11-08 11:55:09', '', null, '');
INSERT INTO `sys_menu` VALUES ('2069', '城市传播指数新增', '2067', '2', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:cityattributes:add', '#', 'admin', '2024-11-08 11:55:09', '', null, '');
INSERT INTO `sys_menu` VALUES ('2070', '城市传播指数修改', '2067', '3', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:cityattributes:edit', '#', 'admin', '2024-11-08 11:55:09', '', null, '');
INSERT INTO `sys_menu` VALUES ('2071', '城市传播指数删除', '2067', '4', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:cityattributes:remove', '#', 'admin', '2024-11-08 11:55:10', '', null, '');
INSERT INTO `sys_menu` VALUES ('2072', '城市传播指数导出', '2067', '5', '#', '', null, '', '1', '0', 'F', '0', '0', 'system:cityattributes:export', '#', 'admin', '2024-11-08 11:55:10', '', null, '');
