const mongoose = require('mongoose')

module.exports.connectdb = ()=>{
    return mongoose.connect("mongodb://10.98.153.247:3000/numberplate")
}