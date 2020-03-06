<?php


function small($isOpen = false) {
    if($isOpen === false) return false;
    $s = '和平区实验小学,和平区中心小学,和平区鞍山道小学,和平区昆鹏小学,和平区逸阳小学,河北区育婴里小学,和平区模范小学,和平区万全小学,河东区实验小学,河西区上海道小学,河西区师大二附小,红桥区求真小学,河北区昆一小学,河北区扶轮小学,南开区东方小学,南开区中营小学,河东区一中心小学,红桥区六一小学,河西区中心小学,河西区闽侯路小学,和平区昆明路小学,南开区未来小学,和平区新华南路小学,南开区南大附小,河西区三水道小学,河北区实验小学,河西区台湾路小学,南开区五马路小学,南开区天大附小,和平区岳阳道小学,南开区翔宇小学,和平区耀华小学,河东区缘诚小学,河西区华江里小学,和平区二十中学附小学';

    $s = str_replace("\n", '', $s);
    $s = explode(',', $s);
    print_r($s);
    $key = 'jzWPDpvR5sv5q8HYadnjK7ICl7dr6Kn5';
    $url = 'http://api.map.baidu.com/geocoding/v3/?output=json&ak='.$key.'&address=';
    $small = [];
    foreach($s as $key => $value) {
        $name = $value;
        $res = json_decode(file_get_contents($url.$name), 1);
        $small[] = [
            'school' => '小学',
            'name' => $name,
            'coor' => [
                'lng' => $res['result']['location']['lng'],
                'lat' => $res['result']['location']['lat'],
                ]
        ];
    }

    $json = json_encode($small, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
    file_put_contents('./small.json', $json);
    $json = "var small = ".$json;
    file_put_contents('./small.js', $json);
}


function middle($isOpen = false) {
    if($isOpen === false) return false;
    $s = '天津耀华中学,天津南开中学,天津第一中学,天津实验中学,天津市第二十中学,天津市第一百中学,天津新华中学,天津七中,天津市第42中学,天津市第五十五中学,天津外国语学院附属中学,天津一中';

    $s = str_replace("\n", '', $s);
    $s = explode(',', $s);
    print_r($s);
    $key = 'jzWPDpvR5sv5q8HYadnjK7ICl7dr6Kn5';
    $url = 'http://api.map.baidu.com/geocoding/v3/?output=json&ak='.$key.'&address=';
    $middle = [];
    foreach($s as $key => $value) {
        $name = $value;
        $res = json_decode(file_get_contents($url.$name), 1);
        $middle[] = [
            'school' => '初中',
            'name' => $name,
            'coor' => [
                'lng' => $res['result']['location']['lng'],
                'lat' => $res['result']['location']['lat'],
                ]
        ];
    }

    $json = json_encode($middle, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
    file_put_contents('./middle.json', $json);
    $json = "var middle = ".$json;
    file_put_contents('./middle.js', $json);
}

middle(true);