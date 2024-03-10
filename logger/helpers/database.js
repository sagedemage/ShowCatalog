const mongoose = require('mongoose');

require('dotenv').config();

const username = process.env.MONGODB_USERNAME
const password = process.env.MONGODB_PASSWORD
const host = process.env.MONGODB_HOST
const db_name = process.env.MONGODB_NAME
const port = '27017'

main().catch(err => console.log(err));

async function main() {
    const config = {dbName: db_name}
    await mongoose.connect('mongodb://' + username + ':' + password + '@' + host + ':' + port + '/', config);
}

const db = mongoose.connection

db.on('error', (error) => {
    console.error(error);
})

db.once('connected', () => {
    console.log('Database Connected');
})

const logSchema = new mongoose.Schema({
    msg: String,
    date: String,
    method: String,
    show_id: Number,
})

const Log = mongoose.model('Log', logSchema)

module.exports = Log;
