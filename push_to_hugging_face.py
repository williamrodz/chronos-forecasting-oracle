from chronos import ChronosPipeline

pipeline = ChronosPipeline.from_pretrained("/home/ubuntu/chronos-forecasting-oracle/scripts/output/chronos-t5-tiny-336-48-alpha/checkpoint-final")
pipeline.model.model.push_to_hub("chronos-t5-tiny-336-48-alpha")
print("Finished pusing model to HF")