//O(N) time; O(1) space
function longestPeak(array) {
	let longestPeakLength = 0;
	let currentPeakLength = 0;

	for(let i = 1; i <= array.length - 2; i++){
		if(array[i] > array[i-1] && array[i] > array[i+1]){
			
			currentPeakLength = findPeakLength(array, i);
			if(currentPeakLength > longestPeakLength){
				longestPeakLength = currentPeakLength;
			}
		}
	}
	return longestPeakLength;
  // Write your code here.
}
function findPeakLength(array, tipIdx){
	let left = tipIdx-1;
	let right = tipIdx+1;
	let runningLength = 3;
	while(array[left]>array[left-1]){
		runningLength++;
		left--;
	}
	while(array[right] > array[right+1]){
		runningLength++;
		right++;
	}
	return runningLength;
}

// Do not edit the line below.
exports.longestPeak = longestPeak;
