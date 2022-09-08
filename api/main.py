from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
from src.utils import bionic_research_try

class Data(BaseModel):
    text: Union[str, List[str]]

tags = [
    {
        "name":"boldy-text",
        "description":"Make the important part of words bold in a text",
    },
]

app = FastAPI(
    title="Boldy Text",
    description="""This is an API to simulate the work done by Bionic Research.""",
    openapi_tags=tags,
)

from IPython.display import display, Markdown

@app.post('/boldy', tags=["boldy-text"])
async def keywords_filter(text:Data):
    bold_text = bionic_research_try(text.text)
    display(Markdown(bold_text))