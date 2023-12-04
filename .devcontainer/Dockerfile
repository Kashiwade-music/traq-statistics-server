# Use the NVIDIA CUDA base image
FROM ubuntu:jammy

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && apt-get install -y \
    git \
    zsh \
    wget \
    sudo \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    mariadb-server \
    mariadb-client

# Create a new user named "vscode"
RUN useradd -m -s /bin/zsh vscode && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to the new user
USER vscode
WORKDIR /home/vscode

# Install Anaconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/anaconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
    echo "export PATH=$HOME/anaconda3/bin:$PATH" >> $HOME/.zshrc

# Install powerlevel10k
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $HOME/powerlevel10k && \
    echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >> $HOME/.zshrc

# Set default shell to zsh
SHELL ["/bin/zsh", "-l"]

# Install VSCode Server
# RUN curl -fsSL https://code-server.dev/install.sh | sh
# 
# # Expose the port used by VSCode Server
# EXPOSE 8080
# 
# # Start VSCode Server
# ENTRYPOINT [ "code-server" ]