#include <bits/stdc++.h>
#define ll long long int
using namespace std;


void program()
{
    ll n, k_cost;
    cin >> n >> k_cost;
    ll fam[n + 1];

    for (int i = 0; i < n; i++)
        cin >> fam[i];

    ll col[n][n] = {0}; // n+1 -> n both

    // for (ll i = 0; i < n; i++)
    // {
    //     for (ll j = 0; j < n; j++)
    //         col[i][j] = 0;
    // }

    for (int i = 0; i < n; i++)
    {
        int family_cnt[n + 1];
        for (int p = 0; p < n + 1; p++)
            family_cnt[p] = 0;

        for (ll j = i; j < n; j++)
        {
            if (j == 0)
                col[i][j] = 0;
            else
                col[i][j] = col[i][j - 1];

            if (family_cnt[fam[j]] != 0)
            {
                if (family_cnt[fam[j]] == 1)
                    col[i][j]++;
                col[i][j]++;
            }
            family_cnt[fam[j]]++;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << col[i][j] << " ";
        cout << endl;
    }
    
    ll dmat[101][1001] = {0};
    // for (int i = 0; i <= 100; i++)
    // {
    //     for (int j = 0; j <= 100; j++)
    //     {
    //         dmat[i][j] = 0;
    //     }
    // }
    for (int i = 2; i < n + 1; i++) // initial i = 0 to i = 2
        dmat[1][i] = col[0][i - 1];

    for (int i = 2; i <= 100; i++)
    {
        for (int j = 2; j <= n; j++)
        {
            ll opti = INT64_MAX;
            for (int p = 1; p < j; p++)
            {
                opti = min(opti, dmat[i - 1][p] + col[p][j - 1]);
            }
            dmat[i][j] = opti;
        }
    }

    ll check = INT64_MAX;
    for (ll i = 1; i <= 100; i++)
    {
        check = min(i * k_cost + dmat[i][n], check);
    }
    cout << check << "\n";
}

int main()
{
    ll n_test;
    std::cin >> n_test;
    for (int i = 0; i < n_test; i++)
        program();
}
