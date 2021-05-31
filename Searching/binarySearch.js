function binarySearch1(array, target) {
	return binarySearchHelper(array, target, 0, array.length-1);
  // Write your code here.
}

function binarySearchHelper1(array, target, left, right){
	if(left > right){
		return -1; //target not found.
	}
	let middle = Math.floor((left + right) / 2);
	let potentialMatch = array[middle];
	if(potentialMatch === target){
		return middle;
	}
	else if(target < potentialMatch){
		return binarySearchHelper(array, target, left, middle -1 );
	}
	else{
		return binarySearchHelper(array, target, middle + 1, right);
	}
	
}

function binarySearch2(array, target) {
  return binarySearchHelper(array, target, 0, array.length -1);
}
function binarySearchHelper2(array, target, left, right){
	while(left <= right){ //done iteratively
	
		let middle = Math.floor((left + right) / 2);
		let potentialMatch = array[middle];
		if(potentialMatch === target){
			return middle;
		}
		else if(target < potentialMatch){
			return binarySearchHelper(array, target, left, middle -1 );
		}
		else{
			return binarySearchHelper(array, target, middle + 1, right);
		}

	}
	return -1;
}

// Do not edit the line below.
exports.binarySearch1 = binarySearch1;
exports.binarySearch2 = binarySearch2;
