#!/usr/bin/node
// this script computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

if (!url) {
	console.log('Usage ./6-complted_tasks.js <API URL>');
	process.exit(1);
}

request.get(url, (error, response, body) => {
	if (error) {
		console.error(`Error: ${error.message}`);
		return;
	}

	if (response.statusCode === 200) {
		const todos = JSON.parse(body);
		const userTaskCount = {};

		todo.forEach(todo => {
			if (userTaskCount[todo.userId]) {
				userTaskCoujt[todo.userId]++;
			} else {
				userTaskCount[todo.userId] = 1;
			}
		}
	});

		console.log(userTaskCount);
	} else {
		console.log(`Error: ${response.StatusCode}`);
	}
});
	
