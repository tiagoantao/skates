Installation
************

Requirements
============

Infrastructure
--------------

Skates can be installed on Bare Metal or Cloud providers. Currently we tested on Google Cloud.

.. warning:: **Kubernetes on the cloud**

   We currently do all the Kubernetes management manually. This means that we do not create vendor locking, but management of the
   Kubernetes cluster is (y)our responsibility. In the future we might do specialized configurations targeting proprietary cloud
   extensions supporting Kubernetes (and Docker). In practice this means that in Google Cloud we create and manage all kubernetes
   infrastructure.


Software
--------

- Linux
- Terraform
- Kubernetes
- Docker

**If you use the setup wizard** (strongly recommended for a first install)

- Python 3
- Flask
- openssl and pyOpenSSL (if you need to generate keys)



Installation
============

