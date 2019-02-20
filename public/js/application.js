

window.g_game = null;

// Wait till the browser is ready to render the game (avoids glitches)
window.requestAnimationFrame(function () {
    Math.seedrandom(456);

    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
	console.log('co');
	socket.emit('g2048', {data: 'I\'m connected!'});
    });

    socket.on('g2048', function(msg) {
	console.log('got message:', msg);
    });
    
    
    window.g_game = new GameManager(4, KeyboardInputManager, HTMLActuator, LocalStorageManager);
});
