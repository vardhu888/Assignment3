<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pathfinding Algorithms Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f5f7fa;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background: #eee;
            padding: 4px 6px;
            border-radius: 5px;
        }
        pre {
            background: #1e1e1e;
            color: #fff;
            padding: 12px;
            border-radius: 8px;
            overflow-x: auto;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        ul {
            margin-left: 20px;
        }
        .highlight {
            background: #e8f4ff;
            padding: 10px;
            border-left: 5px solid #3498db;
            margin: 15px 0;
        }
    </style>
</head>
<body>

<div class="container">

<h1>🚀 Pathfinding Algorithms Project</h1>

<p>This project demonstrates the implementation of popular pathfinding algorithms using Python. It includes:</p>

<ul>
    <li>A* Algorithm (static grid)</li>
    <li>A* with Dynamic Obstacles (real-time replanning)</li>
    <li>Dijkstra’s Algorithm (real-world city graph)</li>
</ul>

<hr>

<h2>📁 Project Files</h2>
<ul>
    <li><b>A* Grid Pathfinding</b> → astar.py</li>
    <li><b>Dynamic Path Planning (A*)</b> → ugv1.py</li>
    <li><b>Dijkstra on Indian Cities Dataset</b> → dijikstra_india.py</li>
    <li><b>Dataset</b> → india_cities_distances.csv</li>
</ul>

<hr>

<h2>🧠 Algorithms Used</h2>

<h3>1. A* Algorithm (Static Environment)</h3>
<ul>
    <li>Uses Manhattan distance heuristic</li>
    <li>Works on a 70×70 grid</li>
    <li>Supports obstacle densities: low, medium, high</li>
</ul>

<div class="highlight">
<b>Outputs:</b>
<ul>
    <li>Path found or not</li>
    <li>Path length</li>
    <li>Nodes explored</li>
</ul>
</div>

<h3>2. Dynamic Path Planning (A*)</h3>
<ul>
    <li>Simulates real-world uncertainty</li>
    <li>Obstacles appear during execution</li>
    <li>Automatically replans path</li>
</ul>

<div class="highlight">
<b>Grid Symbols:</b>
<ul>
    <li>S → Start</li>
    <li>G → Goal</li>
    <li># → Obstacle</li>
    <li>* → Path</li>
</ul>
</div>

<h3>3. Dijkstra Algorithm (City Graph)</h3>
<ul>
    <li>Uses dataset of Indian cities</li>
    <li>Computes shortest distance from a source city</li>
    <li>Graph is undirected</li>
</ul>

<hr>

<h2>⚙️ Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>No external libraries required</li>
</ul>

<hr>

<h2>▶️ How to Run</h2>

<h3>Run A* (Static Grid)</h3>
<pre>python astar.py</pre>
<p>Enter: <code>low / medium / high</code></p>

<h3>Run Dynamic A*</h3>
<pre>python ugv1.py</pre>

<h3>Run Dijkstra</h3>
<pre>python dijikstra_india.py</pre>
<p>Then enter a city name from the list.</p>

<hr>

<h2>📊 Use Cases</h2>
<ul>
    <li>Robotics navigation</li>
    <li>Game AI</li>
    <li>Route optimization</li>
    <li>Autonomous vehicles</li>
</ul>

<hr>

<h2>📌 Key Concepts</h2>
<ul>
    <li>Heuristic search (A*)</li>
    <li>Shortest path algorithms</li>
    <li>Grid navigation</li>
    <li>Graph routing</li>
    <li>Dynamic replanning</li>
</ul>

<hr>

<h2>🧑‍💻 Author</h2>
<p>This project is created for learning and experimenting with pathfinding algorithms.</p>

<hr>

<h2>📜 License</h2>
<p>Free for educational use.</p>

</div>

</body>
</html>
