function nonConstructibleChange(coins) {
	coins.sort((a,b) => a-b);
	let currentChangeCreated = 0;
	for(const coin of coins){
		if(currentChangeCreated + 1 < coin){
			return currentChangeCreated + 1; 
		}
		
		currentChangeCreated += coin; 
	}
  // Write your code here.
  return currentChangeCreated + 1; //ret
}

// Do not edit the line below.
exports.nonConstructibleChange = nonConstructibleChange;
