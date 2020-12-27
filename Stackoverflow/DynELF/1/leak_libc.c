#include<unistd.h>

void vlun()
{
	char buf[128];
	read(0,buf,256);
	
}

char str[]="bye\n";
int main()
{
	vlun();
	write(1,str,sizeof(str)-1);
	
	
}
