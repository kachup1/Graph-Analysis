# 📊 Introduction

## Graphs

This project provides an **implementation and analysis** of Erdős-Rényi random graphs using the **NetworkX** and **Matplotlib** packages in Python. The program can graph, store, and read graphs from a file. 

### Features:
- **User Input:** The user will input a set of parameters into the terminal, including values for input and output, constants, nodes, etc.
- **Shortest Path Calculation:** Computes the shortest path using **Breadth First Search (BFS)** when the user specifies a node.
- **Probability Calculation:** Calculates the probability value based on the user's given constant.

## 🛠️ Pre-Requisites

- **Operating System:** Recommended to run the program in the terminal on Windows.
- **Python:** Ensure you have the latest version of Python installed. For installation, visit: [Python Downloads](https://www.python.org/downloads/).
- **Packages:** Ensure that the **NetworkX** and **Matplotlib** packages are installed.

## 🚀 To Run the Program:

1. **Open Terminal:** On Windows, start by opening your Powershell or Command Prompt window.
2. **Navigate to Directory:** Use the `cd` command to navigate to the directory where the Python file is located.
   
   Example: `cd path/to/directory`

3. **Run the Python File:** Enter the following command in the terminal and hit enter.

   Example: `python graph.py`

4. **Execution:** `graph.py` will now execute.
5. **Command Inputs Format:**

   Example: 
   `python ./graph.py --input out_graph_file.gml --create_random_graph --nodes n --constant c --plot --BFS a --output out_graph_file.gml`

   > **Note:** Input and output names need to match.  
   > **Note:** The GML file must reside in the same location as the .py file.

6. **Example Inputs:**
   - **Generating a Random Graph:**

     Example: `python ./graph.py --create_random_graph --nodes 100 --constant 1.1 --plot --output out_graph_file.gml`

   - **Generating a BFS Graph:**

     Example: `python ./graph.py --input out_graph_file.gml --BFS 1 --plot`

   > **Note:** When the BFS graph is displayed, the nodes may appear clustered together. To view them more clearly, try zooming in.

## 📝 Author

**Karla Chuprinski**
