Repo to learn and test ai agents. 

To run the agent in docker - run the docker compose ``` docker-compose build aiagent ```
if doing for the first time, will have to exec into ollama container and pull llama3. 
```
docker exec -it <containerId> bash
ollama pull llama3
```
exit and restart the aiagent container
```
docker-compose up
```
Exec into aiagent container and try running main.py file to debug. Try running curl http://ollama:11434 to test ollama connection. 
