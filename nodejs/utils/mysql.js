const { Sequelize, DataTypes } = require('sequelize');

const db = new Sequelize({
    dialect: "mysql",
    host: "mysql",
    // port:"3306",
    username: "root",
    password: process.env.MysqlRootPw || '',
    database: "exploratory-analysis-system",
    pool: {
        min: 0
    },
    define: {
        freezeTableName: true
    },
    timezone: '+08:00'
})

const User = db.define('user', {
    account: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true
    },
    password: {
        type: DataTypes.CHAR(32),
        allowNull: false
    },
    salt: {
        type: DataTypes.STRING,
        allowNull: true
    },
    session: {
        type: DataTypes.STRING,
        allowNull: true
    }
});

async function dbInit() {
    await User.sync({ force: true });
    console.log("User init done");
}

async function dbSync() {
    await User.sync({ alter: true });
    console.log("User sync done");
}

async function testConnection() {
    try {
        await db.authenticate();
        console.log('Connection has been established successfully.');
    } catch (error) {
        console.error('Unable to connect to the database:', error);
    }
}


exports.db = db;
exports.User = User;
exports.dbInit = dbInit;
exports.dbSync = dbSync;
exports.testConnection = testConnection;
