function minimumWaitingTime(queries) {
	queries.sort((a,b)=>a-b);
	let minTime = 0;
	for(let idx = 0; idx<queries.length; idx++){
		const duration = queries[idx];
		const queriesLeft = queries.length - (idx + 1);
		minTime+= queriesLeft * duration;
	}
	return minTime;
}

// Do not edit the line below.
exports.minimumWaitingTime = minimumWaitingTime;