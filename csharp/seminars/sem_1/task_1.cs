//Написать программу, которая на вход принимает 2 числа и проверяет, является ли второе число квадратом первого.
//a = 5, b = 25 -> yes
//a = 2, b = 10 -> no
//a = 9, b = -3 -> no
//a = -3, b = 9 -> yes

Console.WriteLine("Введите число a:");
int numA = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число b:");
int numB = Convert.ToInt32(Console.ReadLine());

if(numA * numA == numB)
{
    Console.WriteLine("yes");
}

else
{
    Console.WriteLine("no");
}
