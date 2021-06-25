//run g++ only
#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int N = 7;
    int source=0;
    int goal=6;
    int flag = 0; //handling "goal not found" case
    
    
    cout<<"enter number of nodes\n";
    cin>>N;
    //graph adj list
    vector<pair<int,int>> adj[N]; //pair(node,cost)
    int E,a,b,c;
    cout<<"enter number of edges"<<endl;
    cin>>E;
    cout<<"enter node1 node2 and cost respectively"<<endl;
    for(int i=1;i<=E;i++){
        cin>>a>>b>>c;
        adj[a].push_back({b,c});

    }
    cout<<"enter source node and goal node respectively\n";
    cin>> source>>goal;
    
    vector<int>visited(N,0); //initially not visited;
    
    priority_queue<pair<int,int>> open; //pair(cost,node) 
    vector<int>close;    
    
    //pq implementation
    
    open.push({0,source});
    visited[source]=1;
    
    while(!open.empty()){
         
         
         pair<int, int> front  = open.top();
         int a = front.first; // cost
         int b = front.second; // node
         close.push_back(b);
         open.pop();
         
         //check if the front node is goal or not
         if (b==goal) {
             printf("goal found at node : %d",b); 
             flag =1; 
             break;
         }
         //not goal 
         else{
             for (auto u: adj[b]){
                 int node = u.first;
                 int cost = u.second;
                 
                 if(visited[node]==0){
                     visited[node]=1;
                     open.push({-cost,node});
                 }
             }
         }
         
     }

    //when open list is empty but no goal state found
    if(flag ==0)
        printf("goal not found");
    
    for (auto u: close)
        cout<<endl<<u;
  
    return 0;
}
