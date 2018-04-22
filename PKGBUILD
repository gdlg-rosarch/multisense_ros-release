# Script generated with Bloom
pkgdesc="ROS - multisense_ros"
url='https://bitbucket.org/crl/multisense_ros'

pkgname='ros-kinetic-multisense-ros'
pkgver='4.0.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('libjpeg-turbo'
'ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-genmsg'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-geometry'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-multisense-lib'
'ros-kinetic-rosbag'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf'
'yaml-cpp'
)

depends=('libjpeg-turbo'
'ros-kinetic-angles'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-genmsg'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-geometry'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-multisense-lib'
'ros-kinetic-rosbag'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-stereo-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=multisense_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/multisense_ros $srcdir/multisense_ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

