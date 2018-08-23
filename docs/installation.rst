.. highlight:: shell

.. _installation:

============
Installation
============

In order to develop code for the data quality proof of concept site on your own machine, first create a directory (:file:`data_quality`, say) and change to it.

.. code-block:: bash
  
  mkdir data_quality
  cd data_quality

Create a virtual environment (this is optional, but highly recommended), and activate it.

.. code-block:: bash
  
  python3 -mvenv venv
  source venv/bin/activate

Download the code from `https://github.com/hettlage/data-quality-poc <https://github.com/hettlage/data-quality-poc>`_ and change to the created directory.

.. code-block:: bash
  
  git clone https://github.com/hettlage/data-quality-poc.git
  cd data-quality-poc

Install the site with :command:`pip`. Note that you should include the ``-e`` flag, so that your updates to the code take effect without you having to re-install the package.

.. code-block:: bash
  
  pip install -e .

You can now start the website with the :command:`flask` command.

.. code-block:: bash
  
  export FLASK_APP=dq_poc/dq_poc.py
  export FLASK_DEBUG=1
  flask run

Point your browser to `http://127.0.0.1:5000/ <http://127.0.0.1:5000/>`_ in order view the site. The Flask server can be terminated with ``Ctrl-C``.