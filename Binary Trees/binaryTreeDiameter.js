// This is an input class. Do not edit.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
class TreeInfo{
	constructor(diameter, height){
		this.diameter = diameter;
		this.height = height;
	}
}
function binaryTreeDiameter(tree) {
	
  return getTreeInfo(tree).diameter;
}

function getTreeInfo(tree){
	if(tree === null){
		return new TreeInfo(0,0)
	}
	let leftTreeData = getTreeInfo(tree.left);
	let rightTreeData = getTreeInfo(tree.right);
	
	let longestPathThroughRoot = leftTreeData.height + rightTreeData.height;
	let maxDiameterSoFar = Math.max(leftTreeData.diameter, rightTreeData.diameter);
	let currentDiameter = Math.max(longestPathThroughRoot, maxDiameterSoFar);
	let currentHeight = 1 + Math.max(leftTreeData.height, rightTreeData.height);
	
	return new TreeInfo(currentDiameter, currentHeight);
}
// Do not edit the line below.
exports.binaryTreeDiameter = binaryTreeDiameter;
exports.BinaryTree = BinaryTree;
