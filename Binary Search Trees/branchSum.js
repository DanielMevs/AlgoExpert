// This is the class of the input root.
// Do not edit it.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
function branchSums(root) {
	let sums = [];
	branchSumsHelper(root, 0, sums);
	return sums;

}
function branchSumsHelper(root,currentSum,sum) {
	if(!root){
		return;
	}
	let currentNode = root;
	const running_sum = currentSum + currentNode.value;
	if(!currentNode.left && !currentNode.right){
		sum.push(running_sum);
		return;
	}
	branchSumsHelper(currentNode.left,running_sum, sum);
	branchSumsHelper(currentNode.right,running_sum, sum);

}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.branchSums = branchSums;
