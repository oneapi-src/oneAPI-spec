.. _onemkl_lapack_orgqr_scratchpad_size:

onemkl::lapack::orgqr_scratchpad_size
=====================================


.. container::


   Computes size of scratchpad memory required for :ref:`onemkl_lapack_orgqr` function.


         ``orgqr_scratchpad_size`` supports the following precisions.


         .. list-table:: 
            :header-rows: 1

            * -  T 
            * -  ``float`` 
            * -  ``double`` 




   .. container:: section


      .. rubric:: Description
         :class: sectiontitle


      Computes the number of elements of type T the scratchpad memory to be passed to :ref:`onemkl_lapack_orgqr` function should be able to hold.
      Calls to this routine must specify the template parameter explicitly.


onemkl::lapack::orgqr_scratchpad_size
-------------------------------------

.. container::

   .. container:: section


      .. rubric:: Syntax
         :class: sectiontitle


      .. container:: dlsyntaxpara


         .. cpp:function::  template <typename T>std::int64_t         onemkl::lapack::orgqr_scratchpad_size(cl::sycl::queue &queue, std::int64_t m, std::int64_t         n, std::int64_t k, std::int64_t lda)

   .. container:: section


      .. rubric:: Input Parameters
         :class: sectiontitle


      queue
         Device queue where calculations by :ref:`onemkl_lapack_orgqr` function will be performed.


      m
         The number of rows in the matrix ``A`` (``0≤m``).


      n
         The number of columns in the matrix ``A`` (``0≤n≤m``).


      k
         The number of elementary reflectors whose product defines the
         matrix ``Q`` (``0≤k≤n``).


      lda
         The leading dimension of a.


   .. container:: section


      .. rubric:: Throws
         :class: sectiontitle


      onemkl::lapack::exception
         Exception is thrown in case of incorrect argument value is supplied.
         Position of wrong argument can be determined by `get_info()` method of exception object.


   .. container:: section


      .. rubric:: Return Value
         :class: sectiontitle


      The number of elements of type T the scratchpad memory to be passed to :ref:`onemkl_lapack_orgqr` function should be able to hold.


.. container:: familylinks


   .. container:: parentlink


      **Parent topic:** :ref:`onemkl_lapack-linear-equation-routines` 

