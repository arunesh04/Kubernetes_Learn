const mongoose = require('mongoose')

module.exports.connectdb = ()=>{
    return mongoose.connect("mongodb://127.0.0.1:50991/numberplate")
}