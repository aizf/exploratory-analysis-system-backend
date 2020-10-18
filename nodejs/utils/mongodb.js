const { MongoClient } = require("mongodb");

// Replace the uri string with your MongoDB deployment's connection string.
// 在docker中mongo为主机名
const uri = "mongodb://mongo:27017";

const client = new MongoClient(uri);
let database = null
let collection = null
let isConnected = false;

async function connect() {
    await client.connect();
    database = client.db("exploratory-analysis-system");
    collection = database.collection("interactive-data");
    isConnected = true;
    console.log("mongodb connected")
}
connect();

function close() {
    return client.close()
}

async function insert(docs) {
    if (!isConnected) { console.log('ERROR: not connected'); return; }
    const options = { ordered: true };
    const result = await collection.insertMany(docs, options);

    console.log(
        `${result.insertedCount} documents were inserted`,
    );
}

async function find(query) {
    if (!isConnected) { console.log('ERROR: not connected'); return; }
    const result = await collection.find(query);
    return await result
}

module.exports = { close, insert, find }