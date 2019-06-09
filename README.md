# bert-race
We are going to explore the multiple choice reading comprehension with bert based on RACE dataset

## How to install boto3 
python -m pip install --user boto3

## Out of memory issue
1) Add --fp16 in run.sh. But this requires apex from nvidia. 
2) Choose small model like base. It could be running on 11GB size GPU.
3) Tune freezed layers
4) Use V100 in gcloud

## How to run bert-race
1) git clone bert-race
2) cd bert-race
3) uncompress race dataset under bert-race  
4) ./run.sh   # you could add --do_eval and other parameters.

### run base model in gcloud with K80. It took 28 hours to complete 2 epoches with 1e-5 learning rate.


