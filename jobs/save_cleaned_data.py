import sys

from pyspark.sql import SparkSession

from transformations import clean_data


if __name__ == '__main__':
    arguments = sys.argv

    dataset_input_path = arguments[1]
    dataset_output_path = arguments[2]

    spark = SparkSession.builder.appName('Data Cleaner').getOrCreate()
    
    clean_data.run(spark, dataset_input_path, dataset_output_path)

    spark.stop()