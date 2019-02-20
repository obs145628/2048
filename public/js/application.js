

window.g_game = null;

// Wait till the browser is ready to render the game (avoids glitches)
window.requestAnimationFrame(function () {
    Math.seedrandom(456);
    window.g_game = new GameManager(4, KeyboardInputManager, HTMLActuator, LocalStorageManager);
});
