<!--![GitHub All Releases](https://img.shields.io/github/downloads/ali-zahedi/appicon/total)-->
<!--![GitHub issues](https://img.shields.io/github/issues/ali-zahedi/appicon)-->
![GitHub](https://img.shields.io/github/license/ali-zahedi/appicon)
![GitHub](https://img.shields.io/pypi/pyversions/appicon.svg?maxAge=2592000)
![GitHub](https://img.shields.io/pypi/v/appicon.svg?maxAge=2592000)
# AZ App Icon config

[[_TOC_]]


## Intro

When you want to publish your app, you should provide a high-resolution app icon. App icon is the main representation of your app in users mobile devices. The process of generating app icon is different for each mobile platform. You should spend time and efforts on generating app icon in different resolutions for android and iOS. It's not a concern anymore, AZ app icon generates app icons for many different devices and resolutions on android/iOS for free. Then you can easily add the icon files to your project.

## Install with `pip`

```shell script
pip install appicon
```

## How to use it?

First of all you should be generate icons with `icon_generate` function.

```python
from appicon import icon_generate


directory_path = icon_generate(logo_path='~/logo.png', destination_directory='~/icons', is_zip=False)
```

![image info](./tree_after_generate.png)

If you want to move in to `zip` file you can pass argument `is_zip=True`.

```python
from appicon import icon_generate


zip_path = icon_generate(logo_path='~/logo.png', destination_directory='~/icons', is_zip=True)

```  

## Support

1. iOS

1. Android

# TODO

- [X] Documentation

## Contributors

Thanks to:

1. [@oxcug](https://github.com/oxcug) for the update xcode 13 support.


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.


