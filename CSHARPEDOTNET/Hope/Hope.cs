using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using System.Data.SqlClient;
using MongoDB.Bson;
using MongoDB.Driver;
using System;
using Microsoft.Azure.WebJobs.Host;
using System.Collections.Generic;
using System.Linq;


namespace Products
{
    public static class Hope
    {
        static private MongoClient client = new MongoClient("mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority");
        static private IMongoDatabase database = client.GetDatabase("CrudProject");
        static private IMongoCollection<BsonDocument> collection = database.GetCollection<BsonDocument>("user");
        [FunctionName("Hope")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = "hope")] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("C# HTTP trigger function processed a request.");

            // string name = req.Query["name"];

            // string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            // dynamic data = JsonConvert.DeserializeObject(requestBody);
            // name = name ?? data?.name;

            string responseMessage =  "Have Hope";

            return new OkObjectResult(responseMessage);
        }
        [FunctionName("GetAllProducts")]
        public static async Task<IActionResult> GetAllProducts(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = "products")] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("User Requested all products");
            
            // var database = client.GetDatabase("CrudProject");
            // log.LogInformation(database.typeOf());
            // var collection = database.GetCollection<BsonDocument>("user");
            // log.LogInformation(collection.typeOf());
            var document = await collection.Find(new BsonDocument()).ToListAsync();
            log.LogInformation("Debug");
            return new OkObjectResult(document);
            
        }
        [FunctionName("GetProductByName")]
        public static async Task<IActionResult> GetProductByName(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = "products/{name}")] HttpRequest req,
            ILogger log, string name)
        {
            log.LogInformation($"User Requested Product named {name} ");

            // var database = client.GetDatabase("CrudProject");

            // var collection = database.GetCollection<BsonDocument>("user");

            var filter = Builders<BsonDocument>.Filter.Eq("Name", name);
            
            var findthem = collection.Find(filter).FirstOrDefault();
            if(findthem == null){
                return new NotFoundResult();
            }

            return new OkObjectResult(findthem);
            
        }
        [FunctionName("PostProduct")]
        public static async Task<IActionResult> PostProduct(
            [HttpTrigger(AuthorizationLevel.Anonymous, "post", Route = "products")] HttpRequest req,
            ILogger log)
        {

            string Name = req.Query["name"];
            string Desc = req.Query["desc"];
            string Value = req.Query["value"];

            log.LogInformation($"User tried to post product:\n Name: {Name} \n Description: {Desc} \n Price: {Value} ");

            // var database = client.GetDatabase("CrudProject");

            // var collection = database.GetCollection<BsonDocument>("user");

            var filter = Builders<BsonDocument>.Filter.Eq("Name", Name);
            
            var findthem = collection.Find(filter).FirstOrDefault();

            var newentry = new BsonDocument{
                {"Name", Name},
                {"Description", Desc},
                {"Value", Value},

                };

            if(findthem == null){

            await collection.InsertOneAsync(newentry);

            return new OkObjectResult(newentry);

            }

            return new BadRequestObjectResult(newentry);

        }
        [FunctionName("PutProduct")]
        public static async Task<IActionResult> PutProduct(
            [HttpTrigger(AuthorizationLevel.Anonymous, "put", Route = "products/{name}")] HttpRequest req,
            ILogger log, string name)
        {
            string Name = req.Query["name"];
            string Desc = req.Query["desc"];
            string Value = req.Query["value"];

            log.LogInformation($"User tried to update product:\n Name: {name} \n Description: {Desc} \n Price: {Value} ");

            // var database = client.GetDatabase("CrudProject");

            // var collection = database.GetCollection<BsonDocument>("user");

            var filter = Builders<BsonDocument>.Filter.Eq("Name", name);
            
            var findthem = collection.Find(filter).FirstOrDefault();

            var newentry = new BsonDocument{
                {"Name", Name},
                {"Description", Desc},
                {"Value", Value},

                };

            if(findthem == null){
            return new BadRequestObjectResult(newentry);
            }
            else{

            if(Desc != null){
                var updateDesc = Builders<BsonDocument>.Update.Set("Description", Desc);
                collection.UpdateOne(filter, updateDesc);
            }

            if(Value != null){
                var updateValue = Builders<BsonDocument>.Update.Set("Value", Value);
                collection.UpdateOne(filter, updateValue);
            }

            if(Name != null){
                var updateName = Builders<BsonDocument>.Update.Set("Name", Name);
                collection.UpdateOne(filter, updateName);
            }

            return new OkObjectResult(newentry);
            }

        }
        [FunctionName("DeleteProduct")]
        public static async Task<IActionResult> DeleteProduct(
            [HttpTrigger(AuthorizationLevel.Anonymous, "delete", Route = "products/{name}")] HttpRequest req,
            ILogger log, string name)
        {
            log.LogInformation($"User Wants to delete product {name} ");

            // var database = client.GetDatabase("CrudProject");

            // var collection = database.GetCollection<BsonDocument>("user");

            var filter = Builders<BsonDocument>.Filter.Eq("Name", name);
            
            var findthem = collection.Find(filter).FirstOrDefault();

            if(findthem == null){
                return new NotFoundResult();
            }

            collection.DeleteOne(filter);

            return new OkObjectResult(findthem);
            
        }
    }
}

