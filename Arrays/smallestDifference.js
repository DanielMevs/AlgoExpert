function smallestDifference(arrayOne, arrayTwo) {
	arrayOne.sort((a,b) => a - b);
	arrayTwo.sort((a,b)=> a - b);
	let currentSmallestPair = [];
	let onePointer = 0;
	let twoPointer = 0;
	let smallest = Infinity; //Math.pow(10,1000);
	let current = Infinity;// Math.pow(10,1000);
	
	//currentSmallestPair.push([arrayOne[onePointer], arrayTwo[twoPointer]]);
	
	while(onePointer < arrayOne.length && twoPointer < arrayTwo.length){
		let firstNum = arrayOne[onePointer];
		let secondNum = arrayTwo[twoPointer];
		if (firstNum < secondNum){
			current = secondNum - firstNum;
			onePointer = onePointer + 1;
		}
		else if(secondNum < firstNum){
			current = firstNum - secondNum;
			twoPointer = twoPointer + 1;
		}
		else{
			return [firstNum, secondNum];
		}
		if(smallest > current){
			smallest=current;
			currentSmallestPair = [firstNum, secondNum]
		}
	
	}
	return currentSmallestPair;
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;
