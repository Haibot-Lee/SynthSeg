import datetime
import timeit
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import logging

from service.SynthSeg_predict import process_imgs

logger = logging.getLogger("main:app")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename="logs/app.log", encoding="utf-8", mode="a")
formatter = logging.Formatter("%(asctime)s\t%(levelname)s\t%(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    # log to file
    handler = logging.FileHandler(filename="logs/api.log", encoding="utf-8", mode="a")
    handler.setFormatter(logging.Formatter("%(asctime)s\t%(levelname)s\t%(message)s"))
    logger.addHandler(handler)


@app.get("/hello/{name}")
async def say_hello(name: str = "World"):
    return {"message": f"Hello {name}"}


class Args(BaseModel):
    input: str
    output: str
    parc: Union[bool, None] = False
    robust: Union[bool, None] = False
    fast: Union[bool, None] = False
    ct: Union[bool, None] = False
    vol: Union[str, None] = None
    qc: Union[str, None] = None
    post: Union[str, None] = None
    resample: Union[str, None] = None
    crop: Union[list, None] = None
    threads: Union[int, None] = 1
    cpu: Union[bool, None] = False
    v1: Union[bool, None] = False

    def to_dict(self):
        return {'i': self.input, 'o': self.output, 'parc': self.parc, 'robust': self.robust, 'fast': self.fast,
                'ct': self.ct, 'vol': self.vol, 'qc': self.qc, 'post': self.post, 'resample': self.resample,
                'crop': self.crop, 'threads': self.threads, 'cpu': self.cpu, 'v1': self.v1}


@app.post("/predict")
async def exec_predict(args: Args):
    logger.info("Start prediction...")
    start_time = timeit.default_timer()

    process_imgs(args.to_dict())

    logger.info("Prediction end!")
    time_used = timeit.default_timer() - start_time
    m, s = divmod(time_used, 60)
    logger.info("Duration: %dmin%ds(%ds)" % (m, s, time_used))
