import 'package:flutter/material.dart';
import 'Theme.dart' as Theme;

class SubscriptionRow extends StatefulWidget {
  String name;
  SubscriptionRow(this.name);

  @override
  _SubscriptionRowState createState() => _SubscriptionRowState();
}

class _SubscriptionRowState extends State<SubscriptionRow> {
  @override
  Widget build(BuildContext context) {
    final subscriptionThumbnail = Container(
      margin: const EdgeInsets.all(22),
      child: Material(

        elevation: 4.0,
        shape: CircleBorder(),

        clipBehavior: Clip.hardEdge,
        color: Colors.transparent,
        child: Ink.image(
          image: NetworkImage("https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png"),
          fit: BoxFit.cover,
          width: 75 ,
          height: 75,
          child: InkWell(
            splashColor: Colors.red,
            onTap: () {
              print("CircularAvatar");
            },
          ),
        ),
      ),
    );
//    new Container(
//      decoration: new BoxDecoration(
//        shape: BoxShape.circle,
//        clip
//      ),
//      // alignment: new FractionalOffset(0.0, 0.5),
//      margin: const EdgeInsets.all(5),
//      child: new Hero(
//        tag: widget.name,
//        child: new Image(
//          image: NetworkImage("https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png"),
//          height: Theme.Dimens.planetHeight,
//          width: Theme.Dimens.planetWidth,
//        ),
//      ),
//    );

    final subscriptionCard = SizedBox(
      width: 410,
      height: 120,
      child: new Container(
        margin: const EdgeInsets.all(10),
        decoration: new BoxDecoration(
          color: Colors.pink[50],
          shape: BoxShape.rectangle,
          borderRadius: new BorderRadius.circular(8.0),
          boxShadow: <BoxShadow>[
            new BoxShadow(color: Colors.grey,
                blurRadius: 15.0,
                offset: new Offset(0.0, 0.0))
          ],
        ),
        child: new Container(
          margin: const EdgeInsets.only(top: 6.0, left: 110.0),
          constraints: new BoxConstraints.expand(),
          child: new Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              new Text(widget.name),
              //new Text(planet.location, style: Theme.TextStyles.planetLocation),
//            new Container(
//                color: const Color(0xFF00C6FF),
//                width: 24.0,
//                height: 1.0,
//                margin: const EdgeInsets.symmetric(vertical: 8.0)
//            ),
              new Row(
                children: <Widget>[
//                new Icon(Icons.location_on, size: 14.0,
//                    color: Theme.Colors.planetDistance),
                  new Text("Subscription Details", style: Theme.TextStyles.planetDistance),
//                new Container(width: 20.0),
//                new Icon(Icons.flight_land, size: 14.0,
//                    color: Theme.Colors.planetDistance),
//                new Text(
//                    "hello", style: Theme.TextStyles.planetDistance),
                ],
              )
            ],
          ),
        ),
      ),
    );

    return new Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.pink[300],
        title: Text("Subscriptions"),
      ),

      body: new Column(
        children: <Widget>[
          Stack(
            children: <Widget>[
              subscriptionCard,
              subscriptionThumbnail,],
          ),
          SizedBox(height: 5,),
          Stack(
            children: <Widget>[
              subscriptionCard,
              subscriptionThumbnail,],
          ),
        ],
      ),

//      height: 50.0,
//      margin: const EdgeInsets.only(top: 16.0, bottom: 8.0),
//      child: new FlatButton(
//        //onPressed: () => _navigateTo(context, planet.id),
//
//
//      ),
    );
  }
}
