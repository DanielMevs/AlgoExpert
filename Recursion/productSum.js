// Tip: You can use the Array.isArray function to check whether an item
// is a list or an integer.
function productSum(array, level = 1) {
	let currentSum = 0;
  for (const value of array){
		if(Array.isArray(value)){
			currentSum += productSum(value, level+1);
		}
		else{
			currentSum += value;
		}
	}
	return level * currentSum;
}

// Do not edit the line below.
exports.productSum = productSum;
