<?php

namespace App;

use Illuminate\Database\Capsule\Manager;
use Illuminate\Events\Dispatcher;
use Illuminate\Container\Container;
use App\Config;

class Database
{
    public function __construct()
    {
        // 初始化db，setConnectionResolver、setEventDispatcher
        $manager = new Manager();
        $manager->addConnection((new Config())->get('mysql')['ssd_aos']);
        $manager->setEventDispatcher(new Dispatcher(new Container));
        $manager->setAsGlobal();
        $manager->bootEloquent();
    }
}
