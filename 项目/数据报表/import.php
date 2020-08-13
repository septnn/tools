<?php

namespace App;

include_once 'bootstrap.php';

use App\Elasticsearch;

$table = 'order_detail_20200801';
$orders = (new class extends \Illuminate\Database\Eloquent\Model{})->setTable($table)->newQuery();
$id = 0;
$size = 1000;
do{
    echo memory_get_usage();
    echo $id.PHP_EOL;
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
    }
    Elasticsearch::get()->bulk([
        'body' => $data
    ]);
    $id = $id + $size;
    echo memory_get_usage();
}while(true);
