##  Docker
- Dockerfile elkészítése, amiben szerepelnek a projekt függőségei
- docker-compose elkészítése az egyszerűbb kezelhetőség érdekében
- GitHub Actions készítése a Docker Image automatikus elkészítésére
  - megtekinthető DockerHub-on:
    - https://hub.docker.com/r/cicdemons/app

## Futtatás Docker-ben
Konténer elindítása
```sh
docker-compose up -d
```

Csatlakozás a konténer terminál interfészéhez.
```sh
docker-compose exec python bash
```

Yaay! Mostmár a futtathatók a [tesztek](https://github.com/BME-MIT-IET/iet-hf2021-ci-cdemons#tests) vagy RELP-ben is kipróbálható a könyvtár. 

```sh
python
```
