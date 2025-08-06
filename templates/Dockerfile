FROM kalilinux/kali-rolling

# Install full Kali
RUN apt-get update && apt-get install -y \
    kali-linux-large python3 python3-pip sudo git curl wget \
    cmake g++ make libjson-c-dev libwebsockets-dev \
    && apt-get clean

# Install ttyd
RUN git clone https://github.com/tsl0922/ttyd.git /opt/ttyd && \
    cd /opt/ttyd && mkdir build && cd build && cmake .. && make && make install && \
    cd / && rm -rf /opt/ttyd

# Create user and workspace
RUN useradd -ms /bin/bash dashboarduser
USER dashboarduser
WORKDIR /home/dashboarduser

# Copy recon scripts
COPY --chown=dashboarduser:dashboarduser ../recon_tools ./recon_tools
RUN chmod +x ./recon_tools/*.sh