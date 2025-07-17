FROM nginx:alpine

# Install wget for healthcheck support
RUN apk add --no-cache wget

# Copy your NGINX configuration
COPY default.conf /etc/nginx/conf.d/default.conf