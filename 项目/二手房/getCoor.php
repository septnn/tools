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
    $s = '天津耀华中学,天津南开中学,天津第一中学,天津实验中学,天津市第二十中学,天津市第一百中学,天津新华中学,天津七中,天津市第42中学,天津市第五十五中学,天津外国语学院附属中学,天津一中,';

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

/**
 * 天津南开中学
天津第一中学
天津耀华中学
天津新华中学
天津实验中学
天津第二十中学
天津第二南开中学
天津中学
天津南开大学附属中学
天津大学附属中学
天津海河中学
天津第四十五中学
天津第七中学
天津王庄子中学
天津大白庄镇初级中学
天津王庆坨镇初级中学
天津汊沽港镇初级中学
天津邦均镇初级中学
天津东塔庄镇初级中学
天津双建中学分校
天津大白庄高级中学
天津大口屯高级中学
天津林亭口高级中学
天津求真高级中学
天津第三职工中学
天津外国语学院附中
天津津沽实验中学
天津河北外国语中学
天津天华实验中学
天津大港油田实验中学
天津第一百中学
天津外国语高级中学
天津市南开外国语中学
天津卓群高级中学
天津华泽高级中学
天津育才中学
天津第三十二中学
天津第一职工中学
天津蓟县上仓镇初级中学
天津翔东高级中学
天津天骄高级中学
天津
天津白古屯乡初级中学
天津黄庄乡初级中学
天津大沙河乡初级中学
天津市宝坻区霍各庄镇初级中学
天津南蔡村镇初级中学
天津宝坻区赵各庄镇初级中学
天津宝坻区王卜庄镇初级中学
天津宝坻区口东镇初级中学
天津宝坻区马家店镇初级中学
天津徐庄子中学
天津豆张庄初级中学
天津下里庄初级中学
天津乡初级中学
天津美术中学
天津第四十二中学
天津汇文中学
天津河北区第十四中学
天津育贤中学
天津第九十中学
天津第四十八中学
天津枫林路中学
天津北京师范大学附属中学
天津第五十七中学
天津双建中学
天津第五十四中学
天津小淀中学
天津佟楼中学
天津崇化中学
天津第九十三中学
天津第七十八中学
天津黄花店中学
天津双水道中学
天津苗庄中学
天津第九十八中学
天津华杰中学
天津第八十二中学
天津艺术中学
天津华光中学
天津新港中学
天津市东丽中学
天津嘉陵道中学
天津大沽中学
天津星座中学
天津育英中学
天津王稳庄中学
天津滨江中学
天津第九十五中学
天津潘庄镇中学
天津昆山道中学
天津丰年中学
天津天成中学
天津大寺中学
天津市兴南中学
天津津北中学
天津市塘沽区第十四中学
天津冠华中学
天津博文中学
 */