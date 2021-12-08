#!/bin/bash

set -e
poetry build

INPUT_FILE_PATH="./resources/inputs/top_movie_genres.csv"
OUTPUT_PATH="./resources/outputs/save-cleaned-data-job/"
JOB="./jobs/save_cleaned_data.py"

rm -rf $OUTPUT_PATH

poetry run spark-submit \
    --master local \
    --py-files dist/transformations-*.whl \
    $JOB \
    $INPUT_FILE_PATH \
    $OUTPUT_PATH