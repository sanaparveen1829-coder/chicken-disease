from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.prepare_callbacks import PrepareCallback
from CNNClassifier.components.evaluation import Evaluation
from CNNClassifier import logger

STAGE_NAME="Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
       pass

    def main(self):
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        config=ConfigurationManager()
        val_config=config.get_validation_config()
        evaluation=Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
    
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Pipeline started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Pipeline completed <<<<<<\n\n")
    
    except Exception as e:
        logger.exception(e)
        raise e