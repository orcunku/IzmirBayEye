import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  home: Scaffold(
    backgroundColor: Colors.black,
    body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.waves, color: Colors.cyan, size: 80),
          Text("BayEye Izmir", style: TextStyle(color: Colors.white, fontSize: 30)),
          Text("82%", style: TextStyle(color: Colors.red, fontSize: 90, fontWeight: FontWeight.bold)),
          Text("STAY AWAY FROM COAST", style: TextStyle(color: Colors.orange)),
        ],
      ),
    ),
  ),
));
