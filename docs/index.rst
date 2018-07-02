Welcome to Skates' documentation!
#################################

Skates is a turn-key solution to deploy a complete set of scientific
computing core services that can be used as a base infrastructure for
data-science analysis.

The solution provides a set of basic services (that can be replaced
by existing in-house counterparts):

- LDAP authentication with web interface

- PostgreSQL_ database server with user and admin web interfaces

- Zabbix_-based monitoring with web interface

- File server for data sharing across many protocols (SAMBA, NFS, ...)
  
Scientific services include (all optional):

- Isolated login containers per group of users

- Jupyterhub_ shared service

- Support for scientific software libraries. Integrated support for applications available as Conda_ packages.

- SLURM_ Queuing support: can work as an administrator, head and compute node.


The system can be easily extended. We currently provide a Bioinformatics flavor that includes
a Galaxy_ server.

Skates is based on Linux, Terraform_, Kubernetes_ and Docker_.

Skates can be deployed on Bare Metal or Cloud Infrastructures (tested on Google Cloud).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install/index.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Conda: https://conda.io
.. _Docker: https://docker.com
.. _Galaxy: https://usegalaxy.org
.. _Jupyterhub: https://jupyter.org
.. _Kubernetes: https://kubernetes.io
.. _PostgreSQL: https://postgresql.org
.. _SLURM: https://slurm.schedmd.com
.. _Terraform: https://terraform.io
.. _Zabbix: https://zabbix.com
