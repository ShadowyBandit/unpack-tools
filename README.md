# unpack-tools
Scripts to fix WoWS ContentSDK unpack files
CONTENTS: 
	gatherMP.py
		INFO: This compiles a list of all the active MP tags in the patch into notObsolete.txt. 
			  You only need to run this once per patch.
		SETUP: In order to run this, you need to unpack the entire /gameplay/ folder from the WoWS Unpack tool.
			   Place gatherMP.py and notObsolete.txt in /content/gameplay/ and run this script.
	removeMP.py
		INFO: This deletes all obsolete MP nodes from .visual files in conjunction with notObsolete.txt.
		SETUP: Just place in the second layer of the mod folder e.g. /myMod/USD507_Haida/, or in other words, 
			   place it next to the compile.info alongside notObsolete.txt.
			   ---This directory will be refered to as the "lobby"---
			   
	moveLods.py
		INFO: This moves all lods and updates paths in .model files
		SETUP: Just place in the lobby
			   			   
	fixMFM(SEA).py
		INFO: This updates fx node and /common/ maps
		SETUP: Just place in the lobby
			   
	notObsolete.txt
		INFO: This stores active MP tags
		SETUP: First place in /content/gameplay/ to compile MP.
			   Afterword, place in the lobby
ORDER:
	1. If you haven't compiled all the MP files, do it: 
		move gatherMP.py and notObsolete.txt to /content/gameplay/ and run gatherMP.py. Then move notObsolete.txt to the lobby
	2. Run removeMP.py
	3. Run fixFMF(SEA).py
	4. Run moveLods.py
	(technically 2,3, and 4 can be interchanged)
CREDITS:
	AstreTunes and SEA group for guidance and script skeleton
	ShadowyBandit
