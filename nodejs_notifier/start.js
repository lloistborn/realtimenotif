var http = require("http");
var server = http.createServer().listen(8002);
var cookieReader = require("cookie");
var queryString = require("querystring");
var io = require("socket.io")(3000);
var redis = require("redis");
var redisAdapter = require("socket.io-redis");

io.adapter(redisAdapter({
	host: "localhost",
	port: 6379
}));

io.listen(server);

// middleware: parse cookie header into object and assign as request.cookie
io.use(function(socket, next) {
	var request = socket.request;

	if (request.headers.cookie) {
		request.cookie = cookieReader.parse(request.headers.cookie);
		next();
	}

	next(new Error("error"));
});

io.sockets.on("connection", function(socket) {
	var id = socket.request.cookie.sessionid;
	var channelName = "notification." + id;

	console.log("subscriber:", id);
	console.log("subscribing to channel:", channelName);

	// create redis client
	client = redis.createClient();

	// subscribe to the redis events channel
	client.subscribe(channelName);

	// grab message from redis and send to client
	client.on("message", function(channel, message) {
		console.log("on message", message);
		console.log("on channel", channel);

		socket.send(message);
	});

	// unsubscribe after a disconnect event
	socket.on("disconnect", function() {
		console.log("client " + id + "disconnected");
		client.unsubscribe(channelName);
	});
});