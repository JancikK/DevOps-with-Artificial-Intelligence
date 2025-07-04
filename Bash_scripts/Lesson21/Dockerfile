# Use Debian as the base image
FROM debian:latest

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package manager and install OpenSSH server and passwd utility
RUN apt-get update && \
    apt-get install -y openssh-server passwd python3 sudo && \
    mkdir /var/run/sshd

# Create a new user 'ansible'
RUN useradd -m -s /bin/bash ansible

# Set root password (optional, if you want to enable root login)
RUN echo 'root:password' | chpasswd

# Set password for 'ansible' (optional, passwordless SSH will be used)
RUN echo 'ansible:password' | chpasswd

# Add 'ansible' user to sudoers for passwordless sudo accessgit commit --allow-empty -m "Push image now that Docker Hub repo exists"
RUN echo 'ansible ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Allow root login over SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create .ssh directory for the ansible user and set permissions
RUN mkdir -p /home/ansible/.ssh && \
    chown ansible:ansible /home/ansible/.ssh && \
    chmod 700 /home/ansible/.ssh

RUN touch /home/ansible/.ssh/authorized_keys
# Set correct ownership and permissions for the authorized_keys file
RUN chown ansible:ansible /home/ansible/.ssh/authorized_keys && \
    chmod 600 /home/ansible/.ssh/authorized_keys

COPY test.sh /app/test.sh
RUN chmod +x /app/test.sh
WORKDIR /app

# Expose SSH port
EXPOSE 22

# Start SSH service and keep the container running
CMD ["/usr/sbin/sshd", "-D"]