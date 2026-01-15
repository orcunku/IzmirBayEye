import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  theme: ThemeData.dark(),
  home: Scaffold(
    body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.waves, size: 80, color: Colors.cyan),
          Text("BAYEYE IZMIR", style: TextStyle(fontSize: 24, letterSpacing: 2)),
          Text("82%", style: TextStyle(fontSize: 90, color: Colors.redAccent, fontWeight: FontWeight.bold)),
          Text("CRITICAL ODOR RISK", style: TextStyle(color: Colors.orange)),
          SizedBox(height: 20),
          Text("O2 Level: 2.1 mg/L | Wind: 3 km/h"),
        ],
      ),
    ),
  ),
));
