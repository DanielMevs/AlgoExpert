function findClosestValueInBst1(tree, target) {
  // Write your code here.
	return findClosestHelper(tree, target, tree.value);
}
function findClosestHelper1(tree, target, closest){
	if(tree=== null){
		return closest;
	}
	if(Math.abs(target-tree.value) < Math.abs(target-closest)){
		closest = tree.value;
	}
	if(tree.value > target){
		return findClosestHelper(tree.left, target, closest);
	}
	else if(tree.value < target){
		return findClosestHelper(tree.right, target, closest);
	}
	else{
		return closest;
	}
}

function findClosestValueInBst2(tree, target) {
  // Write your code here.
	return findClosestHelper(tree, target, tree.value);
}
function findClosestHelper2(tree, target, closest){
	let currentNode = tree;
	while(currentNode !== null){
		if(Math.abs(target-closest) > Math.abs(target-currentNode.value)){
			closest = currentNode.value;
		}
		if(currentNode.value > target){
			currentNode = currentNode.left;
		}
		else if(currentNode.value < target){
			currentNode = currentNode.right;
		}
		else{
			break;
		}
	}
	return closest;
	
}

// This is the class of the input tree. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.findClosestValueInBst1 = findClosestValueInBst1;
exports.findClosestValueInBst2 = findClosestValueInBst2;
