// if else

Console.Write("Введите имя пользователя: ");
string username = Console.ReadLine();

if(username.ToLower() == "даша")
{
    Console.WriteLine("Gucci flip flop, DaShA!");
} 
else
{
    Console.WriteLine("Привет, ");
    Console.WriteLine(username);
}