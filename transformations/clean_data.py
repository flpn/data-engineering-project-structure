from typing import List


def upper_case_names(names: List) -> List:
    return list(map(str.upper, names))


def remove_whitespaces_from_names(names: List) -> List:
    return [name.strip().replace(' ', '_') for name in names]


def clean_names(names):
    return remove_whitespaces_from_names(upper_case_names(names))


def run(spark, dataset_input_path, dataset_output_path):
    input_dataframe = spark.read.csv(dataset_input_path, header=True)
    
    cleaned_columns = clean_names(input_dataframe.columns)
    output_dataframe = input_dataframe.toDF(*cleaned_columns)

    output_dataframe.show()

    output_dataframe.write.parquet(dataset_output_path)