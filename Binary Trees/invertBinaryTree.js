//O(N) time
function invertBinaryTree1(tree) {
  // Write your code here.
	let queue = [tree];
	while(queue.length){ //so long as the queue is non-empy; while its not equal to 0
		let current = queue.shift();
		if(current === null){
			continue;
		}
		swapLeftAndRight(current);
		queue.push(current.left);
		queue.push(current.right);
	}
}

//recursive solution
function invertBinaryTree2(tree) {
  // Write your code here.
	if(tree === null){
		return;
	}
	swapLeftAndRight(tree);
	invertBinaryTree(tree.left);
	invertBinaryTree(tree.right);
	
}

function swapLeftAndRight(tree){
	let temp = tree.left;
	tree.left = tree.right;
	tree.right = temp;
}

// This is the class of the input binary tree.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}



// Do not edit the line below.
exports.invertBinaryTree1 = invertBinaryTree1;
exports.invertBinaryTree2 = invertBinaryTree2;

