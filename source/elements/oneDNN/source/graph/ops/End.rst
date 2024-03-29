.. SPDX-FileCopyrightText: 2020-2022 Intel Corporation
..
.. SPDX-License-Identifier: CC-BY-4.0

.. include:: ../../replacements.inc.rst


End
###

End operation is used to help construct graph, for example tracking the
uses of a tensor.

Operation Attributes
********************

End operation does not support any attribute.

Execution Arguments
*******************

The inputs and outputs must be provided according to the below index order
when constructing an operation.

Inputs
======


===== ============= ====================
Index Argument Name Required or Optional
===== ============= ====================
0     ``src``       Required
===== ============= ====================

Outputs
=======


End operation does not support output tensor.


Supported Data Types
********************

End operation supports the following data type combinations.

==== ===========
Src  Destination
==== ===========
f32  f32
bf16 bf16
f16  f16
==== ===========
