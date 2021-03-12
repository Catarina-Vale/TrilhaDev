using System;
using MongoDB.Bson;
using MongoDB.Driver;

namespace MongoReposDOTNET
{
    class Program
    {
        static void Main(string[] args)
        {
            var client = new MongoClient("mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority");

            var database = client.GetDatabase("Teste");

            var collection = database.GetCollection<BsonDocument>("user");

            var document = collection.Find(new BsonDocument()).ToList();
            string output = "";
            foreach(BsonDocument entry in document){
                output += entry;
            }
            Console.Write(output);
            Console.WriteLine("Novo nome para registro: ");
            var newname = Console.ReadLine();
            Console.WriteLine("E qual repositorio este pessoa possui?: ");
            var newrepo = Console.ReadLine();
            var newguy = new BsonDocument{
                {"Usuario", newname},
                {"Repositorio", newrepo},
            };
            collection.InsertOne(newguy);

            Console.WriteLine("Inserted him nice and easy");

            Console.WriteLine("Nome para pesquisa: ");
            var lookforname = Console.ReadLine();
            var filter = Builders<BsonDocument>.Filter.Eq("Usuario", lookforname);
            
            var findthem = collection.Find(filter).FirstOrDefault();
            if(findthem == null){
                Console.WriteLine("Didnt find the guy :(");
            }
            else{
                Console.WriteLine($"Found the guy!: {findthem.ToString()}");
            }
        }
    }
}
