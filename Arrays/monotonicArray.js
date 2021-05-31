function isMonotonic1(array) {
  // Write your code here.
	let isIncreasing = true;
	let isDecreasing = true;
	
	for(let i = 1; i < array.length; i++){
		if(array[i] < array[i-1]){
			isIncreasing = false;
		}
		if(array[i] > array[i-1]){
			isDecreasing = false;
		}
	}
	
	return isDecreasing || isIncreasing;
}

function isMonotonic2(array) {
	let direction = array[1] - array[0];
	
	for(let i = 2; i < array.length; i++){
		if(direction === 0){
			direction = array[i] - array[i-1];
			continue;
		}
		if(wrongDirection(array[i], array[i-1], direction)){
			return false;
		}
	}
	return true;
  // Write your code here.
}

function wrongDirection(numOne, numTwo, direction){
	let difference = numOne - numTwo;
	if(direction > 0){
		return difference < 0;
	}
	return difference > 0;
	
}
// Do not edit the line below.
exports.isMonotonic1 = isMonotonic1;
exports.isMonotonic2 = isMonotonic2;

