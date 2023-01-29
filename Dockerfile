FROM ghcr.io/anime-republic/wzml:latest
COPY . .
CMD ["bash", "start.sh"]
