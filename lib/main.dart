import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';
import 'package:carousel_slider/carousel_slider.dart';
import 'dart:math';
import 'package:flutter_scatter/flutter_scatter.dart';
import 'Subscriptions.dart';

Random random = new Random();

void main() => runApp(MaterialApp(home: Home()));

//List<CustomPaint> circles =  <CustomPaint>[
//  CustomPaint(painter: ShapesPainter(), child: Container(height: 700,)),
//];

class Circle {
  Offset center;
  double radius;
  Paint paint = Paint();

  Circle(Offset c, double r, Paint p) {
    center = c;
    radius = r;
    paint = p;
  }
}
bool setUp = false;
void setup() //backend
{
  if(!setUp)
    {
      for (int i = 0; i < 15; ++i) {
        Material circularAvatar = Material(
          elevation: 4.0,
          shape: CircleBorder(),

          clipBehavior: Clip.hardEdge,
          color: Colors.transparent,
          child: Ink.image(
            image: NetworkImage("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTC1u8SQNxmqTSpC1CZ5YtLbhwXQFrIKmyPkmjtR3-bgtjrY9yC&usqp=CAU"),
            fit: BoxFit.cover,
            width: 50 + random.nextInt(100).floorToDouble(),
            height: 50 + random.nextInt(100).floorToDouble(),
            child: InkWell(
              splashColor: Colors.red,
              onTap: () {
                print("CircularAvatar");
              },
            ),
          ),
        );
        CircleOne.add(circularAvatar);
      }
    }

}

List<Material> CircleOne = [];


//class ShapesPainter extends CustomPainter {
//  @override
//  void paint(Canvas canvas, Size size) {
//    List<Circle> circlesToBeDrawn =  <Circle>[];
//    print(circlesToBeDrawn.length);
//    for(int i = 0; i < 10; ++i) {
//      final paint = Paint();
//      paint.color = Colors.deepOrange;
//      // center of the canvas is (x,y) => (width/2, height/2)
//      var center = Offset(
//          random.nextInt((size.height / 2).round()).floorToDouble(),
//          random.nextInt((size.width / 2).round()).floorToDouble());
//      // draw the circle with center having radius 75.0
//      double radius = random.nextInt(100).floorToDouble();
//      Circle c = new Circle(center, radius, paint);
//      bool overlapping = false;
//      //canvas.drawCircle(center, radius, paint);
//
//      for(int j = 0; j <circlesToBeDrawn.length; ++j)
//        {
//
//          //canvas.drawCircle(center, radius, paint);
//
//          Circle other = circlesToBeDrawn[j];
//          paint.color = Colors.amber;
//
//          //canvas.drawCircle(other.center, other.radius, other.paint);
//
//          double d = (c.center - other.center).distance.abs();
//          print(d);
//          print(c.radius + other.radius);
//          if(d < c.radius + other.radius)
//            {
//              overlapping = true;
//              break;
//            }
//
//          if(!overlapping)
//          {
//            print("hello");
//
//            circlesToBeDrawn.add(c);
//            canvas.drawCircle(center, radius, paint);
//
//          }
//
//        }
//
//    }
//  }
//
//  @override
//  bool shouldRepaint(CustomPainter oldDelegate) => false;
//}

List<StaggeredTile> _staggeredTiles = const <StaggeredTile>[
  const StaggeredTile.count(2, 2),
  const StaggeredTile.count(2, 1),
  const StaggeredTile.count(2, 2),
  const StaggeredTile.count(2, 2),
  const StaggeredTile.count(1, 2),
  const StaggeredTile.count(1, 2),
  const StaggeredTile.count(1, 1),
  const StaggeredTile.count(1, 1),
  const StaggeredTile.count(3, 1),
  const StaggeredTile.count(1, 1),
  const StaggeredTile.count(4, 1),

];

List<Widget> _tiles = const <Widget>[
  const _FamilyTile(Colors.green, "https://i.pinimg.com/originals/4e/aa/07/4eaa071e822f3af2402f5311b700f0d1.jpg"),
  const _Example01Tile(Colors.lightBlue, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTghz2APs21H0k4W1LrACwQhnb6p8CoH1WU5ZP-hAhHIQt03PDe&usqp=CAU"),
  const _CarouselTile(),
  const _Example01Tile(Colors.amber, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTghz2APs21H0k4W1LrACwQhnb6p8CoH1WU5ZP-hAhHIQt03PDe&usqp=CAU"),
  const _Example01Tile(Colors.brown, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRzSxjt0GEoiXTt52rwTCvRZdA_GCQlkk1q4iNqBqO2yayd6a_z&usqp=CAU"),
  const _Example01Tile(Colors.deepOrange, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRzSxjt0GEoiXTt52rwTCvRZdA_GCQlkk1q4iNqBqO2yayd6a_z&usqp=CAU"),
  const _Example01Tile(Colors.indigo, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR9Xo-Ec26iN0VPb-aIKqxDHGzxGVt39gqX7eRbua2NIBWM7xwc&usqp=CAU"),
  const _Example01Tile(Colors.pink, "https://cdn.iconscout.com/icon/free/png-512/medical-127-129383.png"),
  const _Example01Tile(Colors.purple, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRzSxjt0GEoiXTt52rwTCvRZdA_GCQlkk1q4iNqBqO2yayd6a_z&usqp=CAU"),
  const _Example01Tile(Colors.blue, "https://img.icons8.com/cotton/2x/settings.png"),
  const _Example01Tile(Colors.blue, "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRzSxjt0GEoiXTt52rwTCvRZdA_GCQlkk1q4iNqBqO2yayd6a_z&usqp=CAU"),

];

class _FamilyTile extends StatelessWidget {
  const _FamilyTile(this.backgroundColor, this.imageData);

  final Color backgroundColor;
  final String imageData;

  @override
  Widget build(BuildContext context) {
    return new Card(
      color: backgroundColor,
      child: new InkWell(
        child: Container(
          width: double.infinity,
          child: Image(
              image: NetworkImage(imageData),
              fit: BoxFit.cover
          ),
        ),
        onTap: () {
          setup();
          setUp = true;
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => Family()),
          );
        },
      ),
    );
  }
}
class _Example01Tile extends StatelessWidget {
  const _Example01Tile(this.backgroundColor, this.imageData);

  final Color backgroundColor;
  final String imageData;

  @override
  Widget build(BuildContext context) {
    return new Card(
        color: backgroundColor,
        child: new InkWell(
          child: Container(
            width: double.infinity,
            child: Image(
                image: NetworkImage(imageData),
                fit: BoxFit.cover
            ),
          ),
          onTap: () {
          },
        ),
    );
  }
}

class _CarouselTile extends StatelessWidget {
  const _CarouselTile();

  @override
  Widget build(BuildContext context) {
    return new Card(
      child: new InkWell(
        onTap: () {},
        child: CarouselSlider(
          viewportFraction: 1.0,
          autoPlay: true,
          autoPlayInterval: Duration(seconds: 3),
          items: [
            'https://cdn.vox-cdn.com/thumbor/Yq1Vd39jCBGpTUKHUhEx5FfxvmM=/39x0:3111x2048/1200x800/filters:focal(39x0:3111x2048)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png',
            'https://m.media-amazon.com/images/G/01/digital/video/acquisition/amazon_video_light_on_dark.png'
          ].map((i) {
            return Builder(
              builder: (BuildContext context) {
                return InkWell(
                  child: Container(
                      width: double.infinity,
                      child: Image.network(i, fit: BoxFit.cover)),
                  onTap: () {
                    Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => SubscriptionRow('Netflix')),
                  );
                  }

                );
              },
            );
          }).toList(),
        ),
      ),
    );
  }
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.black45,
        appBar: AppBar(
//          leading: GestureDetector(
//            onTap: () {},
//            child: IconButton(
//              icon: Icon(
//                Icons.menu,
//                color: Colors.white,
//              ),
//            ),
//          ),
          title: Text('DigiFam'),
          centerTitle: true,
          backgroundColor: Colors.green[400],
//          actions: <Widget>[
//            IconButton(
//              icon: Icon(
//                Icons.settings,
//                color: Colors.white,
//              ),
//            ),
//          ],
        ),
        body: Padding(
            padding: const EdgeInsets.only(top: 1),
            child: StaggeredGridView.count(
              crossAxisCount: 4,
              staggeredTiles: _staggeredTiles,
              children: _tiles,
              mainAxisSpacing: 1,
              crossAxisSpacing: 1,
              padding: const EdgeInsets.only(top: 1, bottom: 0, left: 3, right: 3),
            ))
//        Center(
//            child: Stack(
//              children: <Widget>[
//                Padding(
//                  padding: const EdgeInsets.only(
//                    top: 30,
//                    left: 25,
//                  ),
//                  child: Text(
//                    "Hello <Username>",     //backend
//                    style: TextStyle(
//                        fontSize: 40.0
//                    ),
//                  ),
//                ),
//                StaggeredGridView.countBuilder(
//                  crossAxisCount: 4,
//                  itemBuilder: (BuildContext context, int index) => new Container(
//                      color: Colors.amberAccent,
//                      child: new Center(
//                        child: Text("hello"),
//                      )
//                  ),
//                  staggeredTileBuilder: (int index) =>
//                      StaggeredTile.count(2, index.isEven ? 2: 1),
//
//                  mainAxisSpacing: 4.0,
//                  crossAxisSpacing: 4.0,
//                ),
//
//
//              ],
//            )
//
//        )

    );
  }
}

class Family extends StatefulWidget {
  @override
  _FamilyState createState() => _FamilyState();
}

class _FamilyState extends State<Family> {
  @override
  Widget build(BuildContext context) {
    final screenSize = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        title: Text("Family"),
      ),
      body: Center(
        child: FittedBox(
          child: Scatter(
            fillGaps: true,
            delegate: ArchimedeanSpiralScatterDelegate(a: 10, b: 18),
            children: CircleOne,
          ),
        ),
      ),
    );
  }
}
