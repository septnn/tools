<?php

ini_set('error_reporting', E_ALL);
ini_set('display_errors', true);

$loader = include_once __DIR__ . '\vendor/autoload.php';
$loader->unregister();
$loader->addPsr4('App\\', __DIR__); // 注册当前当前项目命名空间
$loader->register(true);

use App\Database;
// 初始化数据库
new Database();