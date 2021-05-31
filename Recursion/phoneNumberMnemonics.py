# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:00:24 2021

@author: daniel
"""
#O((4^n) * n) time and space complexity
def phoneNumberMnemonics(phoneNumber):
	currentMnemonic = ['0'] * len(phoneNumber)
	mnemonicsFound = []
	phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonicsFound)
	return mnemonicsFound
def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonic, mnemonicsFound):
	if idx == len(phoneNumber):
		mnemonic = ''.join(currentMnemonic) #takes O(n) time
		mnemonicsFound.append(mnemonic)
	else:
		digit = phoneNumber[idx]
		letters = DIGIT_LETTERS[digit]
		for letter in letters: 
			currentMnemonic[idx] = letter
			phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonic, mnemonicsFound)
DIGIT_LETTERS = {
		"0": ["0"],
		"1": ["1"],
		"2" : ["a", "b", "c"],
		"3" : ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"],
	}
