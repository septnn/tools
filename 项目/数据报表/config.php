<?php

$config = [
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
return $config;