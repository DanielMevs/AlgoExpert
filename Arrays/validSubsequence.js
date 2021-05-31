function isValidSubsequence1(array, sequence) {
  // Write your code here.
	let seqInx = 0;
	for(const val of array){
		if(seqInx == sequence.length){
			break;
		}
		if(sequence[seqInx] == val){
			seqInx++;
		}
		
	}
	return seqInx == sequence.length;
}

function isValidSubsequence2(array, sequence) {
  // Write your code here.
	let seqInx = 0;
	let arrInx = 0;
	while(arrInx < array.length && seqInx < sequence.length){
		if(array[arrInx] == sequence[seqInx]){
			seqInx++;
		}
		arrInx++;
	}
	return seqInx == sequence.length;
}

exports.isValidSubsequence1 = isValidSubsequence1;
exports.isValidSubsequence2 = isValidSubsequence2;