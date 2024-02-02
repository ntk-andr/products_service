import uvicorn

uvicorn.run(
    'products_service.app:app',
    host="0.0.0.0",
    port=8080,
    # reload=True,
    
    log_config="log_conf.yml"
)

