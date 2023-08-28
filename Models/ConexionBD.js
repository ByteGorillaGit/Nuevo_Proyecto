const mysql = require('mysql')
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'post_sale'
})

connection.connect((err) => {
    if (err) throw err
    console.log('Conexion establecida correctamente')
})

connection.end()
