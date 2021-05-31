function bubbleSort(array) {
	for(let i = 0; i < array.length +1; i++){
		for(let j = i; j < array.length + 1; j++){
			if(array[i] >= array[j]){
				swap(array, i , j);
			}
		}
	}
	return array;
  // Write your code here.
}

function bubbleSort2(array) {
	let isSorted = false;
	let counter = 0;
	while(!isSorted){
		isSorted = true;
		for(let i = 0; i < array.length -1 - counter; i++){
			if( array[i] > array[i+1]){
				swap(array, i, i+1);
				isSorted = false;
			}
		}
		counter++;
	}
  // Write your code here.
	return array;
}

function swap(array, i, j){
	let temp = array[j];
	array[j] = array[i];
	array[i] = temp;
}
// Do not edit the line below.
exports.bubbleSort = bubbleSort;
exports.bubbleSort2 = bubbleSort2;

