Name:           ros-indigo-fetch-pbd-interaction
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS fetch_pbd_interaction package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-couchdb
Requires:       ros-indigo-fetch-arm-control
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-interactive-marker-proxy
Requires:       ros-indigo-interactive-markers
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-moveit-commander
Requires:       ros-indigo-rail-manipulation-msgs
Requires:       ros-indigo-rail-segmentation > 0.1.9-0
Requires:       ros-indigo-rosbridge-server
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rospy-message-converter
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf2-web-republisher
BuildRequires:  python-couchdb
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-fetch-arm-control
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-interactive-marker-proxy
BuildRequires:  ros-indigo-interactive-markers
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-moveit-commander
BuildRequires:  ros-indigo-rail-manipulation-msgs
BuildRequires:  ros-indigo-rail-segmentation
BuildRequires:  ros-indigo-rosbridge-server
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rospy-message-converter
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf2-web-republisher

%description
The fetch_pbd_interaction package

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
* Fri Sep 09 2016 Sarah Elliott <sksellio@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Fri Sep 09 2016 Sarah Elliott <sksellio@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Fri Sep 09 2016 Sarah Elliott <sksellio@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Fri Sep 09 2016 Sarah Elliott <sksellio@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

