<?php

use Elasticsearch\Client;
use Elasticsearch\ClientBuilder;

$ClientBuilder = ClientBuilder::create()->setHosts($config['es']['hosts'])->setLogger(
    new class extends \Psr\Log\AbstractLogger {
        public function log($level, $message, array $context = array())
        {
            // 输出get uri
            $method = $context['method']??'';
            switch ($method){
                case 'GET':
                    echo $context['uri'].PHP_EOL;
                    break;
                case 'POST':
                    var_dump($context);
                    break;
                default:
                    break;
            }
        }
    }
);
$client = $ClientBuilder->build();

// 获取内置测试数据
//var_dump($client->get(['index'=>'kibana_sample_data_ecommerce','id'=>'dEOv1nMBRAHmuS0u8LWQ']));

return $client;