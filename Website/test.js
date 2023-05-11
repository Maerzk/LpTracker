const { get } = require("http");
const sqlite3 = require("sqlite3").verbose();

my_ign = "Kolosalos"


let path = require('path')
const filePath = path.dirname(__filename);
let dbPath = path.join(filePath, "../Database/" + my_ign + "Data.db");

// open the database
let db = new sqlite3.Database(dbPath);

getRow("matchid");

function getRow(rowName)
{
    let Array = [];
    let sql = "SELECT " + rowName + " FROM solodata";

    db.all(sql, [], (err, rows) => 
    {
        if (err) 
        {
            throw err;
        }
        rows.forEach((row) => 
        {
            //console.log(row.points);
            Array.push(row[rowName]);
        });
    print(Array)
    db.close();    
    });
}

function print(Array)
{
    console.log(Array);
}