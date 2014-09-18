# This builds on some iRODS compatible items.
# Ultimately, we will be getting an environment variable for which collection
# to use.

FROM      ytproject/yt-devel:latest
MAINTAINER Matthew Turk "matthewturk@gmail.com"
#
# install package dependencies to prevent Docker build from erring out
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y `dpkg -I /home/admin/irods-icommands-4.0.3-64bit.deb | sed -n 's/^ Depends: //p' | sed 's/,//g'`
RUN dpkg -i /home/admin/irods-icommands-4.0.3-64bit.deb
