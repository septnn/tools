<?php

namespace App;

use App\Config;
use Elasticsearch\Client;
use Elasticsearch\ClientBuilder;

class Elasticsearch
{
    public static function get()
    {
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
        return $ClientBuilder->build();
    }
}

// 获取内置测试数据
//var_dump($client->get(['index'=>'kibana_sample_data_ecommerce','id'=>'dEOv1nMBRAHmuS0u8LWQ']));

//dd(Elasticsearch::get()->get(['index'=>'kibana_sample_data_ecommerce','id'=>'dEOv1nMBRAHmuS0u8LWQ']));

//var_dump($client->indices()->create([
//    'index' => 'order',
//    'body' => [
//        'settings' => [
//            'number_of_shards' => 2,
//            'auto_expand_replicas' => '0-1'
//        ],
//        'mappings' => [
//            'properties' => [
//                'source' => ['type' => 'keyword'],
//                'order_no' => ['type' => 'keyword'],
//                'shop_id' => ['type' => 'keyword'],
//                'shop_name' => ['type' => 'text'],
//                'company_no' => ['type' => 'keyword'],
//                'business_no' => ['type' => 'keyword'],
//                'customer_id' => ['type' => 'keyword'],
//                'customer_phone' => ['type' => 'keyword'],
//                'device_id' => ['type' => 'integer'],
//                'device_uid' => ['type' => 'integer'],
//                'amount_info' => [
//                    'properties' => [
//                        'goods_amount' => ['type' => 'integer'],
//                        'final_amount' => ['type' => 'integer'],
//                        'activity_amount' => ['type' => 'integer'],
//                        'coupon_amount' => ['type' => 'integer'],
//                        'discount_amount' => ['type' => 'integer'],
//                        'package_amount' => ['type' => 'integer'],
//                        'voucher_amount' => ['type' => 'integer'],
//                        'delivery_price' => ['type' => 'integer'],
//                        'delivery_original_price' => ['type' => 'integer'],
//                    ]
//                ],
//                'status' => ['type' => 'keyword'],
//                'order_create_time' => ['type' => 'date', 'format' => 'epoch_second']
//            ]
//        ]
//    ]
//]));exit;

//var_dump($client->indices()->delete(['index' => 'order']));exit;