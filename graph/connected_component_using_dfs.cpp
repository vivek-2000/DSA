#include <iostream>
#include <list>
#include <map>
#include <queue>
using namespace std;

template <typename T>
class Graph{
   map<T,list<T> >adjlist;
public:
   void add_edges(T u ,T v,bool bidir=true){
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
   //dfs
   void dfs(T src){
      map <T,bool> visited;
      int component=1;
      dfs_helpher(src,visited);
      cout<<endl;
      for (auto i:adjlist){
         T city=i.first;
         if (!visited[city]){
            dfs_helpher(city,visited);
            component++;
         }
      }
   }
   //bfs
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
	Graph <string> g;
   g.add_edges("Amritsar","Jaipur");
   g.add_edges("Amritsar","Delhi");
   g.add_edges("Delhi","Jaipur");
   g.add_edges("Mumbai","Jaipur");
   g.add_edges("Mumbai","Bhopal");
   g.add_edges("Delhi","Bhopal");
   g.add_edges("Mumbai","Banglore");
   g.add_edges("Agra","Delhi");
   g.add_edges("Andaman","Nicobar");

	//g.printadj();
	//g.bfs(0);
	g.dfs("Amritsar");
	return 0;
}
