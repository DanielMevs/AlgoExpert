// This is an input class. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function findKthLargestValueInBst(tree, k) {
	let bstArr = [];
	
	bstArr = findKthLargestHelper(tree, bstArr);
  // Write your code here.
  return bstArr[bstArr.length - k ]
}

function findKthLargestHelper(tree, arr){
	if(tree === null){
		return;
	}
	findKthLargestHelper(tree.left, arr);
	arr.push(tree.value);
	findKthLargestHelper(tree.right, arr);
	
	return arr;
}

// Do not edit the lines below.
exports.BST = BST;
exports.findKthLargestValueInBst = findKthLargestValueInBst;
