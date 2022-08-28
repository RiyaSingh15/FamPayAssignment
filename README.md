Setup
- Open docker-compose.yaml file.
- Fill your secrets under environment section, like `SECRET_KEY`, `GOOOGLE_API_KEY` and `MAX_DEPTH` constant
- Install [docker desktop](https://docs.docker.com/desktop/) or [docker engine](https://docs.docker.com/engine/install/).


Running the project

- Run the following command to start the server 
```
docker-compose up --build
```
- Visit `localhost:8000` to see the dashboard.


API
- GET `/video`
    - params: 
        - title: string containing the substring of title
        - description: string containing the substring of description
        - offset: Offset to the paginated request
        - limit: Number of results to be sent by the server
    - response: 
        - count: Number of total results based on the request
        - next: Link to next page containing offset and limit and other params(if any)
        - previous: Link to next page containing offset and limit and other params(if any)
        - results: List containing json objects of video
            - video object has following attributes:
                - id: unique string or video id
                - title: title of the video
                - description: description of the video
                - thumbnails: thumbnails details of the video
                - published_at: published datetime of the video

You can hit the api from any CLI client(curl) or desktop client(Postman)


For any queries please reach out to me at my [mail](mailto:r.riyasingh.s15@gmail.com)