Name:           ros-indigo-multisense-lib
Version:        3.3.7
Release:        0%{?dist}
Summary:        ROS multisense_lib package

Group:          Development/Libraries
License:        BSD
URL:            https://bitbucket.org/crl/multisense_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       libpng-devel
Requires:       ros-indigo-cv-bridge
BuildRequires:  libpng-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge

%description
multisense_lib

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Nov 25 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.7-0
- Autogenerated by Bloom

* Mon Nov 10 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.6-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.5-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.4-0
- Autogenerated by Bloom

* Fri Oct 24 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.3-0
- Autogenerated by Bloom

* Thu Oct 23 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.2-0
- Autogenerated by Bloom

