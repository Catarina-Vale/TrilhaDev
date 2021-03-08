using System;

namespace Soltos
{
    class Program
    {
        static void listminmaxdecimals(){
            Console.WriteLine("signed integral types:");
            Console.WriteLine($"byte   : {sbyte.MinValue} to {sbyte.MaxValue}");
            Console.WriteLine($"ushort : {short.MinValue} to {short.MaxValue}");
            Console.WriteLine($"uint   : {int.MinValue} to {int.MaxValue}");
            Console.WriteLine($"ulong  : {long.MinValue} to {long.MaxValue}");
        }
        static void listminmaxfloatingpoint(){
            Console.WriteLine("signed integral types:");
            Console.WriteLine($"byte   : {float.MinValue} to {float.MaxValue}");
            Console.WriteLine($"ushort : {double.MinValue} to {double.MaxValue}");
            Console.WriteLine($"uint   : {decimal.MinValue} to {decimal.MaxValue}");
        }
        static void Main(string[] args)
        {
            var name = "Bob";
            var nemails = 3;
            var temperature = 34.4m;
            Console.WriteLine($"Hello {name}! You have {nemails} new emails. The temperature outside is {temperature}.");
        }   
    }
}
