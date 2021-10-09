# This is the Dockerfile of syntax_checker image used in CircleCI
FROM python:3.7

RUN set -x \
    && echo "deb http://deb.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/stretch-backports.list \
    && echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y ansible \
    && python3 -m pip install --no-cache-dir flake8 mypy py532lib \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /root/.cache* \
    && rm -rf /tmp/* \
;
