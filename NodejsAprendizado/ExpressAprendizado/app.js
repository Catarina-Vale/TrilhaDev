const express = require('express');
const mongo = require('./mongo.js');
url = "mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
dbName = "CrudProject";



const server = express();

port = 5000;
server.get('/', (req, res) => {
    res.send("Hello world");
});
//explanation on how it all works on the post method, since its all very similar
server.get('/api/products', (req, res) => {
    const client = new mongo(url,dbName);
    client.find_many().catch(console.dir).then((value) => res.send(value));
});

server.get('/api/products/:name', (req, res) => {
    const client = new mongo(url,dbName);
    let name = req.params.name;
    console.log(`User wants product:\n name: ${name}`);
    client.find_one(name).catch(console.dir).then((value) => res.send(value));
});

server.post('/api/products', (req, res) => {
    //establish a connection by declaring a new mongo object
    const client = new mongo(url,dbName);
    //gather the request variables
    let name = req.query.name;
    let desc = req.query.desc;
    let price = req.query.price;
    //log on console just to be sure
    console.log(`User wants to register product:\n name: ${name}\n desc: ${desc}\n price:${price}`);
    //here we call the async function from the mongo class, catch on the console for any errors, 
    //setting a then function for after the promises have been fulfilled to send to the user
    client.insert(name,desc,price).catch(console.dir).then((value) => res.send(value));
});

server.put('/api/products/:name', (req, res) => {
    const client = new mongo(url,dbName);
    let name = req.params.name;
    let desc = req.query.desc;
    let price = req.query.price;
    console.log(`User wants to update product:\n name: ${name}\n desc: ${desc}\n price:${price}`);
    client.update(name,desc,price).catch(console.dir).then((value) => res.send(value));
});

server.delete('/api/products/:name', (req, res) => {
    const client = new mongo(url,dbName);
    let name = req.params.name;
    console.log(`User wants to delete product:\n name: ${name}`);
    client.delete_one(name).catch(console.dir).then((value) => res.send(value));
});

server.listen(port, () => {
    console.log(`Currently listening on port ${port}`);
});
