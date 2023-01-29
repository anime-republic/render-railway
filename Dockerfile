FROM ghcr.io/anime-republic/reborn:latest
COPY . .
CMD ["bash", "start.sh"]
