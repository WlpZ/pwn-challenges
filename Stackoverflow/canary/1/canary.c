#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
void shell()
{

	system("/bin/sh");
}
int main()
{

	char ch;
	//gets(&ch);
	
	read(0,&ch,100);
	puts(&ch);	
	read(0,&ch,100);
	//puts(&ch);
}
