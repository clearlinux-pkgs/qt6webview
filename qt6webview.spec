#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : qt6webview
Version  : 6.7.3
Release  : 20
URL      : https://download.qt.io/official_releases/qt/6.7/6.7.3/submodules/qtwebview-everywhere-src-6.7.3.zip
Source0  : https://download.qt.io/official_releases/qt/6.7/6.7.3/submodules/qtwebview-everywhere-src-6.7.3.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6webview-lib = %{version}-%{release}
Requires: qt6webview-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6webview package.
Group: Development
Requires: qt6webview-lib = %{version}-%{release}
Provides: qt6webview-devel = %{version}-%{release}
Requires: qt6webview = %{version}-%{release}

%description dev
dev components for the qt6webview package.


%package lib
Summary: lib components for the qt6webview package.
Group: Libraries
Requires: qt6webview-license = %{version}-%{release}

%description lib
lib components for the qt6webview package.


%package license
Summary: license components for the qt6webview package.
Group: Default

%description license
license components for the qt6webview package.


%prep
%setup -q -n qtwebview-everywhere-src-6.7.3
cd %{_builddir}/qtwebview-everywhere-src-6.7.3
pushd ..
cp -a qtwebview-everywhere-src-6.7.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727912529
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1727912529
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6webview
cp %{_builddir}/qtwebview-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6webview/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtwebview-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6webview/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtwebview-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6webview/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtwebview-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6webview/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtWebView/6.7.3/QtWebView/private/qabstractwebview_p.h
/usr/include/QtWebView/6.7.3/QtWebView/private/qnativeviewcontroller_p.h
/usr/include/QtWebView/6.7.3/QtWebView/private/qwebview_p.h
/usr/include/QtWebView/6.7.3/QtWebView/private/qwebviewfactory_p.h
/usr/include/QtWebView/6.7.3/QtWebView/private/qwebviewinterface_p.h
/usr/include/QtWebView/6.7.3/QtWebView/private/qwebviewloadrequest_p.h
/usr/include/QtWebView/6.7.3/QtWebView/private/qwebviewplugin_p.h
/usr/include/QtWebView/QtWebView
/usr/include/QtWebView/QtWebViewDepends
/usr/include/QtWebView/QtWebViewVersion
/usr/include/QtWebView/qtwebviewfunctions.h
/usr/include/QtWebView/qtwebviewversion.h
/usr/include/QtWebView/qwebview_global.h
/usr/include/QtWebViewQuick/6.7.3/QtWebViewQuick/private/qquickviewcontroller_p.h
/usr/include/QtWebViewQuick/6.7.3/QtWebViewQuick/private/qquickwebview_p.h
/usr/include/QtWebViewQuick/6.7.3/QtWebViewQuick/private/qquickwebviewloadrequest_p.h
/usr/include/QtWebViewQuick/6.7.3/QtWebViewQuick/private/qquickwebviewsettings_p.h
/usr/include/QtWebViewQuick/6.7.3/QtWebViewQuick/private/qtwebviewquickglobal_p.h
/usr/include/QtWebViewQuick/QtWebViewQuick
/usr/include/QtWebViewQuick/QtWebViewQuickDepends
/usr/include/QtWebViewQuick/QtWebViewQuickVersion
/usr/include/QtWebViewQuick/qtwebviewquickversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtWebViewTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtwebviewquickpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtwebviewquickpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtwebviewquickpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtwebviewquickpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtwebviewquickpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtwebviewquickpluginTargets.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewConfig.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewConfigVersion.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewDependencies.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewPlugins.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewTargets.cmake
/usr/lib64/cmake/Qt6WebView/Qt6WebViewVersionlessTargets.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickConfig.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickConfigVersion.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickDependencies.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickTargets.cmake
/usr/lib64/cmake/Qt6WebViewQuick/Qt6WebViewQuickVersionlessTargets.cmake
/usr/lib64/libQt6WebView.prl
/usr/lib64/libQt6WebView.so
/usr/lib64/libQt6WebViewQuick.prl
/usr/lib64/libQt6WebViewQuick.so
/usr/lib64/pkgconfig/Qt6WebView.pc
/usr/lib64/pkgconfig/Qt6WebViewQuick.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_webview.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_webview_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_webviewquick.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_webviewquick_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6WebView.so.6.7.3
/V3/usr/lib64/libQt6WebViewQuick.so.6.7.3
/V3/usr/lib64/qt6/qml/QtWebView/libqtwebviewquickplugin.so
/usr/lib64/libQt6WebView.so.6
/usr/lib64/libQt6WebView.so.6.7.3
/usr/lib64/libQt6WebViewQuick.so.6
/usr/lib64/libQt6WebViewQuick.so.6.7.3
/usr/lib64/qt6/metatypes/qt6webview_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6webviewquick_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/WebView.json
/usr/lib64/qt6/modules/WebViewQuick.json
/usr/lib64/qt6/qml/QtWebView/libqtwebviewquickplugin.so
/usr/lib64/qt6/qml/QtWebView/plugins.qmltypes
/usr/lib64/qt6/qml/QtWebView/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6webview/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6webview/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6webview/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6webview/dc8f2e570bf431427dbc3bab9d4d551b53a60208
