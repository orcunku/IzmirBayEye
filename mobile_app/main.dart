import 'package:flutter/material.dart';

void main() => runApp(BayEyeMobile());

class BayEyeMobile extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark(),
      home: Scaffold(
        appBar: AppBar(
          title: Text("BayEye: Izmir"),
          backgroundColor: Colors.blueGrey[900],
        ),
        body: Container(
          padding: EdgeInsets.all(20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // This represents the Status Icon
              Icon(Icons.warning_amber_rounded, size: 100, color: Colors.orangeAccent),
              SizedBox(height: 20),
              Text("Current Odor Risk", style: TextStyle(fontSize: 22)),
              
              // This shows the Risk Score from your Python API
              Text(
                "82%", 
                style: TextStyle(fontSize: 80, fontWeight: FontWeight.bold, color: Colors.redAccent)
              ),
              
              Divider(color: Colors.white24),
              Text(
                "Recommendation: High sulfide levels detected. Municipality teams have been notified.",
                textAlign: TextAlign.center,
                style: TextStyle(fontStyle: FontStyle.italic, color: Colors.grey[400]),
              ),
              SizedBox(height: 30),
              
              // A button for citizens to report odor manually
              ElevatedButton(
                onPressed: () {}, 
                child: Text("Report Local Odor"),
                style: ElevatedButton.styleFrom(backgroundColor: Colors.blueAccent),
              )
            ],
          ),
        ),
      ),
    );
  }
}
