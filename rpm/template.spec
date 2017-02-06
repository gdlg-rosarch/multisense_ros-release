Name:           ros-indigo-multisense-cal-check
Version:        4.0.0
Release:        0%{?dist}
Summary:        ROS multisense_cal_check package

Group:          Development/Libraries
License:        BSD
URL:            https://bitbucket.org/crl/multisense_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-multisense-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-multisense-ros

%description
multisense_cal_check

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Feb 06 2017 Carnegie Robotics <support@carnegierobotics.com> - 4.0.0-0
- Autogenerated by Bloom

* Fri Mar 04 2016 Carnegie Robotics <support@carnegierobotics.com> - 3.4.7-0
- Autogenerated by Bloom

* Tue Dec 01 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.6-0
- Autogenerated by Bloom

* Tue Oct 20 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.5-0
- Autogenerated by Bloom

* Thu Jun 25 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.4-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.3-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Carnegie Robotics <support@carnegierobotics.com> - 3.4.2-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.4.1-0
- Autogenerated by Bloom

* Thu Dec 11 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.4.0-0
- Autogenerated by Bloom

* Mon Dec 08 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.9-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.8-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.7-1
- Autogenerated by Bloom

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

