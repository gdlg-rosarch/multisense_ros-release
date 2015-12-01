Name:           ros-jade-multisense-ros
Version:        3.4.6
Release:        0%{?dist}
Summary:        ROS multisense_ros package

Group:          Development/Libraries
License:        BSD
URL:            https://bitbucket.org/crl/multisense_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-angles
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-genmsg
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-geometry
Requires:       ros-jade-image-transport
Requires:       ros-jade-message-generation
Requires:       ros-jade-message-runtime
Requires:       ros-jade-multisense-lib
Requires:       ros-jade-rosbag
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-stereo-msgs
Requires:       ros-jade-tf
Requires:       turbojpeg-devel
BuildRequires:  ros-jade-angles
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-genmsg
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-message-runtime
BuildRequires:  ros-jade-multisense-lib
BuildRequires:  ros-jade-rosbag
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-stereo-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  turbojpeg-devel
BuildRequires:  yaml-cpp-devel

%description
multisense_ros

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Dec 01 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.6-0
- Autogenerated by Bloom

* Wed Oct 21 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.5-0
- Autogenerated by Bloom

* Thu Jun 25 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.4-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.3-0
- Autogenerated by Bloom

