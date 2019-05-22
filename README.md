# bert-race
We are going to explore the multiple choice reading comprehension with bert based on RACE dataset

## Out of memory issue
1) add --fp16 in run.sh. But this requires apex from nvidia. 
2) choose small model like base. It could be running on 11GB size GPU.

## How to run bert-race
cd bert-race
./run.sh
