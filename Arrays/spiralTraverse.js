function spiralTraverse(array) {
  // Write your code here.
	const result = [];
	spiralFill(array, 0, 0, array.length-1, array[0].length -1, result);
	return result;
	
}
function spiralFill(array, startRow, startCol, endRow, endCol,  result){
	if(startRow > endRow || startCol > endCol){
		return;
	}
	for(let col = startCol; col <= endCol ; col++){
		result.push(array[startRow][col]);
	}
	for(let row = startRow + 1; row <= endRow; row++){
		result.push(array[row][endCol]);
	}
	for(let col = endCol -1; col >= startCol; col--){
		if(startRow === endRow) break;
		result.push(array[endRow][col]);
	
	}
	for(let row = endRow-1; row >= startRow + 1; row--){
		if(startCol === endCol) break;
		result.push(array[row][startCol]);
	}
	
	spiralFill(array, startRow+1, startCol+1,endRow-1,endCol-1,result);
	
}

// Do not edit the line below.
exports.spiralTraverse = spiralTraverse;
