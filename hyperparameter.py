class Hyperparameter:
	# save index 0 for unk and 1 for pad
	PAD_IDX = 0
	BOS_IDX = 1
	EOS_IDX = 2
	UNK_IDX = 3
	prepath_data = './project/'
	# prepath_data = './gdrive/My Drive/project/'
	dummy2int = {'contradiction': 0, 'entailment': 1, 'neutral': 2}
	glove_emb_dim = 200
	words_to_load = 400000
	BATCH_SIZE = 32
	MAX_SENTENCE_LENGTH = 800
	
