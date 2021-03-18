const { MongoClient } = require("mongodb");

const url = "mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

//const dbName = "Teste"

// const client = new MongoClient(url, {
//   useNewUrlParser: true,
//   useUnifiedTopology: true,
// });

class noSqlengine
{
  constructor(url, dbName){
    this.client = new MongoClient(url, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    this.dbName = dbName;
  }
  async find_one(name) {

    try {
      await this.client.connect();
      const database = this.client.db(this.dbName);
      const collection = database.collection('user');
      // Query for a filter
      const query = { Name: name };
      const find_him = await collection.findOne(query);
      if(!find_him){
        return `Could not find user named ${name}!`
      }
      else{
      return find_him;
      }
    } finally {
      // Ensures that the client will close when you finish/error
      await this.client.close();
    }
  }
  async find_many() {

    try {
      await this.client.connect();
      const database = this.client.db(this.dbName);
      const collection = database.collection('user');

      const find_all = await collection.find().toArray();

      await this.client.close();
      return find_all;
    } finally {
      // Ensures that the client will close when you finish/error
      await this.client.close();
    }
  }
  async insert(name, desc, price) {

    try {
      await this.client.connect();
      const database = this.client.db(this.dbName);
      const collection = database.collection('user');
      const query = {Name : name};

      const find_him = await collection.findOne(query);
      if(!find_him){

        const newguy = {Name: name, Desc: desc, Price: price};
        
        await collection.insertOne(newguy);
        
        return `${newguy.Name} was inserted`
      }
    } finally {
      // Ensures that the client will close when you finish/error
      await this.client.close();
    }
  }
  async update(name, desc, price) {

    try {
      await this.client.connect();
      const database = this.client.db(this.dbName);

      const collection = database.collection('user');
      
      const query = { Name: name };
      //upsert means it will create a new entry if none is found
      const options = { upsert: true };
      
      const updateDoc = {
      $set: {
        Desc : desc,
        Price: price,
      },
    };
    const find_him = await collection.findOne(query);
    

    await collection.updateOne(query, updateDoc, options);
    if(!find_him){
      return `Found no product with that name, creating...`
    }
    else{
      return `Found a product with that name, updating...`;
    }
    
    } finally {
      // Ensures that the client will close when you finish/error
      await this.client.close();
    }
  }
  async delete_one(name) {

    try {
      await this.client.connect();
      const database = this.client.db(this.dbName);
      const collection = database.collection('user');
      // Query for a filter
      const query = { Name: name };
      const result = await collection.deleteOne(query);
      if (result.deletedCount === 1) {
        return "Successfully deleted one document.";
      } else {
        return "No documents matched the query. Deleted 0 documents.";
      }
    } finally {
      // Ensures that the client will close when you finish/error
      await this.client.close();
    }
  }
}

// sus = new noSqlengine(url, dbName);

// sus.find_one("evil-pato").catch(console.dir).then(console.log);


module.exports = noSqlengine;