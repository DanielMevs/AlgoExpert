function findThreeLargestNumbers(array) {
	let threeLargest = [null, null, null];
	for(const num of array){
		updateLargest(threeLargest, num);
	}
	return threeLargest;
  // Write your code here.
}

function updateLargest(array, num){
	if(array[2] === null || array[2] < num){
		shiftAndUpdate(array, num, 2);
	}
	else if(array[1] === null || array[1] < num){
		shiftAndUpdate(array, num, 1);
	}
	else if(array[0] === null || array[0] < num){
		shiftAndUpdate(array, num, 0);
	}
}

function shiftAndUpdate(array, num, idx){
	for(let i = 0; i <= idx; i++){
		if(i === idx){
			array[i] = num;
		}
		else{
			array[i] = array[i +1];
		}
	}
}
// Do not edit the line below.
exports.findThreeLargestNumbers = findThreeLargestNumbers;
