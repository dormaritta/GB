// В этой программе выясняется, сколько раз пробежит собака между друзьями, пока они идут навстречу друг к другу

int count = 0;
int distance = 10000;
int meetingDistance = 10;
int firstFriendSpeed = 1;
int secondFriendSpeed = 2;
int dogSpeed = 5;
int friend = 2;
int time = 0;

while(distance > meetingDistance)
{
    if(friend == 1)
    {
       time = distance / (firstFriendSpeed + dogSpeed);
       friend = 2; 
    }

    else
    {
        time = distance / (secondFriendSpeed + dogSpeed);
        friend = 1;
    }

    distance = distance - (firstFriendSpeed + secondFriendSpeed) * time;
    count = count + 1;
}

Console.WriteLine(count);