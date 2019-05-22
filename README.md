# bert-race
We are going to explore the multiple choice reading comprehension with bert based on RACE dataset

## Out of memory issue
1) add --fp16 in run.sh. But this requires apex from nvidia. 
2) choose small model like base. It could be running on 11GB size GPU.

## How to run bert-race
1) git clone bert-race
2) cd bert-race
3) uncompress race dataset under bert-race  
4) ./run.sh   # you could add --do_eval and other parameters.
