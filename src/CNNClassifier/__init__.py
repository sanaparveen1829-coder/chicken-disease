import os
import sys
import logging


logging_str='[%(asctime)s - %(name)s - %(levelname)s - %(message)s]'

logging_dir='logs'
log_filepath=os.path.join(logging_dir,'running_logs.log')
os.makedirs(logging_dir, exist_ok=True)


logging.basicConfig(level=logging.INFO,
                    format=logging_str,
                    handlers=[logging.FileHandler(log_filepath),
                              logging.StreamHandler(sys.stdout)]
                    )


logger=logging.getLogger('CNNClassifier')