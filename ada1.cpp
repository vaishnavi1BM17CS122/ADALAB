#include<iostream>
#include<time.h>
using namespace std;
int floor( int x)
{
    if(x==0||x==1)
        return x;
     int start=1,end=x,ans;
    while(start<=end)
    {
       int mid=(start+end)/2;
        if(mid*mid==x)
            return x;
        if(mid*mid<x)
        {
            start=mid+1;
            ans=mid;
        }
        else
            end=mid-1;
    }
     return ans;
}
int main()
{
    int x;
    cout<<"enter the value of x"<<endl;
    cin>>x;
    clock_t start;
    clock_t last;
    start=clock();
    cout<<"square root is"<<floor(x)<<endl;
    last=clock();
    cout<<"time is"<<((double )last-start)/CLOCKS_PER_SEC;
    return 0;

}
