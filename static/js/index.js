
var Express= require('Express');
var socket = require('socket.io') ;

var appname = Express();
var server=appname.listen(5000,function(){
console.log('your server at http:/localhost:5000')

});
