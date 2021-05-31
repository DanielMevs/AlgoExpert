
//O(n^2) time; O(h) space : h = height
class BST{
    constructor(value, left = null, right = null){
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

function reconstructBst(preOrderTraversalValues){
    if(preOrderTraversalValues.length == 0){
        return null;
    }
    const currentValue = preOrderTraversalValues[0];
    let rightSubtreeRootIdx = preOrderTraversalValues.length;

    for(let i = 1; i < preOrderTraversalValues.length; i++){ 
        if(preOrderTraversalValues[i] >= currentValue){
            rightSubtreeRootIdx = i;
            break;
        }
    }

    const leftSubtree = reconstructBst(preOrderTraversalValues.slice(1, rightSubtreeRootIdx));
    const rightSubtree = reconstructBst(preOrderTraversalValues.slice(rightSubtreeRootIdx));

    return BST(currentValue, leftSubtree, rightSubtree);
}

exports.BST = BST;
exports.reconstructBst = reconstructBst;