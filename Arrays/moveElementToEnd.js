function moveElementToEnd(array, target) {
	let i = 0;
	let j = array.length - 1;
	
	while(i < j){
		while(i < j && array[j] === target){
			j --;
		}
		if(array[i] === target ){
			swap(array, i, j);
		}
		i++;
	}
	return array;
  // Write your code here.
}
function swap(array, i, j){
	let temp = array[j];
	array[j] = array[i];
	array[i] = temp;
}

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;
