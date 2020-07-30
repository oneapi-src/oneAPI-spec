.. _onemkl_dft_compute_forward:

compute_forward
===============

This function computes the forward transform defined by an instantiation of the :ref:`onemkl_dft_descriptor` class.

.. _onemkl_dft_compute_forward_description:

.. rubric:: Description

The compute_forward function accepts the :ref:`onemkl_dft_descriptor` and one or more data parameters and in the case of USM data, any ``syc::event`` dependencies.  Given a successfully configured and committed descriptor, this function computes the forward transform, that is, the :ref:`transform<onemkl_dft_formula>` with the minus sign, :math:`\delta=-1`, in the exponent.

The configuration parameters ``config_param::COMPLEX_STORAGE``, ``config_param::REAL_STORAGE`` and ``config_param::CONJUGATE_EVEN_STORAGE`` define the layout of the input and output data and must be properly set in a call to :ref:`onemkl_dft_descriptor_set_value`.

.. note::
   The compute_forward function may need to access the internals and private/protected members of the :ref:`onemkl_dft_descriptor` class.  This could be done, for instance, by labeling it as a friend function to the descriptor class.   


.. onemkl_dft_compute_forward_buffer:

compute_forward (Buffer version)
---------------------------------

.. rubric:: Syntax (In-place transform)

.. cpp:function:: template <typename IOType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    void oneapi::mkl::dft::compute_forward(\
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        sycl::buffer<IOType, 1> &inout);

.. rubric:: Syntax (In-place transform, using ``config_param::COMPLEX_STORAGE=config_value::REAL_REAL`` :ref:`data format<onemkl_dft_complex_storage>` )

.. cpp:function:: template <typename IOType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    void oneapi::mkl::dft::compute_forward(\
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        sycl::buffer<IOType, 1> &inout_re, \
                sycl::buffer<IOType, 1> &inout_im);


.. rubric:: Syntax (Out-of-place transform)

.. cpp:function:: template <typename IType, typename OType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    void oneapi::mkl::dft::compute_forward( \
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        sycl::buffer<IType, 1> &in, \
	        sycl::buffer<OType, 1> &out);

.. rubric:: Syntax (Out-of-place transform, using ``config_param::COMPLEX_STORAGE=config_value::REAL_REAL`` :ref:`data format<onemkl_dft_complex_storage>` )

.. cpp:function:: template <typename IType, typename OType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    void oneapi::mkl::dft::compute_forward( \
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        sycl::buffer<IType, 1> &in_re, \
	        sycl::buffer<IType, 1> &in_im, \
	        sycl::buffer<OType, 1> &out_re,\
                sycl::buffer<OType, 1> &out_im);



.. container:: section

   .. rubric:: Input Parameters

   :ref:`onemkl_dft_descriptor`
      A fully configured and committed discrete Fourier transform description, defining the type of transformation and data layout to be applied. At commit time, the ``sycl::queue`` has already been provided.

   inout
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house both the input and output data sequences for the in-place transformation. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_re
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_im
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   in
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the input data sequence for the out-of-place transformation. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   in_re
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of input data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   in_im
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of input data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.



.. container:: section

   .. rubric:: Output Parameters

   inout
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house both the input and output data sequences for the in-place transformation. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_re
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_im
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   out
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the output data sequence for the out-of-place transformation. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   out_re
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of output data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   out_im
      Sycl buffer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of output data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.





.. onemkl_dft_compute_forward_usm:

compute_forward (USM version)
---------------------------------

.. rubric:: Syntax (In-place transform)

.. cpp:function:: template <typename IOType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    sycl::event oneapi::mkl::dft::compute_forward(\
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        IOType *in, \
	        const cl::sycl::vector_class<cl::sycl::event> &dependencies = {});

.. rubric:: Syntax (In-place transform, using ``config_param::COMPLEX_STORAGE=config_value::REAL_REAL`` :ref:`data format<onemkl_dft_complex_storage>` )

.. cpp:function:: template <typename IOType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    sycl::event oneapi::mkl::dft::compute_forward(\
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        IOType *in_re, \
	        IOType *in_im, \
	        const cl::sycl::vector_class<cl::sycl::event> &dependencies = {});



.. rubric:: Syntax (Out-of-place transform)

.. cpp:function:: template <typename IType, typename OType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    sycl::event oneapi::mkl::dft::compute_forward( \
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        IType *in, \
	        OType *out, \
	        const cl::sycl::vector_class<cl::sycl::event> &dependencies = {})

.. rubric:: Syntax (Out-of-place transform, using ``config_param::COMPLEX_STORAGE=config_value::REAL_REAL`` :ref:`data format<onemkl_dft_complex_storage>` )

.. cpp:function:: template <typename IType, typename OType, oneapi::mkl::dft::precision prec, oneapi::mkl::dft::domain dom>\
	    sycl::event oneapi::mkl::dft::compute_forward( \
                oneapi::mkl::dft::descriptor<prec,dom> &descriptor, \
	        IType *in_re, \
	        IType *in_im, \
	        OType *out_re, \
	        OType *out_im, \
	        const cl::sycl::vector_class<cl::sycl::event> &dependencies = {})


.. container:: section

   .. rubric:: Input Parameter

   :ref:`onemkl_dft_descriptor`
      A fully configured and committed discrete Fourier transform description, defining the type of transformation and data layout to be applied. At commit time, the ``sycl::queue`` has already been provided.

   inout
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house both the input and output data sequences for the in-place transformation. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_re
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_im
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   in
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the input data sequence for the out-of-place transformation. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   in_re
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of the input data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.
  
   in_im
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of the input data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.
 
   dependencies
      A vector of ``sycl::event``'s that represent the previously enqueued tasks that must be finished before this transformation can be started.

.. container:: section

   .. rubric:: Output Parameters


   inout
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house both the input and output data sequences for the in-place transformation. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_re
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   inout_im
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of both the input and output data sequences for the in-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   out
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the output data sequence for the out-of-place transformation. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.

   out_re
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the real part of the output data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.
  
   out_im
      USM pointer containing an array of length no less than is specified at the :ref:`descriptor construction<onemkl_dft_descriptor_constructor>` time to house the imaginary part of the output data sequence for the out-of-place transformation when using the ``config_value::REAL_REAL`` format for the ``config_param::COMPLEX_STORAGE`` configuration parameter. Corresponds to the choice of ``config_value::NOT_INPLACE`` for the configuration parameter ``config_param::PLACEMENT``.
 


.. container:: section

   .. rubric:: Return Values

   This function returns a ``sycl::event`` that allows to track progress of this transformation, and can be passed as a dependency to other routines that may depend on the results of this transformation to be finished before proceeding with the other operations.


**Parent topic:** :ref:`onemkl_dft`


