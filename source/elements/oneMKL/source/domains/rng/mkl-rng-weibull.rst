.. _onemkl_rng_weibull:

weibull
=======

Class is used for generation of Weibull distributed real types random numbers.

.. _onemkl_rng_weibull_description:

.. rubric:: Description

The class object is used in :ref:`oneapi::mkl::rng::generate()<onemkl_rng_generate>` function to provide random numbers Weibull distributed with displacement :math:`a`, scalefactor :math:`\beta`, and shape :math:`\alpha`, where :math:`a, \beta, \alpha \in R; \alpha > 0; \beta > 0`.

The probability distribution is given by:

.. math::

    f_{a, \alpha, \beta}(x) = \left\{ \begin{array}{rcl} \frac{\alpha}{\beta^\alpha}(x - a)^{\alpha - 1}exp((-\frac{x - a}{\beta})^{\alpha}), x \ge a \\ 0, x < a \end{array}\right.

The cumulative distribution function is as follows:

.. math::

    F_{a, \alpha, \beta}(x) = \left\{ \begin{array}{rcl} 1 - exp((-\frac{x - a}{\beta})^{\alpha}), x \ge a \\ 0, x < a \end{array}\right.

.. _onemkl_rng_weibull_syntax:

class weibull
-------------

.. rubric:: Syntax

.. code-block:: cpp

    template<typename RealType = float, typename Method = weibull_method::by_default>
    class weibull {
    public:
        using method_type = Method;
        using result_type = RealType;
        weibull();
        explicit weibull(RealType alpha, RealType a, RealType b);
        RealType alpha() const;
        RealType a() const;
        RealType beta() const;
    };

.. cpp:class:: template<typename RealType = float, typename Method = oneapi::mkl::rng::weibull_method::by_default> \
                oneapi::mkl::rng::weibull

.. container:: section

    .. rubric:: Template parameters

    .. container:: section

        typename RealType
            Type of the produced values. Supported types:
                * ``float``
                * ``double``

    .. container:: section

        typename Method = oneapi::mkl::rng::weibull_method::by_default
            Transformation method, which will be used for generation. Supported types:

                * ``oneapi::mkl::rng::weibull_method::by_default``
                * ``oneapi::mkl::rng::weibull_method::icdf``
                * ``oneapi::mkl::rng::weibull_method::icdf_accurate``

            See description of the methods in :ref:`Distributions methods template parameter<onemkl_rng_distributions_template_parameter_mkl_rng_method_values>`

.. container:: section

    .. rubric:: Class Members

    .. list-table::
        :header-rows: 1

        * - Routine
          - Description
        * - `weibull()`_
          - Default constructor
        * - `explicit weibull(RealType alpha, RealType a, RealType beta)`_
          - Constructor with parameters
        * - `RealType alpha() const`_
          - Method to obtain shape value
        * - `RealType a() const`_
          - Method to obtain displacement value
        * - `RealType beta() const`_
          - Method to obtain scalefactor value

.. container:: section

    .. rubric:: Member types

    .. container:: section

        .. cpp:type:: weibull::method_type = Method

        .. container:: section

            .. rubric:: Description

            Type which defines transformation method for generation.

    .. container:: section

        .. cpp:type:: weibull::result_type = RealType

        .. container:: section

            .. rubric:: Description

            Type which defines type of generated random numbers.

.. container:: section

    .. rubric:: Constructors

    .. container:: section

        .. _`weibull()`:

        .. cpp:function:: weibull::weibull()

        .. container:: section

            .. rubric:: Description

            Default constructor for distribution, parameters set as `alpha` = 1.0, `a` = 0.0, and `b` = 1.0.

    .. container:: section

        .. _`explicit weibull(RealType alpha, RealType a, RealType beta)`:

        .. cpp:function:: explicit weibull::weibull(RealType alpha, RealType a, RealType beta)

        .. container:: section

            .. rubric:: Description

            Constructor with parameters. `alpha` is a shape value, `a` is a displacement value, `beta` is a scalefactor value.


.. container:: section

    .. rubric:: Characteristics

    .. container:: section

        .. _`RealType alpha() const`:

        .. cpp:function:: RealType weibull::alpha() const

        .. container:: section

            .. rubric:: Return Value

            Returns the distribution parameter `alpha` - shape value.

    .. container:: section

        .. _`RealType a() const`:

        .. cpp:function:: RealType weibull::a() const

        .. container:: section

            .. rubric:: Return Value

            Returns the distribution parameter `a` - displacement value.

    .. container:: section

        .. _`RealType beta() const`:

        .. cpp:function:: RealType weibull::beta() const

        .. container:: section

            .. rubric:: Return Value

            Returns the distribution parameter `beta` - scalefactor value.

**Parent topic:** :ref:`onemkl_rng_distributions`
