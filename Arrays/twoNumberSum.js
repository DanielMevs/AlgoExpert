function twoNumberSum1(array, targetSum) {
  // Write your code here.
	for (i=0; i< array.length;i++){
		var firstNum = array[i]
		for (j = 0; j < i; j++){
			var secondNum = array[j]
			if (firstNum + secondNum == targetSum){
				return [firstNum, secondNum];
			}
		}
	}
	return [];
}

function twoNumberSum2(array, targetSum) {
  // Write your code here.
	var hashTab = {};
	for(const num of array){
		const potentialMatch = targetSum-num;
		if(potentialMatch in hashTab){
			return[potentialMatch, num];
		}
		else{
			hashTab[num] = true;
		}
	}
	return [];
	
}

function twoNumberSum3(array, targetSum) {
  // Write your code here.
	array.sort((a, b) => a - b);
	let left= 0;
	let right= array.length -1; 
	while(left < right){
		const potentialMatch = array[left] + array[right];
		if(potentialMatch == targetSum){
			return [array[left], array[right]];
		}
		else if(potentialMatch < targetSum){
			left+=1;
		}
		else if(potentialMatch > targetSum){
			right-=1;
		}
	}
	return[];
}

exports.twoNumberSum1 = twoNumberSum1;
exports.twoNumberSum2 = twoNumberSum2;
exports.twoNumberSum3 = twoNumberSum3;