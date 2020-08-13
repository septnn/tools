<?php

ini_set('error_reporting', E_ALL);
ini_set('display_errors', true);

$loader = include_once 'vendor/autoload.php';
$loader->unregister();
$loader->addPsr4('App\\', __DIR__);
$loader->register(true);

use App\Database;

new Database();