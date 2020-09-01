Operation Attributes
====================

oneCCL specification defines communication operation attributes that serve as modifiers of an operation's behavior. Optionally, they may be passed to the corresponding communication operations.

oneCCL specification defines the following operation attribute classes:

- ``allgatherv_attr``
- ``allreduce_attr``
- ``alltoall_attr``
- ``alltoallv_attr``
- ``barrier_attr``
- ``broadcast_attr``
- ``reduce_attr``
- ``reduce_scatter_attr``

oneCCL specification defines attribute identifiers that may be used to fill operation attribute objects.

The list of common attribute identifiers that may be used for any communication operation:

.. code:: cpp

    enum class operation_attr_id {
        priority    = /* unspecified */,
        to_cache    = /* unspecified */,
        synchronous = /* unspecified */,
        match_id    = /* unspecified */

        last_value  = /* unspecified, equal to the largest of all the values above */
    };

operation_attr_id::priority
    the priority of the communication operation
operation_attr_id::to_cache
    | persistent/non-persistent communication operation
    | should be used in conjunction with ``match_id``
operation_attr_id::synchronous
    synchronous/asynchronous communication operation
operation_attr_id::match_id
    | the unique identifier of the operation
    | enables correct matching and execution of the operations started in different order on different ranks
    | in conjunction with ``to_cache``, it also enables the caching of the communication operation

The communication operation specific attribute identifiers may extend the list of common identifiers.

The list of attribute identifiers that may be used for :ref:`Allreduce`, :ref:`Reduce` and :ref:`ReduceScatter` collective operations:

.. code:: cpp

    enum class allreduce_attr_id {
        reduction_fn = /* unspecified */
    };

    enum class reduce_attr_id {
        reduction_fn = /* unspecified */
    };

    enum class reduce_scatter_attr_id {
        reduction_fn = /* unspecified */
    };

allreduce_attr_id::reduction_fn / reduce_attr_id::reduction_fn / reduce_scatter_attr_id::reduction_fn
    a function pointer for the custom reduction operation that follows the signature:

.. code:: cpp

        typedef void (*ccl_reduction_fn_t)
        (
            const void*,      // in_buf
            size_t,           // in_count
            void*,            // inout_buf
            size_t*,          // out_count
            datatype,         // datatype
            const fn_context* // context
        );

        typedef struct {
            const char* match_id;
            const size_t offset;
        } fn_context;

The ``environment`` class shall provide the ability to create an attribute object for a communication operation.

Creating an operation attribute object, which may be used in a corresponding communication operation:

.. code:: cpp

    template <class OpAttrType>
    OpAttrType environment::create_operation_attr() const;

return ``OpAttrType``
    an object to hold attributes for a specific communication operation

The operation attribute classes shall provide ``get`` and ``set`` methods for getting and setting of values with specific attribute identifiers.
