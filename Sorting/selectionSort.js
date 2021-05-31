//find the smallest number in the sublist of unsorted numbers 
//and append it to the end of the list of the sort numbers.
function selectionSort(array) {
	let currentIdx = 0;
	while(currentIdx < array.length -1){
		let smallestIdx = currentIdx;
		for(let i = currentIdx + 1; i < array.length;i++){
			if(array[i]< array[smallestIdx]){
				smallestIdx = i;
			}
		}
		swap(array,currentIdx, smallestIdx);
		currentIdx++;
		
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
exports.selectionSort = selectionSort;
