#include <iostream>
#include <list>
using namespace std;

class Graph{
   int V;
   list <int> *l;
public:
   Graph(int v){
      V=v;
      // Array of linked lists
      l=new list <int> [v];
   }
   void add_edges(int u ,int v,bool bidir=true){
      l[u].push_back(v);
      if (bidir)
      l[v].push_back(u);
      
   }
   void printadj(){
      for (int i=0;i<V;i++){
         //l[i] is linked list
         cout<<i<<"->";
      
      for(int vertex:l[i]){
         cout<<vertex<<",";
      }
      cout<<endl;
      }
   }
};
int main() {
	// your code goes here
	//Graph has 5 vertices  (0-5)
	Graph g(5);
	g.add_edges(0,1);
	g.add_edges(0,4);
	g.add_edges(4,3);
	g.add_edges(1,4);
	g.add_edges(1,2);
	g.add_edges(2,3);
	g.add_edges(1,3);
	g.printadj();

	return 0;
}
