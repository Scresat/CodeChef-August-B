#include <bits/stdc++.h>
#define ll long long int
using namespace std;

void program()
{
    ll n, k_cost;
    cin >> n >> k_cost;
    ll fam[n];

    for (int i = 0; i < n; i++)
        cin >> fam[i];

    ll counter[n][n] = {0};
    for (int i = 0; i < n; i++)
    {
        map<ll, ll>dict;
        for (ll j = i; j < n; j++)
        {
            if (j) counter[i][j] = counter[i][j-1];
            else counter[i][j] = 0;
            if (dict.count(fam[j]))
            {
                if (dict[fam[j]] == 1)
                    counter[i][j]++;
                counter[i][j]++;
            }
            dict[fam[j]]++;
        }
    }

    ll dmat[101][1001] = {0};
    for (int i = 0; i < n + 1; i++)
        dmat[1][i] = counter[0][i - 1];

    for (int i = 2; i <= 100; i++)
    {
        for (int j = 2; j <= n; j++)
        {
            ll opti = INT64_MAX;
            for (int p = 1; p < j; p++)
                opti = min(opti, dmat[i - 1][p] + counter[p][j - 1]);

            dmat[i][j] = opti;
        }
    }

    ll check = INT64_MAX;
    for (ll i = 1; i <= 100; i++)
    {
        ll p = i * k_cost + dmat[i][n];
        if (p < check) check = p;
    }
    cout << check << endl;
}

int main()
{
    ll n_test;
    std::cin >> n_test;
    for (int i = 0; i < n_test; i++)
        program();
}
