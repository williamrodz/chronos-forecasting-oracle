from chronos import ChronosPipeline

pipeline = ChronosPipeline.from_pretrained("/home/ubuntu/chronos-forecasting-oracle/scripts/output/chronos-tiny-336-48-8_000-abd/checkpoint-final")
pipeline.model.model.push_to_hub("chronos-tiny-336-48-8_000-abd")
print("Finished pusing model to HF")