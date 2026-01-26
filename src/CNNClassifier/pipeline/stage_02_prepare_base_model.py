from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.prepare_base_model import PrepareBaseModel
from CNNClassifier import logger

STAGE_NAME = "Prepare Base Model Stage"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
       pass

    def main(self):
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        config= ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model() 
        prepare_base_model.update_base_model()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Pipeline started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Pipeline completed <<<<<<\n\n")
    
    except Exception as e:
        logger.exception(e)
        raise e