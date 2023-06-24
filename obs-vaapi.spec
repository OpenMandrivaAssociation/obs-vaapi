Name:		obs-vaapi
Version:	0.3.0
Release:	1
License:	GPLv2.0
Group:		Video
Summary:	OBS Studio VAAPI support via GStreamer
Url:		https://github.com/fzwoch/obs-vaapi/
Source0:	https://github.com/fzwoch/obs-vaapi/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	meson
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libpci)

Requires: obs-studio
Requires: vulkan-loader
Requires: gstreamer1.0-vaapi
Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-bad
Requires: gstreamer1.0-plugins-ugly

%description
GStreamer based VAAPI encoder implementation. Taken out of the GStreamer OBS plugin as a standalone plugin. 
Simply because the FFMPEG VAAPI implementation shows performance bottlenecks on some AMD hardware.
Supports H.264 and H.265.
Note that not all options in the encoder properties may be working. 
VAAPI is just an interface and it is up to the GPU hardware and driver what is actually supported. Not all options make sense to change.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson \
        --prefix=%{_libdir}/obs-plugins \
        --libdir=%{_libdir}/obs-plugins \
        --buildtype=release

%meson_build

%install
%meson_install

%files
%{_libdir}/obs-plugins/obs-vaapi.so
