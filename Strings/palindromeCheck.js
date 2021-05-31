function isPalindrome(string) {
	let reversedString = '';
	for(let i = string.length-1; i >= 0; i--){
		reversedString += string[i];
	}
	return string === reversedString;
  // Write your code here.
}

// Do not edit the line below.
exports.isPalindrome = isPalindrome;
