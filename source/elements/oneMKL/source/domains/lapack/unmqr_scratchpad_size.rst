.. _onemkl_lapack_unmqr_scratchpad_size:

unmqr_scratchpad_size
=====================

Computes size of scratchpad memory required for :ref:`onemkl_lapack_unmqr` function.

.. container:: section

  .. rubric:: Description
         
``unmqr_scratchpad_size`` supports the following precisions.

     .. list-table:: 
        :header-rows: 1

        * -  T 
        * -  ``std::complex<float>`` 
        * -  ``std::complex<double>`` 

Computes the number of elements of type ``T`` the scratchpad memory to be passed to :ref:`onemkl_lapack_unmqr` function should be able to hold.
Calls to this routine must specify the template parameter
explicitly.

unmqr_scratchpad_size
---------------------

.. container:: section

  .. rubric:: Syntax
         
.. cpp:function::  template <typename T>std::int64_t         oneapi::mkl::lapack::unmqr_scratchpad_size(cl::sycl::queue &queue, onemkl::side left_right,         onemkl::transpose trans, std::int64_t m, std::int64_t n,         std::int64_t k, std::int64_t lda, std::int64_t ldc,         std::int64_t &scratchpad_size)

.. container:: section

  .. rubric:: Input Parameters
         
queue
   Device queue where calculations by :ref:`onemkl_lapack_unmqr` function will be performed.

left_right
   If ``left_right=onemkl::side::left``, :math:`Q` or :math:`Q^{H}` is
   applied to :math:`C` from the left.

   If ``left_right=onemkl::side::right``, :math:`Q` or :math:`Q^{H}` is
   applied to :math:`C` from the right.

trans
   If ``trans=onemkl::transpose::trans``, the routine multiplies
   :math:`C` by :math:`Q`.

   If ``trans=onemkl::transpose::conjtrans``, the routine multiplies
   :math:`C` by :math:`Q^H`.

m
   The number of rows in the matrix :math:`A` (:math:`0 \le m`).

n
   The number of columns the matrix :math:`A` (:math:`0 \le n \le m`).

k
   The number of elementary reflectors whose product defines the
   matrix :math:`Q` (:math:`0 \le k \le n`).

lda
   The leading dimension of ``a``.

ldc
   The leading dimension of ``c``.

.. container:: section

  .. rubric:: Return Value
         
The number of elements of type ``T`` the scratchpad memory to be passed to :ref:`onemkl_lapack_unmqr` function should be able to hold.

**Parent topic:** :ref:`onemkl_lapack-linear-equation-routines`

