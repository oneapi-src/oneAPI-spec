==============================
Hardware Device Error Handling
==============================

The SDK accelerates decoding, encoding, and video processing through a hardware
device. The SDK functions may return errors or warnings if the hardware device
encounters errors. See the
:ref:`Hardware Device Errors and Warnings table <hw-device-errors-table>` for
detailed information about the errors and warnings.

.. list-table:: Hardware Device Errors and Warnings
   :header-rows: 1

   * - Status
     - Description
   * - :cpp:enumerator:`mfxStatus::MFX_ERR_DEVICE_FAILED`
     - Hardware device returned unexpected errors. SDK was unable to restore operation.
   * - :cpp:enumerator:`mfxStatus::MFX_ERR_DEVICE_LOST`
     - Hardware device was lost due to system lock or shutdown.
   * - :cpp:enumerator:`mfxStatus::MFX_WRN_PARTIAL_ACCELERATION`
     - The hardware does not fully support the specified configuration. The encoding, decoding, or video processing operation may be partially accelerated.
   * - :cpp:enumerator:`mfxStatus::MFX_WRN_DEVICE_BUSY`
     - Hardware device is currently busy.

.. _hw-device-errors-table:


SDK ``Query``, ``QueryIOSurf``, and ``Init`` functions return
:cpp:enumerator:`mfxStatus::MFX_WRN_PARTIAL_ACCELERATION` to indicate that the encoding,
decoding, or video processing operation can be partially hardware accelerated or
not hardware accelerated at all. The application can ignore this warning and
proceed with the operation. (Note that SDK functions may return
errors or other warnings overwriting
:cpp:enumerator:`mfxStatus::MFX_WRN_PARTIAL_ACCELERATION`, as it is a lower priority warning.)

SDK functions return :cpp:enumerator:`mfxStatus::MFX_WRN_DEVICE_BUSY` to indicate that the
hardware device is busy and unable to take commands at this time. Resume the
operation by waiting for a few milliseconds and resubmitting the request.
The following example shows the decoding pseudo-code:

.. literalinclude:: snippets/prg_err.c
   :language: c++
   :start-after: /*beg1*/
   :end-before: /*end1*/
   :lineno-start: 1

The same procedure applies to encoding and video processing.

SDK functions return :cpp:enumerator:`mfxStatus::MFX_ERR_DEVICE_LOST` or
:cpp:enumerator:`mfxStatus::MFX_ERR_DEVICE_FAILED` to indicate that there is a complete
failure in hardware acceleration. The application must close and reinitialize
the SDK function class. If the application has provided a hardware acceleration
device handle to the SDK, the application must reset the device.



