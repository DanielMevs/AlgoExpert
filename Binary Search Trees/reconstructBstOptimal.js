//O(n) time; O(h) space
class BST{
    constructor(value, left=null, right=null){
        this.value = value;
        this.left = left;
        this.right = right;
    }
}
class treeInfo{
    constructor(rootIdx){
        this.rootIdx = rootIdx;
    }
}

function reconstructBst(preOrderTraversalValues){
    const treeInfo = new treeInfo(0);
    return reconstructBstFromRange(-Infinity, Infinity, preOrderTraversalValues, treeInfo)

}

function reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo){
    if(currentSubtreeInfo.rootIdx == preOrderTraversalValues.length){
        return null;
    }

    const rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx];
    if(rootValue < lowerBound || rootValue >= upperBound){ //strictly less than because the right child value can be the same as the current node.
        return null;
    }

    currentSubtreeInfo.rootIdx += 1;
    const leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo);
    const rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo);

    return new BST(rootValue, leftSubtree, rightSubtree);
}
exports.BST = BST;
exports.reconstructBst = reconstructBst;