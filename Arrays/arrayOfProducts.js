//O(n^2) time ; O(n) space where n is the length of the input array.
function arrayOfProducts1(array) {
	let output = [];
	let maxLength = array.length;
	for(let i = 0; i < maxLength; i++){
		let currentProduct = 1;
		for(let j= i+1;j<maxLength; j++){
			currentProduct = currentProduct * array[j % maxLength];
		}
		/*for(let j = 0; j < maxLength; j++){
			if(i != j){
				currentProduct = currentProduct * array[j];
			}
			
		}*/
		output[i] = currentProduct;
		
	}
	return output;
  // Write your code here.
}

function arrayOfProducts2(array) {
	const products = new Array(array.length).fill(1);
  // Write your code here.
	let leftRunningProduct = 1;
	for(let i = 0; i< array.length;i++){
		products[i] = leftRunningProduct;
		leftRunningProduct *= array[i];
	}
	let rightRunningProduct = 1;

	for(let j = array.length -1;j>=0 ;j--){
		products[j] *= rightRunningProduct;
		rightRunningProduct *= array[j];
	}
	return products;
}


// Do not edit the line below.
exports.arrayOfProducts1 = arrayOfProducts1;
exports.arrayOfProducts2 = arrayOfProducts2;
