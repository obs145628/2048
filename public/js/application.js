

// Wait till the browser is ready to render the game (avoids glitches)
window.requestAnimationFrame(function () {
    var game = new GameManager(4, KeyboardInputManager, HTMLActuator, LocalStorageManager);

    
    var sock = io.connect('http://' + document.domain + ':' + location.port);
    sock.on('req', function(data) {
	idx = data[0];
	req = data[1];

	if (req[0] == 'R')
	{
	    game.restart();
	    sock.emit('req', [idx, game.getState()]);
	}

	else if (req[0] == 'SEED')
	{
	    Math.seedrandom(req[1]);
	    sock.emit('req', [idx, null]);
	}

	else if(req[0] == 'S')
	{
	    var dirs = [0, 1, 2, 3];
	    var old_score = game.score;
	    game.move(dirs[req[1]]);
	    var state = game.getState();
	    var reward = game.score - old_score;
	    var done = !game.movesAvailable();
	    sock.emit('req', [idx, [state, reward, done]])
	}

	else
	{
	    console.error('Invalid request:', req);
	    sock.emit('req', [idx, null]);
	}
	
    });
});
