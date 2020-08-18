<?php

namespace App;

include_once __DIR__ . '\bootstrap.php';

use App\Elasticsearch;

class Import
{
    public function run()
    {
        $date = [20200813];
        foreach ($date as $item){
            $table = 'order_detail_'.$item;
            echo $table.PHP_EOL;
            $orders = (new class extends \Illuminate\Database\Eloquent\Model{})->setTable($table)->newQuery();
            $id = 0;
            $size = 2000;
            $count = 0;
            do{
                echo 'id:'.$id.PHP_EOL;
//                echo 'do:'.memory_get_usage().PHP_EOL;
                $orders->wheres = []; // 重置条件
                $orders->where('id', '>', $id);
                $orders->limit($size);
                if($orders->count() <= 0) {
                    break;
                }
                $data = [];
                foreach ($orders->cursor() as $value) {
                    $value->amount_info = @json_decode($value->amount_info);
                    $data[] = [
                        'index' => [
                            '_index' => 'order'
                        ],
                    ];
                    $data[] = [
                        'source' => $value->source,
                        'order_no' => $value->order_no,
                        'shop_id' => $value->shop_id,
                        'shop_name' => $value->shop_name,
                        'company_no' => $value->company_no,
                        'business_no' => $value->business_no,
                        'customer_id' => $value->customer_id,
                        'customer_phone' => $value->customer_phone,
                        'device_id' => (int)$value->device_id,
                        'device_uid' => (int)$value->device_uid,
                        'amount_info' => [
                            'goods_amount' => (int)$value->amount_info->goods_amount,
                            'final_amount' => (int)$value->amount_info->final_amount,
                            'activity_amount' => (int)$value->amount_info->activity_amount,
                            'coupon_amount' => (int)$value->amount_info->coupon_amount,
                            'discount_amount' => (int)$value->amount_info->discount_amount,
                            'package_amount' => (int)$value->amount_info->package_amount,
                            'voucher_amount' => (int)$value->amount_info->voucher_amount,
                            'delivery_price' => (int)$value->amount_info->delivery_price,
                            'delivery_original_price' => (int)$value->amount_info->delivery_original_price,
                        ],
                        'status' => $value->status,
                        'order_create_time' => $value->order_create_time,
                    ];
                    $id = $value->id;
                }
                $count = $count + count($data);
                echo 'count:'.$count.PHP_EOL;
//                echo 'Elasticsearch:'.memory_get_usage().PHP_EOL;
                Elasticsearch::get()->bulk([
                    'body' => $data
                ]);
//                echo 'do end:'.memory_get_usage().PHP_EOL;
            }while(true);
        }
    }

    public function createIndex()
    {
        var_dump(Elasticsearch::get()->indices()->create([
            'index' => 'order',
            'body' => [
                'settings' => [
                    'number_of_shards' => 2,
                    'auto_expand_replicas' => '0-1'
                ],
                'mappings' => [
                    'properties' => [
                        'source' => ['type' => 'keyword'],
                        'order_no' => ['type' => 'keyword'],
                        'shop_id' => ['type' => 'keyword'],
                        'shop_name' => ['type' => 'text'],
                        'company_no' => ['type' => 'keyword'],
                        'business_no' => ['type' => 'keyword'],
                        'customer_id' => ['type' => 'keyword'],
                        'customer_phone' => ['type' => 'keyword'],
                        'device_id' => ['type' => 'integer'],
                        'device_uid' => ['type' => 'integer'],
                        'amount_info' => [
                            'properties' => [
                                'goods_amount' => ['type' => 'integer'],
                                'final_amount' => ['type' => 'integer'],
                                'activity_amount' => ['type' => 'integer'],
                                'coupon_amount' => ['type' => 'integer'],
                                'discount_amount' => ['type' => 'integer'],
                                'package_amount' => ['type' => 'integer'],
                                'voucher_amount' => ['type' => 'integer'],
                                'delivery_price' => ['type' => 'integer'],
                                'delivery_original_price' => ['type' => 'integer'],
                            ]
                        ],
                        'status' => ['type' => 'keyword'],
                        'order_create_time' => ['type' => 'date', 'format' => 'epoch_second']
                    ]
                ]
            ]
        ]));
    }

    public function truncate()
    {
        var_dump(Elasticsearch::get()->indices()->delete(['index' => 'order']));exit;
    }
}

(new Import())->run();

//(new Import())->createIndex();

//(new Import())->truncate();