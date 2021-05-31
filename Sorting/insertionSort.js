function insertionSort(array) {
	for(let i = 0; i < array.length; i++){
		for(let j = i; j > 0 && array[j] < array[j-1]; j--){
			swap(array, j, j-1);
		}
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
exports.insertionSort = insertionSort;
