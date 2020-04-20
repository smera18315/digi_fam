import 'package:flutter/material.dart';
import 'Theme.dart' as Theme;

class FamilySearch extends StatefulWidget {
  FamilySearch();

  @override
  _FamilySearchState createState() => _FamilySearchState();
}

class _FamilySearchState extends State<FamilySearch> {
  @override
  Widget build(BuildContext context) {

    final searchOption =
    Center(
      child: RaisedButton(
        child: Text("Option"),
        onPressed: () {
//        Navigator.push(
//          context,
//          MaterialPageRoute(
//              builder: (context) => SecondPage(
//                data: data,
//              )),
//        );
        },
      ),
    );
    return new Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.pink[300],
        title: Text("Subscriptions"),
      ),

      body: new Column(
        children: <Widget>[
          Center(
            child: RaisedButton(
              child: Text("Get top 100 family members"),
              onPressed: () {
//                    Navigator.push(
//                      context,
//                      MaterialPageRoute(
//                          builder: (context) => SecondPage(
//                            data: data,
//                          )),
//                    );
              },
            ),
          ),
          SizedBox(height: 5,),
          Center(
            child: RaisedButton(
              child: Text("Get top 100 family members"),
              onPressed: () {
//                    Navigator.push(
//                      context,
//                      MaterialPageRoute(
//                          builder: (context) => SecondPage(
//                            data: data,
//                          )),
//                    );
              },
            ),
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
