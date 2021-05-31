// Do not edit the class below except for
// the insert, contains, and remove methods.
// Feel free to add new properties and methods
// to the class.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
//O(n(logn)) time
  insert(value) {
		let currentNode = this;
		while(true){
			if(value < currentNode.value){
				if(currentNode.left === null){
					currentNode.left = new BST(value);
					break;
				}
				else{
					currentNode = currentNode.left;
				}
			}
			else {
				if(currentNode.right === null){
					currentNode.right = new BST(value);
					break;
				}
				else{
					currentNode = currentNode.right;
				}
			}
		}
    return this;
  }

  contains(value) {
		let currentNode = this;
		while(currentNode != null){
			if(value < currentNode.value){
				currentNode = currentNode.left;
			}
			else if (value > currentNode.value){
				currentNode = currentNode.right;
			}
			else{
				return true;
			}
		}
		return false;
    // Write your code here.
  }

  remove(value, parentNode = null) {
    let currentNode = this;
		while(currentNode !== null){
			if(value < currentNode.value){
				parentNode = currentNode;
				currentNode = currentNode.left;
			}
			else if(value > currentNode.value){
				parentNode = currentNode;
				currentNode = currentNode.right;
			}
			else{
				if(currentNode.left !== null && currentNode.right !== null){
					currentNode.value = currentNode.right.getMinValue(); 
					//current.value = smallest value of right subtree
					currentNode.right.remove(currentNode.value, currentNode)
				}
				else if(parentNode === null){//value = root
					if(currentNode.left !== null){
						currentNode.value = currentNode.left.value;
						currentNode.right = currentNode.left.right;
						currentNode.left = currentNode.left.left;
					}
					else if(currentNode.right != null){
						currentNode.value = currentNode.right.value;
						currentNode.left = currentNode.right.left;
						currentNode.right = currentNode.right.right;
					}
					else{
						//currentNode = null; //single node tree
					}
				}
				else if(parentNode.left === currentNode){
					parentNode.left = currentNode.left !== null ? currentNode.left : currentNode.right;
					
				}
				else if(parentNode.right === currentNode){
					parentNode.right = currentNode.left !== null ? currentNode.left :currentNode.right;
				}
				break;
			}
		}
		return this;
    
  }
		
  getMinValue(){
		let currentNode = this;
		while(currentNode.left !== null){
			 currentNode = currentNode.left;
		}
		return currentNode.value;
	}
}

// Do not edit the line below.
exports.BST = BST;
