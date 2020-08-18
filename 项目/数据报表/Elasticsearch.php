<?php

namespace App;

use App\Config;
use Elasticsearch\Client;
use Elasticsearch\ClientBuilder;

class Elasticsearch
{
    private static $client;

    public static function get()
    {
        if(self::$client instanceof Client) {
            return self::$client;
        }
        $ClientBuilder = ClientBuilder::create()->setHosts((new Config)->get('es')['hosts'])->setLogger(
            new class extends \Psr\Log\AbstractLogger {
                public function log($level, $message, array $context = array())
                {
                    // 输出get uri
                    $method = $context['method']??'';
                    switch ($method){
                        case 'GET':
//                            echo $context['uri'].PHP_EOL;
                            break;
                        case 'POST':
//                            var_dump($context);
                            break;
                        default:
                            break;
                    }
                }
            }
        );
        self::$client = $ClientBuilder->build();
        return self::$client;
    }
}

// 获取内置测试数据
//var_dump($client->get(['index'=>'kibana_sample_data_ecommerce','id'=>'dEOv1nMBRAHmuS0u8LWQ']));

//dd(Elasticsearch::get()->get(['index'=>'kibana_sample_data_ecommerce','id'=>'dEOv1nMBRAHmuS0u8LWQ']));



//var_dump($client->indices()->delete(['index' => 'order']));exit;