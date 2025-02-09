//function to display messages on the bottom right
export async function msg(msg) {
	if (msg === undefined)
		return;
	const error_box = document.getElementById("error-box");
	error_box.textContent = msg.toUpperCase();
	error_box.classList.toggle("error_active");
	await sleep(2000);
	error_box.classList.toggle("error_active");
}

//zzzzzzzzz
export function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

export function randomNumber(numberList) {
	const listLength = numberList.length;
	const randomIndex = Math.random();
	const randomIntegerIndex = Math.floor(randomIndex * listLength);
	return numberList[randomIntegerIndex];
}

// to avoid xss injections
export function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}

//used to display test on paddles in tourney and online modes
export function writeVerticalText(context, text, x, y, font, rotation) {
	context.save(); // Save the current state
	context.translate(x, y); // Move the origin
	if (rotation == 0)
		context.rotate(Math.PI / 2); // Rotate 90 degrees counter-clockwise
	else
		context.rotate(-Math.PI / 2); // Rotate 90 degrees counter-clockwise
	context.font = font;
	context.fillText(text, 0, 0); // Draw text horizontally at origin
	context.restore(); // Restore the original state
}

//used to keep track of the state of the tourney
export class tourneyGame {
	constructor(player, index, scores, max_points, max_phases) {
		this.player = [];
		this.index = index;
		this.score = [];
		this.max_points;
		this.max_phases;
	}
}

//to make sure the previous tournament doesn't influence the new one
export function resetTourneyGame(tourney_game) {
	tourney_game.player = [];
	tourney_game.score = [];
	tourney_game.index = "";
	tourney_game.max_points = 0;
	tourney_game.max_phases = 0;
}
