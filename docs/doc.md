
- RabbitMq docker image
 
    ``` 
    docker run -d -p 15672:15672 -p 5672:5672 \ 
        --name rabbitMq \
        rabbitmq:3-management
    ```

- Install celery 

    ```pip install celery```

- Start celery module

    ```celery -A <module-name>  worker --loglevel=info -P eventlet```