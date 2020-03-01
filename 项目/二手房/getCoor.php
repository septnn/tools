<?php
$s = '1:和平区实验小学,
2:和平区中心小学,
3:和平区鞍山道小学,
4:和平区昆鹏小学,
5:和平区逸阳小学,
6:河北区育婴里小学,
7:和平区模范小学,
8:和平区万全小学,
9:河东区实验小学,
10:河西区上海道小学,
11:河西区师大二附小,
12:红桥区求真小学,
13:河北区昆一小学,
14:河北区扶轮小学,
15:南开区东方小学,
16:南开区中营小学,
17:河东区一中心小学,
18:红桥区六一小学,
19:河西区中心小学,
20:河西区闽侯路小学,
21:和平区昆明路小学,
22:南开区未来小学,
23:和平区新华南路小学,
24:南开区南大附小,
25:河西区三水道小学,
26:河北区实验小学,
27:河西区台湾路小学,
28:南开区五马路小学,
29:南开区天大附小,
30:和平区岳阳道小学,
31:南开区翔宇小学,
32:和平区耀华小学,
33:河东区缘诚小学,
34:河西区华江里小学,
35:和平区二十中学附小';

$s = str_replace("\n", '', $s);
$s = explode(',', $s);
print_r($s);
$key = 'jzWPDpvR5sv5q8HYadnjK7ICl7dr6Kn5';
$url = 'http://api.map.baidu.com/geocoding/v3/?output=json&ak='.$key.'&address=';
$school = [];
foreach($s as $key => $value) {
    $name = explode(':', $value);
    $res = json_decode(file_get_contents($url.$name[1]), 1);
    $school[] = [
        'name' => $name[1],
        'coor' => [
            'lng' => $res['result']['location']['lng'],
            'lat' => $res['result']['location']['lat'],
            ]
    ];
}

$json = json_encode($school, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
file_put_contents('./school.json', $json);
$json = "var school = ".$json;
file_put_contents('./school.js', $json);