python race.py --data_dir=RACE --bert_model=bert-large-uncased --output_dir=large_models --max_seq_length=320 --do_eval  --do_lower_case --train_batch_size=8 --eval_batch_size=32 --learning_rate=1e-5 --num_train_epochs=2 --gradient_accumulation_steps=8 --loss_scale=0


