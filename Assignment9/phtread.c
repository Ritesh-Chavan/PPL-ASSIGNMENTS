#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<unistd.h>
#include<string.h>

typedef struct timer{
	int sec;
	int min;
	int hrs;
} timer;

void *hours(void* time){
	timer* uptime = time;
	while(1){
		sleep(3600);
		uptime->hrs = uptime->hrs + 1;
		uptime->min = 0;
	}
}

void *minutes(void* time){
	timer* uptime = time;
	while(1){
		sleep(60);
		uptime->min = uptime->min + 1;
		uptime->sec = 0;
	}
}

void *seconds(void* time){
	timer* uptime = time;
	while(1){
		sleep(1);
		uptime->sec = uptime->sec + 1;
	}
}	
		

void *Time(void* time){
	timer* uptime = time;
	char seconds[3] = "\0";
	char minutes[3] = "\0";
	char hours[3] = "\0";
	
	while(1){
		if(uptime->sec < 10)
			sprintf(seconds,"0%d", uptime->sec);
		else
			sprintf(seconds,"%d", uptime->sec);

		if(uptime->min < 10)
			sprintf(minutes,"0%d", uptime->min);
		else
			sprintf(minutes,"%d", uptime->min);
		
		if(uptime->hrs < 10)
			sprintf(hours,"0%d", uptime->hrs);
		else
			sprintf(hours,"%d", uptime->hrs);
		
		printf("\r %s:%s:%s.", hours, minutes, seconds);
	}
}



int main(){
	printf("Timer:\n");  
	pthread_t td1,td2,td3, td4;

	timer *time = malloc(sizeof(timer));
	time -> sec = 0;
	time -> min = 0;
	time -> hrs = 0;
	
	pthread_create(&td1, NULL, seconds, time);
	pthread_create(&td2, NULL, minutes, time);	
	pthread_create(&td3, NULL, hours, time);
	pthread_create(&td4, NULL, Time, time);

	int join1 = pthread_join(td1, NULL);
	int join2 = pthread_join(td2, NULL);
	int join3 = pthread_join(td3, NULL);
	int join4 = pthread_join(td3, NULL);

	return 0;

}
