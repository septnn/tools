import 'dart:async';
import 'dart:io';

import 'package:flutter/material.dart';
import 'dart:math';
import 'package:image_picker/image_picker.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
// import 'package:http/http.dart' as http;
import 'package:dio/dio.dart';
// import 'package:path_provider/path_provider.dart';

void main() => runApp(MyApp());

// 应用入口文件
class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  // 这个插件是应用根目录
  
  // 重写build函数，初始化
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      localizationsDelegates: [
        // 本地化代理
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ],
      supportedLocales: [
          const Locale('en', 'US'), // 美国英语
          const Locale('zh', 'CN'), // 中文简体
          //其它Locales
        ],
      title: 'Xiao V',
      theme: ThemeData(
        // This is the theme of your application.
        // 这个是应用的主题
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Xiao V'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  // 构造方法
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".
  // 定义变量
  String title;
  // 重写 创建可变状态
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _talk = 'Hi, I am Xiao V';
  File image;

  List replyTalkList = [
    '你好',
    'Hello', // 英语
    'こんにちは', // 日语
    'Hallo', // 德语
    'Здравствыйте', // 俄语
  ];
  void _replyTalk() {
    String _rand = replyTalkList[new Random().nextInt(replyTalkList.length)];
    setState(() {
      _talk = _rand;
    });
  }
  // 打开相机
  void _openImagePicker(ImageSource source) async {
    // gallery 相册
    // camera 相机
    print(source);
    try {
      image = await ImagePicker.pickImage(source: source);
    } catch (e) {
      print(e);
    }
    setState(() {
        // _image = image;
    });
  }
  // 相机回调
  Future<void> _callImagePicker() async {
    final LostDataResponse response = await ImagePicker.retrieveLostData();
    if (response.isEmpty) {
      return;
    }
    setState(() {
      image = response.file;
    });
  }
  void _upload(image) async {
    String token = '23.55dd958bdfcffed88d1e1a5ad3f34376.2592000.1561430482.302801485-238347';
    String url = "https://c.pcs.baidu.com/rest/2.0/pcs/file?method=upload&access_token="+token+"&path=/apps/pcstest_oauth/test/file.jpg";
    FormData formData = new FormData.from({
      "file": new UploadFileInfo(new File(image.path), "file.jpg"),
    });
    Dio dio = new Dio();
    var response = await dio.post(url, data: formData);
    print(response.data);
  }
  // 显示照片
  Widget _shoImagePicker() {
    if (image != null) {
      _upload(image);
      return Image.file(image, width: 300.0, height: 300.0);
    } else {
      return Text('等待拍照');
    }
  }
  // 打开相册
  void _openImagePickerGallery() async{
    try {
      image = await ImagePicker.pickImage(source: ImageSource.gallery);
    } catch (e) {
      print(e);
    }
    setState(() {
        // _image = image;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              '$_talk',
            ),
            Container(
              // color: Colors.blueAccent,
              alignment: new Alignment(1.0, 0.0),
              width: 100.0,
              height: 100.0,
              decoration: BoxDecoration(
                // color: Colors.grey[200],
                // shape: BoxShape.circle,
                shape: BoxShape.rectangle,
                image: DecorationImage(
                  image: AssetImage('img/logo.png'),
                ),
                // border: Border.all(color: Colors.blueGrey, width: 2.0),
              ),
            ),
            Container(
              child : new MaterialButton(
                  color: Colors.blue,
                  textColor: Colors.white,
                  child: new Text('Hi Xiao'),
                  onPressed: _replyTalk,
              ),
            ),
            Container(
              child: FutureBuilder(
                future: _callImagePicker(),
                builder: (BuildContext context, AsyncSnapshot<void> snapshort){
                  return _shoImagePicker();
                },
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        children: <Widget>[
          FloatingActionButton(
            onPressed: () {
              // print(ImageSource.camera);
              _openImagePicker(ImageSource.camera);
            },
            tooltip: '拍照',
            child: Icon(Icons.camera_alt),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 16.0), 
            child: FloatingActionButton(
              onPressed: () {
                // print(ImageSource.camera);
                _openImagePicker(ImageSource.camera);
              },
              tooltip: '录像',
              child: Icon(Icons.video_library),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 16.0), 
            child: FloatingActionButton(
              onPressed: () {
                _openImagePickerGallery();
              },
              tooltip: '上传',
              child: Icon(Icons.photo_library),
            ),
          )
        ],
      )
       // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
