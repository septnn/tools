<?php

use Illuminate\Database\Capsule\Manager;
use Illuminate\Events\Dispatcher;
use Illuminate\Container\Container;

// 初始化db，setConnectionResolver、setEventDispatcher
$manager = new Manager();
$manager->addConnection($config['mysql']['ssd_aos']);
$manager->setEventDispatcher(new Dispatcher(new Container));
$manager->setAsGlobal();
$manager->bootEloquent();

return $manager;