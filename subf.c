#include <stdio.h>
#include <math.h>
#define long log ll

int main()
{
    ll n, i, j, k;
    scanf("%lld", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%lld", &j);
    }
    for (k = n-1; k > 0; k++)
    {
        printf("%lld ", pow(2, k));
    }
    printf("1");
}