# Docker registry gcs driver

This is a [docker-registry backend driver](https://github.com/dotcloud/docker-registry/tree/master/depends/docker-registry-core) based on the [gcs](http://reverbrain.com/gcs/) key-value storage.

[![PyPI version][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]

## Usage

Assuming you have a working docker-registry and gcs setup.

`pip install docker-registry-driver-gcs`

Edit your configuration so that `storage` reads `gcs`.


## Options

You may add any of the following to your main docker-registry configuration to further configure it.

These options configure your [Google Cloud Storage](https://cloud.google.com/products/cloud-storage/) storage.
These are used when `storage` is set to `gcs`.

1. `boto_bucket`: string, the bucket name
1. `storage_path`: string, the sub "folder" where image data will be stored.
1. `oauth2`: boolean, true to enable [OAuth2.0](https://developers.google.com/accounts/docs/OAuth2)

Example:
```yaml
dev:
  boto_bucket: "_env:GCS_BUCKET"
  storage: gcs
  storage_path: "_env:STORAGE_PATH:/"
  oauth2: true
```

You can also use [developer keys](https://developers.google.com/storage/docs/reference/v1/getting-startedv1#keys) for (if `oauth2` is unset or set to false) instead
of using [OAuth2.0](https://developers.google.com/accounts/docs/OAuth2). Options to configure then:

1. `gs_access_key`: string, GCS access key
1. `gs_secret_key`: string, GCS secret key
1. `gs_secure`: boolean, true for HTTPS to GCS

Example:
```yaml
dev:
  boto_bucket: "_env:GCS_BUCKET"
  storage: gcs
  storage_path: "_env:STORAGE_PATH:/"
  gs_access_key: GOOGTS7C7FUP3AIRVJTE
  gs_secret_key: bGoa+V7g/yqDXvKRqq+JTFn4uQZbPiQJo4pf9RzJ
  gs_secure: false
```

## Developer setup

Clone this.

Get your python ready:

```
sudo apt-get install python-pip
sudo pip install tox
```

Start the test gcs:

```
cd fixtures
sudo ./start.sh
```

You are ready to hack.
In order to verify what you did is ok:
 * run `tox`
 * alternatively, run `python setup.py nosetests` to only run tests on the system python

This will run the tests provided by [`docker-registry-core`](https://github.com/dotcloud/docker-registry/tree/master/depends/docker-registry-core)


## License

This is licensed under the Apache license.
Most of the code here comes from docker-registry, under an Apache license as well.

[pypi-url]: https://pypi.python.org/pypi/docker-registry-driver-gcs
[pypi-image]: https://badge.fury.io/py/docker-registry-driver-gcs.svg

[travis-url]: http://travis-ci.org/dmp42/docker-registry-driver-gcs
[travis-image]: https://secure.travis-ci.org/dmp42/docker-registry-driver-gcs.png?branch=master
