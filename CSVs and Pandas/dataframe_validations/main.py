import pandas
import pandera

from altered_schema import schema
from pandera.typing import Series
from datetime import date


class OutputSchema(pandera.SchemaModel):
    """Schema model for US tornado."""
    yr: Series[int]
    mo: Series[int]
    dy: Series[int]
    date: Series[str]
    st: Series[str] = pandera.Field(nullable=True)
    mag: Series[int] = pandera.Field(ge=0)
    inj: Series[int] = pandera.Field(ge=0)
    fat: Series[int] = pandera.Field(ge=0)
    slat: Series[float]
    slon: Series[float]
    elat: Series[float]
    elon: Series[float]
    len: Series[float]
    wid: Series[int]


# generate pandas dataset schema
def main():
    data = pandas.read_csv("us_tornado_dataset_1950_2021.csv")
    print(data.head())

    data_inferred_schema = pandera.infer_schema(data)
    with open("inferred_schema.py", "w") as file:
        file.write(data_inferred_schema.to_script())

    try:
        schema.validate(data, lazy=True)
    except pandera.errors.SchemaError as err:
        print(err)


def pydantic_model():
    data = pandas.read_csv("us_tornado_dataset_1950_2021.csv")
    print(data.head())

    # data_inferred_schema = pandera.infer_schema(data)
    # with open("inferred_schema.py", "w") as file:
    #     file.write(data_inferred_schema.to_script())

    try:
        OutputSchema.validate(data, lazy=True)
    except pandera.errors.SchemaError as err:
        print(err)


if __name__ == '__main__':
    pydantic_model()