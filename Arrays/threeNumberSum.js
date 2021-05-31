function threeNumberSum(array, target) {
	let threeNumberList = [];
	array.sort((a,b)=>a-b);
  for(let i = 0; i < array.length - 2; i++){
		let left = i + 1;
		let right = array.length -1;
		while(left < right){
			if(isTriplet(array[i],array[left], array[right], target)){
				threeNumberList.push([array[i], array[left], array[right]]);
				left = left + 1;
				right = right - 1;
			}
			else if(isLessThanTarget(array[i],array[left], array[right], target)){
				left = left + 1;
			}
			else{
				right = right - 1;
			}
		}
		
	}
	return threeNumberList;
}

function isTriplet(firstNumber, secondNumber, thirdNumber, target){
	if(firstNumber + secondNumber + thirdNumber === target){
		return true;
	}
	else{
		return false;
	}
}
function isLessThanTarget(firstNumber, secondNumber, thirdNumber, target){
	let difference = (firstNumber + secondNumber + thirdNumber);
	if(difference < target){
		return true;
	}
	else{
		return false;
	}
}


// Do not edit the line below.
exports.threeNumberSum = threeNumberSum;
