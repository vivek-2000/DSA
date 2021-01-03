#include <iostream>
#include <list>
#include <map>
#include <queue>
using namespace std;

template <typename T>
class Graph{
   map<T,list<T> >adjlist;
public:
   void add_edges(int u ,int v,bool bidir=true){
      adjlist[u].push_back(v);
      if (bidir)
      adjlist[v].push_back(u);
      
   }
   void printadj(){
      // iteratoe over map
      for (auto i:adjlist){
         //adjlist[i] is linked list
         cout<<i.first<<"->";
         for (auto entry :i.second){
         cout<<entry<<",";
 
      }
      cout<<endl;
      }
   }
   void dfs_helpher(T node ,map<T,bool>&visited){
      //whenever to come to node ,mark it visited
      visited[node]=true;
      cout<<node<<" ";
      for (T neighbour:adjlist[node]){
         if(!visited[neighbour]){
            dfs_helpher(neighbour,visited);
         }
      }
   }
   void dfs(T src){
      map <T,bool> visited;
      dfs_helpher(src,visited);
   }
   void bfs(T src){
      queue<T> q;
      map <T,bool> visited;
      q.push(src);
      visited[src]=true;
      while(!q.empty()){
         T node =q.front();
         cout<<node<<" ";
         q.pop();
         for(auto neighbour :adjlist[node]){
            if (!visited[neighbour]){
               q.push(neighbour);
               visited[neighbour]=true;
            }
         }
      }
   }
};
int main() {
	// your code goes here
	//Graph has 5 vertices  (0-5)
	Graph <int> g;
    g.add_edges(0,1);
    g.add_edges(1,2);
    g.add_edges(0,4);
    g.add_edges(2,4);
    g.add_edges(2,3);
    g.add_edges(3,4);
    g.add_edges(3,5);
	//g.printadj();
	//g.bfs(0);
	g.dfs(0);
	return 0;
}
