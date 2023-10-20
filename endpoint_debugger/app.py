from fastapi import FastAPI, Request
from pprint import pprint

DEBUG = False

app = FastAPI(
    docs_url=None,  # Disable docs (Swagger UI)
    redoc_url=None,  # Disable redoc
)


@app.get("/{full_path:path}")
@app.post("/{full_path:path}")
async def root(request: Request, full_path: str):
    title_size = 25

    print(f"{'path'.center(title_size, '#')}\n{full_path}")

    print(f"{'query_params'.center(title_size, '#')}\n{request.query_params}")
    print(f"{'query params dict'.center(title_size, '#')}")
    pprint(dict(request.query_params))
    print("")

    print(f"{'headers'.center(title_size, '#')}")
    pprint(dict(request.headers))
    print("")

    print(f"{'Cloudflare IP'.center(title_size, '#')}")
    print(request.headers.get("cf-connecting-ip"))
    print("")

    raw_body = await request.body()
    print(f"{'raw_body'.center(title_size, '#')}->\n{raw_body}")
    print("")

    if raw_body:
        body = await request.json()
    else:
        print("Body is empty")
        body = None

    print(f"{'body'.center(title_size, '#')}->")
    pprint(body)
    print("")

    if (DEBUG):
        return {
            "path": full_path,
            "raw_query_params": str(request.query_params),
            "query_params": request.query_params,
            "raw_body": raw_body,
            "body": body,
        }
    else:
        return {}
