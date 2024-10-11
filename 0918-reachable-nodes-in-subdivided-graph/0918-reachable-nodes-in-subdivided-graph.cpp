int mp[3005][3005];
class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        int N = n;
        vector<array<int, 2>> adj[N];
        memset(mp, -1, sizeof mp);
        for(auto &e: edges){
            int u = e[0], v = e[1], w = e[2] + 1;
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
            mp[u][v] = mp[v][u] = e[2];
        }

        vector<int> dist(N, INT_MAX);
        vector<bool> visited(N);
        dist[0] = 0;
        priority_queue<array<int,2>, vector<array<int,2>>, greater<>> pq;
        pq.push({0, 0});
        while(!pq.empty()){
            auto [d, v] = pq.top(); pq.pop();
            if(visited[v]) continue;
            visited[v] = true;
            for(auto [u, w]: adj[v]){
                int new_d = d + w;
                if(new_d < dist[u]){
                    dist[u] = new_d;
                    pq.push({new_d, u});
                }
            }
        }

        int ans = 0;
        for(int i = 0; i < N; ++i){
            if(dist[i] <= maxMoves) ans++;
            for(int j = i + 1; j < N; ++j){
                if(mp[i][j] == -1) continue;
                int cnti = mp[i][j], n1 = max(0, maxMoves - dist[i]), n2 = max(0, maxMoves - dist[j]);
                int cur_ans = min(cnti, n1 + n2);
                ans += cur_ans;
            }
        }
        return ans;
    }
};