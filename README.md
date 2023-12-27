
# Gist: Per-request state vs global state

Demonstration of the danger of keeping a per-request state into
a non-per-request state (e.g. singleton / global state etc)

```shell
docker-compose up
```

```shell
./request-in-parallel.sh
```
