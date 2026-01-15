import 'package:flutter/material.dart';

// UI Prototype for Citizen Monitoring App
void main() => runApp(MaterialApp(
  theme: ThemeData.dark(),
  home: Scaffold(
    body: Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(begin: Alignment.topCenter, colors: [Colors.blueGrey[900]!, Colors.black])
      ),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("IZMIR BAY STATUS", style: TextStyle(letterSpacing: 2, color: Colors.cyan)),
            SizedBox(height: 20),
            Text("82%", style: TextStyle(fontSize: 100, fontWeight: FontWeight.bold, color: Colors.redAccent)),
            Text("ODOR RISK LEVEL", style: TextStyle(fontSize: 18)),
            SizedBox(height: 40),
            InfoTile(Icons.opacity, "Oxygen", "2.1 mg/L"),
            InfoTile(Icons.thermostat, "Temp", "32.4 °C"),
            InfoTile(Icons.air, "Wind", "3.2 km/h"),
          ],
        ),
      ),
    ),
  ),
));

class InfoTile extends StatelessWidget {
  final IconData icon; final String label; final String val;
  InfoTile(this.icon, this.label, this.val);
  @override
  Widget build(BuildContext context) => Padding(
    padding: EdgeInsets.symmetric(vertical: 5),
    child: Row(mainAxisSize: MainAxisSize.min, children: [
      Icon(icon, size: 20, color: Colors.cyan),
      SizedBox(width: 10),
      Text("$label: $val", style: TextStyle(fontSize: 16))
    ]),
  );
}
