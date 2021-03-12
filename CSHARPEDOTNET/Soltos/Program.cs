using System;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;


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
        static void konichiwaworld(){
            Console.WriteLine("\u3053\u3093\u306B\u3061\u306F World!");
        }
        static void interpolation(){
            var name = "Bob";
            var nemails = 3;
            var temperature = 34.4m;
            Console.WriteLine($"Hello {name}! You have {nemails} new emails. The temperature outside is {temperature}.");
        }
        static int addition(int firstnumber,int secondnumber){
            return firstnumber + secondnumber;
        }
        static int subtraction(int firstnumber,int secondnumber){
            return firstnumber - secondnumber;
        }
        static int multiplication(int firstnumber,int secondnumber){
            return firstnumber * secondnumber;
        }
        static float division(float firstnumber,float secondnumber){
            return firstnumber / secondnumber;
        }
        static float fahrenheitToCelsius(float input){
            float celsius = (input - 32) * 5/9;
            return celsius;
        }
        static void DesafioIfElse(){
            Random random = new Random();
            int daysUntilExpiration = random.Next(0,12);
            int discountPercentage = 0;
            if (daysUntilExpiration > 10){
                return;
            }
            else if(daysUntilExpiration > 5){
                Console.WriteLine("Your subscription will expire soon.  Renew now!");
            }
            else if(daysUntilExpiration > 1){
                discountPercentage = 10;
                Console.WriteLine($"Your subscription expires in {daysUntilExpiration} days!\nRenew now and save {discountPercentage}%!");
            }
            else if(daysUntilExpiration == 1){
                discountPercentage = 20;
                Console.WriteLine($"Your subscription expires within a day!\nRenew now and save {discountPercentage}%!");
            }
            else{
                Console.WriteLine("Your subscription has expired.");
            }
        }
        static void treinoMatrizes(){
            string[] jooj = {"jeej", "jiij", "juuj"};
            foreach (string item in jooj)
            {
                Console.WriteLine(item);
            }
        }
        static void trainuserinput(){
            Console.Write("Please input a word - ");
            var word = Console.ReadLine();
            Console.WriteLine($"You Wrote: {word}");
        }
        static HttpClient client = new HttpClient();
        static async Task Main(){
            
            HttpResponseMessage response = await client.GetAsync("https://www.dnd5eapi.co/api/spells/acid-arrow/");
            string ResponseBody = await response.Content.ReadAsStringAsync();
            Console.Write(ResponseBody);
        }
        // static void Main(string[] args)
        // {
        //     responsefromgit();
        // }   
    }
}
//https://api.github.com/users/{user}/repos