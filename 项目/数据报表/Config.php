<?php

namespace App;

use Illuminate\Contracts\Config\Repository;

class Config implements Repository
{
    protected $items = [
        'mysql' => [
            'ssd_aos' => [
                'driver'    => 'mysql',
                'host'      => 'ssd-default.mysql.rds.aliyuncs.com',
                'database'  => 'ssd_aos',
                'username'  => 'dev',
                'password'  => 'Ka^2LPqn8',
                'charset'   => 'utf8',
            ]
        ],
        'es' => [
            'hosts' => ['http://192.168.99.100:9200'],
        ]
    ];

    public function __construct(Array $items = [])
    {
        $this->items = array_merge($this->items, $items);
    }

    public function has($key)
    {
        return isset($this->items[$key]);
    }

    public function get($key, $default = null)
    {
        return $this->has($key) ? $this->items[$key] : $default ;
    }

    public function all()
    {
        return $this->items;
    }

    public function set($key, $value = null)
    {
        return array_merge($this->items, [$key => $value]);
    }

    public function prepend($key, $value)
    {
        return array_merge($this->items, [$key => $value]);
    }

    public function push($key, $value)
    {
        return $this->set($key, $value);
    }
}
