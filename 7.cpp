#include <stdio.h>

int main()
{
	int a,b,max = 0,i,thamchieu;
	printf("Nhap a va b: ");
	scanf("%d%d",&a,&b);
	for (i=1; (i<=a && i<=b) ; i++)		
	{
		if (a % i == 0 && b % i ==0)
			thamchieu = i;
			if (max <= thamchieu)
				max = thamchieu;
	}
	printf("UCLN cua %d va %d la %d",a,b,max);
}
