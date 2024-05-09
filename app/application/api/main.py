from fastapi import FastAPI


def create_app():
    return FastAPI(
        title="Arbitrum API",
        docs_url='/api/docs'
    )